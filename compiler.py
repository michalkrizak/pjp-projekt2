import sys
from antlr4 import *
from PJPLexer import PJPLexer
from PJPParser import PJPParser
from PJPVisitor import PJPVisitor


# Prevod nazvu typu na pismeno pro instrukce
def tl(typ):
    return {'int': 'I', 'float': 'F', 'bool': 'B', 'string': 'S'}[typ]


class TypeChecker(PJPVisitor):

    def __init__(self):
        self.variables = {}  # jmeno -> typ
        self.errors = []

    def visitProg(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    def visitEmptyCommandStat(self, ctx):
        pass

    def visitDeclarationStat(self, ctx):
        typ = ctx.varType().getText()
        for id_tok in ctx.VAR():
            name = id_tok.getText()
            if name in self.variables:
                self.errors.append(f"Error: '{name}' already declared")
            else:
                self.variables[name] = typ

    def visitExpressionStat(self, ctx):
        self.visit(ctx.expression())

    def visitReadStat(self, ctx):
        for id_tok in ctx.VAR():
            name = id_tok.getText()
            if name not in self.variables:
                self.errors.append(f"Error: '{name}' not declared")

    def visitWriteStat(self, ctx):
        for e in ctx.expression():
            self.visit(e)

    def visitStatementStat(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    def visitIfStat(self, ctx):
        cond = self.visit(ctx.expression())
        if cond != 'bool':
            self.errors.append("Error: if condition must be bool")
        for s in ctx.statement():
            self.visit(s)

    def visitWhileStat(self, ctx):
        cond = self.visit(ctx.expression())
        if cond != 'bool':
            self.errors.append("Error: while condition must be bool")
        for s in ctx.statement():
            self.visit(s)

    def visitVarType(self, ctx):
        pass

    def visitAndExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if l != 'bool' or r != 'bool':
            self.errors.append("Error: && requires bool operands")
        return 'bool'
    
    def visitOrExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if l != 'bool' or r != 'bool':
            self.errors.append("Error: || requires bool operands")
        return 'bool'


    def visitMultDivModExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == '%':
            if l != 'int' or r != 'int':
                self.errors.append("Error: % requires int operands")
            return 'int'
        if l in ('int', 'float') and r in ('int', 'float'):
            return 'float' if 'float' in (l, r) else 'int'
        self.errors.append("Error: * / type mismatch")
        return None

    def visitPlusMinusConcatExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        op = ctx.op.text
        if op == '.':
            if l != 'string' or r != 'string':
                self.errors.append("Error: . only works with strings")
            return 'string'
        if op == '+':
            if l == 'string' or r == 'string':
                self.errors.append("Error: + doesn't work with strings")
                return None
        if op == '-':
            if l == 'string' or r == 'string':
                self.errors.append("Error: - doesn't work with strings")
                return None
        if l in ('int', 'float') and r in ('int', 'float'):
            return 'float' if 'float' in (l, r) else 'int'
        self.errors.append("Error: +/- type mismatch")
        return None

    def visitVarExpr(self, ctx):
        name = ctx.VAR().getText()
        if name not in self.variables:
            self.errors.append(f"Error: '{name}' not declared")
            return None
        return self.variables[name]

    def visitLogicNotExpr(self, ctx):
        t = self.visit(ctx.expression())
        if t != 'bool':
            self.errors.append("Error: ! requires bool operand")
        return 'bool'

    def visitAssignExpr(self, ctx):
        name = ctx.VAR().getText()
        if name not in self.variables:
            self.errors.append(f"Error: '{name}' not declared")
            return None
        var_type = self.variables[name]
        val_type = self.visit(ctx.expression())
        if val_type is None:
            return var_type
        if var_type == 'float' and val_type == 'int':
            return var_type
        if var_type != val_type:
            self.errors.append(f"Error: cannot assign {val_type} to {var_type} (variable '{name}')")
        return var_type

    def visitEqualNotEqualExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if ((l == 'int' or l == 'float') and (r == 'int' or r == 'float')):
            return 'bool'
        if l != r:
            self.errors.append("Error: == / != type mismatch")
            return 'bool'
        if l not in ('int', 'float', 'string'):
            self.errors.append(f"Error: == / != not supported for {l}")
        return 'bool'

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())
    
    def visitHigherLowerExpr(self, ctx):
        l = self.visit(ctx.expression(0))
        r = self.visit(ctx.expression(1))
        if ((l == 'int' or l == 'float') and (r == 'int' or r == 'float')):
            return 'bool'
        if l != r or l not in ('int', 'float'):
            self.errors.append("Error: < / > requires int or float")
        return 'bool'
   
    def visitUnaryMinusExpr(self, ctx):
        t = self.visit(ctx.expression())
        if t not in ('int', 'float'):
            self.errors.append("Error: unary - requires int or float")
            return None
        return t
    
    def visitBoolExpr(self, ctx):
        return 'bool'

    def visitStringExpr(self, ctx):
        return 'string'
    
    def visitFloatExpr(self, ctx):
        return 'float'
    
    def visitIntExpr(self, ctx):
        return 'int'
    
    
    
class CodeGenerator(PJPVisitor):

    def __init__(self, variables):
        self.variables = variables
        self.instructions = []
        self.label_count = 0

    def emit(self, instr):
        self.instructions.append(instr)

    def new_label(self):
        n = self.label_count
        self.label_count += 1
        return n
    
    def infer_type(self, ctx):
        if isinstance(ctx, PJPParser.IntExprContext):
            return 'int'
        if isinstance(ctx, PJPParser.FloatExprContext):
            return 'float'
        if isinstance(ctx, PJPParser.BoolExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.StringExprContext):
            return 'string'
        if isinstance(ctx, PJPParser.VarExprContext):
            return self.variables[ctx.VAR().getText()]
        if isinstance(ctx, PJPParser.ParenExprContext):
            return self.infer_type(ctx.expression())
        if isinstance(ctx, PJPParser.UnaryMinusExprContext):
            return self.infer_type(ctx.expression())
        if isinstance(ctx, PJPParser.LogicNotExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.AssignExprContext):
            return self.variables[ctx.VAR().getText()]
        if isinstance(ctx, PJPParser.OrExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.AndExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.EqualNotEqualExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.HigherLowerExprContext):
            return 'bool'
        if isinstance(ctx, PJPParser.PlusMinusConcatExprContext):
            op = ctx.op.text
            if op == '.':
                return 'string'
            l = self.infer_type(ctx.expression(0))
            r = self.infer_type(ctx.expression(1))
            return 'float' if 'float' in (l, r) else 'int'
        if isinstance(ctx, PJPParser.MultDivModExprContext):
            op = ctx.op.text
            if op == '%':
                return 'int'
            l = self.infer_type(ctx.expression(0))
            r = self.infer_type(ctx.expression(1))
            return 'float' if 'float' in (l, r) else 'int'
        return None
    
    def visitProg(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    def visitEmptyCommandStat(self, ctx):
        pass

    def visitDeclarationStat(self, ctx):
        typ = ctx.varType().getText()
        defaults = {'int': 'push I 0', 'float': 'push F 0.0', 'bool': 'push B false', 'string': 'push S ""'}
        for id_tok in ctx.VAR():
            name = id_tok.getText()
            self.emit(defaults[typ])
            self.emit(f'save {name}')

    def visitExpressionStat(self, ctx):
        self.visit(ctx.expression())
        self.emit('pop')

    def visitReadStat(self, ctx):
        for id_tok in ctx.VAR():
            name = id_tok.getText()
            self.emit(f'read {tl(self.variables[name])}')
            self.emit(f'save {name}')

    def visitWriteStat(self, ctx):
        count = 0
        for e in ctx.expression():
            self.visit(e)
            count += 1
        self.emit(f'print {count}')

    def visitStatementStat(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    def visitIfStat(self, ctx):
        l_else = self.new_label()
        l_end = self.new_label()
        self.visit(ctx.expression())
        self.emit(f'fjmp {l_else}')
        self.visit(ctx.statement(0))
        self.emit(f'jmp {l_end}')
        self.emit(f'label {l_else}')
        if len(ctx.statement()) > 1:
            self.visit(ctx.statement(1))
        self.emit(f'label {l_end}')

    def visitWhileStat(self, ctx):
        l_start = self.new_label()
        l_end = self.new_label()
        self.emit(f'label {l_start}')
        self.visit(ctx.expression())
        self.emit(f'fjmp {l_end}')
        self.visit(ctx.statement(0))
        self.emit(f'jmp {l_start}')
        self.emit(f'label {l_end}')

    def visitVarType(self, ctx):
        pass

    def visitAndExpr(self, ctx):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.emit('and')
        return 'bool'
    
    def visitOrExpr(self, ctx):
        self.visit(ctx.expression(0))
        self.visit(ctx.expression(1))
        self.emit('or')
        return 'bool'


    def visitMultDivModExpr(self, ctx):
        op = ctx.op.text
        l_type = self.infer_type(ctx.expression(0))
        r_type = self.infer_type(ctx.expression(1))
        result_type = 'int' if op == '%' else ('float' if 'float' in (l_type, r_type) else 'int')
        self.visit(ctx.expression(0))
        if l_type == 'int' and result_type == 'float':
            self.emit('itof')
        self.visit(ctx.expression(1))
        if r_type == 'int' and result_type == 'float':
            self.emit('itof')
        if op == '*':
            self.emit(f'mul {tl(result_type)}')
        elif op == '/':
            self.emit(f'div {tl(result_type)}')
        else:
            self.emit('mod')
        return result_type

    def visitPlusMinusConcatExpr(self, ctx):
        op = ctx.op.text
        l_type = self.infer_type(ctx.expression(0))
        r_type = self.infer_type(ctx.expression(1))
        result_type = 'string' if op == '.' else ('float' if 'float' in (l_type, r_type) else 'int')
        self.visit(ctx.expression(0))
        if l_type == 'int' and result_type == 'float':
            self.emit('itof')
        self.visit(ctx.expression(1))
        if r_type == 'int' and result_type == 'float':
            self.emit('itof')
        if op == '.':
            self.emit('concat')
        elif op == '+':
            self.emit(f'add {tl(result_type)}')
        else:
            self.emit(f'sub {tl(result_type)}')
        return result_type

    def visitVarExpr(self, ctx):
        name = ctx.VAR().getText()
        self.emit(f'load {name}')
        return self.variables[name]

    def visitLogicNotExpr(self, ctx):
        self.visit(ctx.expression())
        self.emit('not')
        return 'bool'

    def visitAssignExpr(self, ctx):
        name = ctx.VAR().getText()
        var_type = self.variables[name]
        val_type = self.visit(ctx.expression())
        if val_type == 'int' and var_type == 'float':
            self.emit('itof')
        self.emit(f'save {name}')
        self.emit(f'load {name}')
        return var_type

    def visitEqualNotEqualExpr(self, ctx):
        op = ctx.op.text
        l_type = self.infer_type(ctx.expression(0))
        r_type = self.infer_type(ctx.expression(1))
        cmp_type = 'float' if 'float' in (l_type, r_type) else l_type
        self.visit(ctx.expression(0))
        if l_type == 'int' and cmp_type == 'float':
            self.emit('itof')
        self.visit(ctx.expression(1))
        if r_type == 'int' and cmp_type == 'float':
            self.emit('itof')
        self.emit(f'eq {tl(cmp_type)}')
        if op == '!=':
            self.emit('not')
        return 'bool'

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())
    
    def visitHigherLowerExpr(self, ctx):
        op = ctx.op.text
        l_type = self.infer_type(ctx.expression(0))
        r_type = self.infer_type(ctx.expression(1))
        cmp_type = 'float' if 'float' in (l_type, r_type) else 'int'
        self.visit(ctx.expression(0))
        if l_type == 'int' and cmp_type == 'float':
            self.emit('itof')
        self.visit(ctx.expression(1))
        if r_type == 'int' and cmp_type == 'float':
            self.emit('itof')
        if op == '<':
            self.emit(f'lt {tl(cmp_type)}')
        else:
            self.emit(f'gt {tl(cmp_type)}')
        return 'bool'
   
    def visitUnaryMinusExpr(self, ctx):
        t = self.visit(ctx.expression())
        self.emit(f'uminus {tl(t)}')
        return t
    
    def visitBoolExpr(self, ctx):
        self.emit(f'push B {ctx.BOOL().getText()}')
        return 'bool'

    def visitStringExpr(self, ctx):
        self.emit(f'push S {ctx.STRING().getText()}')
        return 'string'
    
    def visitFloatExpr(self, ctx):
        self.emit(f'push F {ctx.FLOAT().getText()}')
        return 'float'
    
    def visitIntExpr(self, ctx):
        self.emit(f'push I {ctx.INT().getText()}')
        return 'int'

def main():
    if len(sys.argv) < 2:
        print("Pouziti: python compiler.py <vstupni_soubor>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        source = f.read()

    input_stream = InputStream(source)
    lexer = PJPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PJPParser(stream)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"{parser.getNumberOfSyntaxErrors()} syntakticka chyba(y), konec.")
        sys.exit(1)

    checker = TypeChecker()
    checker.visit(tree)

    if checker.errors:
        for e in checker.errors:
            print(e)
        sys.exit(1)

    gen = CodeGenerator(checker.variables)
    gen.visit(tree)

    output_file = sys.argv[1].rsplit('.', 1)[0] + '.instr'
    with open(output_file, 'w') as f:
        for instr in gen.instructions:
            f.write(instr + '\n')

    print(f"Vygenerovano: {output_file}")


if __name__ == '__main__':
    main()
