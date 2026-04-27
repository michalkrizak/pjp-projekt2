# Generated from PJP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PJPParser import PJPParser
else:
    from PJPParser import PJPParser

# This class defines a complete generic visitor for a parse tree produced by PJPParser.

class PJPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PJPParser#prog.
    def visitProg(self, ctx:PJPParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#EmptyCommandStat.
    def visitEmptyCommandStat(self, ctx:PJPParser.EmptyCommandStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#DeclarationStat.
    def visitDeclarationStat(self, ctx:PJPParser.DeclarationStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#ExpressionStat.
    def visitExpressionStat(self, ctx:PJPParser.ExpressionStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#ReadStat.
    def visitReadStat(self, ctx:PJPParser.ReadStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#WriteStat.
    def visitWriteStat(self, ctx:PJPParser.WriteStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#StatementStat.
    def visitStatementStat(self, ctx:PJPParser.StatementStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#IfStat.
    def visitIfStat(self, ctx:PJPParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#WhileStat.
    def visitWhileStat(self, ctx:PJPParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#DoWhileStat.
    def visitDoWhileStat(self, ctx:PJPParser.DoWhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#ForStat.
    def visitForStat(self, ctx:PJPParser.ForStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#FopenStat.
    def visitFopenStat(self, ctx:PJPParser.FopenStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#FwriteStat.
    def visitFwriteStat(self, ctx:PJPParser.FwriteStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#FappendStat.
    def visitFappendStat(self, ctx:PJPParser.FappendStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#FileStreamStat.
    def visitFileStreamStat(self, ctx:PJPParser.FileStreamStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#varType.
    def visitVarType(self, ctx:PJPParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#AndExpr.
    def visitAndExpr(self, ctx:PJPParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#BoolExpr.
    def visitBoolExpr(self, ctx:PJPParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#StringExpr.
    def visitStringExpr(self, ctx:PJPParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#MultDivModExpr.
    def visitMultDivModExpr(self, ctx:PJPParser.MultDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#FloatExpr.
    def visitFloatExpr(self, ctx:PJPParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#PlusMinusConcatExpr.
    def visitPlusMinusConcatExpr(self, ctx:PJPParser.PlusMinusConcatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#LogicNotExpr.
    def visitLogicNotExpr(self, ctx:PJPParser.LogicNotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#LenExpr.
    def visitLenExpr(self, ctx:PJPParser.LenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#OrExpr.
    def visitOrExpr(self, ctx:PJPParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#AssignExpr.
    def visitAssignExpr(self, ctx:PJPParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#CharAtExpr.
    def visitCharAtExpr(self, ctx:PJPParser.CharAtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#EqualNotEqualExpr.
    def visitEqualNotEqualExpr(self, ctx:PJPParser.EqualNotEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#VarExpr.
    def visitVarExpr(self, ctx:PJPParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#IntExpr.
    def visitIntExpr(self, ctx:PJPParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#ParenExpr.
    def visitParenExpr(self, ctx:PJPParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#HigherLowerExpr.
    def visitHigherLowerExpr(self, ctx:PJPParser.HigherLowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:PJPParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)



del PJPParser