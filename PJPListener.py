# Generated from PJP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PJPParser import PJPParser
else:
    from PJPParser import PJPParser

# This class defines a complete listener for a parse tree produced by PJPParser.
class PJPListener(ParseTreeListener):

    # Enter a parse tree produced by PJPParser#prog.
    def enterProg(self, ctx:PJPParser.ProgContext):
        pass

    # Exit a parse tree produced by PJPParser#prog.
    def exitProg(self, ctx:PJPParser.ProgContext):
        pass


    # Enter a parse tree produced by PJPParser#EmptyCommandStat.
    def enterEmptyCommandStat(self, ctx:PJPParser.EmptyCommandStatContext):
        pass

    # Exit a parse tree produced by PJPParser#EmptyCommandStat.
    def exitEmptyCommandStat(self, ctx:PJPParser.EmptyCommandStatContext):
        pass


    # Enter a parse tree produced by PJPParser#ArrayDeclStat.
    def enterArrayDeclStat(self, ctx:PJPParser.ArrayDeclStatContext):
        pass

    # Exit a parse tree produced by PJPParser#ArrayDeclStat.
    def exitArrayDeclStat(self, ctx:PJPParser.ArrayDeclStatContext):
        pass


    # Enter a parse tree produced by PJPParser#DeclarationStat.
    def enterDeclarationStat(self, ctx:PJPParser.DeclarationStatContext):
        pass

    # Exit a parse tree produced by PJPParser#DeclarationStat.
    def exitDeclarationStat(self, ctx:PJPParser.DeclarationStatContext):
        pass


    # Enter a parse tree produced by PJPParser#ExpressionStat.
    def enterExpressionStat(self, ctx:PJPParser.ExpressionStatContext):
        pass

    # Exit a parse tree produced by PJPParser#ExpressionStat.
    def exitExpressionStat(self, ctx:PJPParser.ExpressionStatContext):
        pass


    # Enter a parse tree produced by PJPParser#ReadStat.
    def enterReadStat(self, ctx:PJPParser.ReadStatContext):
        pass

    # Exit a parse tree produced by PJPParser#ReadStat.
    def exitReadStat(self, ctx:PJPParser.ReadStatContext):
        pass


    # Enter a parse tree produced by PJPParser#WriteStat.
    def enterWriteStat(self, ctx:PJPParser.WriteStatContext):
        pass

    # Exit a parse tree produced by PJPParser#WriteStat.
    def exitWriteStat(self, ctx:PJPParser.WriteStatContext):
        pass


    # Enter a parse tree produced by PJPParser#StatementStat.
    def enterStatementStat(self, ctx:PJPParser.StatementStatContext):
        pass

    # Exit a parse tree produced by PJPParser#StatementStat.
    def exitStatementStat(self, ctx:PJPParser.StatementStatContext):
        pass


    # Enter a parse tree produced by PJPParser#IfStat.
    def enterIfStat(self, ctx:PJPParser.IfStatContext):
        pass

    # Exit a parse tree produced by PJPParser#IfStat.
    def exitIfStat(self, ctx:PJPParser.IfStatContext):
        pass


    # Enter a parse tree produced by PJPParser#WhileStat.
    def enterWhileStat(self, ctx:PJPParser.WhileStatContext):
        pass

    # Exit a parse tree produced by PJPParser#WhileStat.
    def exitWhileStat(self, ctx:PJPParser.WhileStatContext):
        pass


    # Enter a parse tree produced by PJPParser#varType.
    def enterVarType(self, ctx:PJPParser.VarTypeContext):
        pass

    # Exit a parse tree produced by PJPParser#varType.
    def exitVarType(self, ctx:PJPParser.VarTypeContext):
        pass


    # Enter a parse tree produced by PJPParser#AndExpr.
    def enterAndExpr(self, ctx:PJPParser.AndExprContext):
        pass

    # Exit a parse tree produced by PJPParser#AndExpr.
    def exitAndExpr(self, ctx:PJPParser.AndExprContext):
        pass


    # Enter a parse tree produced by PJPParser#BoolExpr.
    def enterBoolExpr(self, ctx:PJPParser.BoolExprContext):
        pass

    # Exit a parse tree produced by PJPParser#BoolExpr.
    def exitBoolExpr(self, ctx:PJPParser.BoolExprContext):
        pass


    # Enter a parse tree produced by PJPParser#StringExpr.
    def enterStringExpr(self, ctx:PJPParser.StringExprContext):
        pass

    # Exit a parse tree produced by PJPParser#StringExpr.
    def exitStringExpr(self, ctx:PJPParser.StringExprContext):
        pass


    # Enter a parse tree produced by PJPParser#MultDivModExpr.
    def enterMultDivModExpr(self, ctx:PJPParser.MultDivModExprContext):
        pass

    # Exit a parse tree produced by PJPParser#MultDivModExpr.
    def exitMultDivModExpr(self, ctx:PJPParser.MultDivModExprContext):
        pass


    # Enter a parse tree produced by PJPParser#FloatExpr.
    def enterFloatExpr(self, ctx:PJPParser.FloatExprContext):
        pass

    # Exit a parse tree produced by PJPParser#FloatExpr.
    def exitFloatExpr(self, ctx:PJPParser.FloatExprContext):
        pass


    # Enter a parse tree produced by PJPParser#PlusMinusConcatExpr.
    def enterPlusMinusConcatExpr(self, ctx:PJPParser.PlusMinusConcatExprContext):
        pass

    # Exit a parse tree produced by PJPParser#PlusMinusConcatExpr.
    def exitPlusMinusConcatExpr(self, ctx:PJPParser.PlusMinusConcatExprContext):
        pass


    # Enter a parse tree produced by PJPParser#LogicNotExpr.
    def enterLogicNotExpr(self, ctx:PJPParser.LogicNotExprContext):
        pass

    # Exit a parse tree produced by PJPParser#LogicNotExpr.
    def exitLogicNotExpr(self, ctx:PJPParser.LogicNotExprContext):
        pass


    # Enter a parse tree produced by PJPParser#ArrayAccessExpr.
    def enterArrayAccessExpr(self, ctx:PJPParser.ArrayAccessExprContext):
        pass

    # Exit a parse tree produced by PJPParser#ArrayAccessExpr.
    def exitArrayAccessExpr(self, ctx:PJPParser.ArrayAccessExprContext):
        pass


    # Enter a parse tree produced by PJPParser#OrExpr.
    def enterOrExpr(self, ctx:PJPParser.OrExprContext):
        pass

    # Exit a parse tree produced by PJPParser#OrExpr.
    def exitOrExpr(self, ctx:PJPParser.OrExprContext):
        pass


    # Enter a parse tree produced by PJPParser#AssignExpr.
    def enterAssignExpr(self, ctx:PJPParser.AssignExprContext):
        pass

    # Exit a parse tree produced by PJPParser#AssignExpr.
    def exitAssignExpr(self, ctx:PJPParser.AssignExprContext):
        pass


    # Enter a parse tree produced by PJPParser#EqualNotEqualExpr.
    def enterEqualNotEqualExpr(self, ctx:PJPParser.EqualNotEqualExprContext):
        pass

    # Exit a parse tree produced by PJPParser#EqualNotEqualExpr.
    def exitEqualNotEqualExpr(self, ctx:PJPParser.EqualNotEqualExprContext):
        pass


    # Enter a parse tree produced by PJPParser#VarExpr.
    def enterVarExpr(self, ctx:PJPParser.VarExprContext):
        pass

    # Exit a parse tree produced by PJPParser#VarExpr.
    def exitVarExpr(self, ctx:PJPParser.VarExprContext):
        pass


    # Enter a parse tree produced by PJPParser#ArrayAssignExpr.
    def enterArrayAssignExpr(self, ctx:PJPParser.ArrayAssignExprContext):
        pass

    # Exit a parse tree produced by PJPParser#ArrayAssignExpr.
    def exitArrayAssignExpr(self, ctx:PJPParser.ArrayAssignExprContext):
        pass


    # Enter a parse tree produced by PJPParser#IntExpr.
    def enterIntExpr(self, ctx:PJPParser.IntExprContext):
        pass

    # Exit a parse tree produced by PJPParser#IntExpr.
    def exitIntExpr(self, ctx:PJPParser.IntExprContext):
        pass


    # Enter a parse tree produced by PJPParser#ParenExpr.
    def enterParenExpr(self, ctx:PJPParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PJPParser#ParenExpr.
    def exitParenExpr(self, ctx:PJPParser.ParenExprContext):
        pass


    # Enter a parse tree produced by PJPParser#HigherLowerExpr.
    def enterHigherLowerExpr(self, ctx:PJPParser.HigherLowerExprContext):
        pass

    # Exit a parse tree produced by PJPParser#HigherLowerExpr.
    def exitHigherLowerExpr(self, ctx:PJPParser.HigherLowerExprContext):
        pass


    # Enter a parse tree produced by PJPParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:PJPParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by PJPParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:PJPParser.UnaryMinusExprContext):
        pass



del PJPParser