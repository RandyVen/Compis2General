# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPL2Parser import YAPL2Parser
else:
    from YAPL2Parser import YAPL2Parser

# This class defines a complete listener for a parse tree produced by YAPL2Parser.
class YAPL2Listener(ParseTreeListener):

    # Enter a parse tree produced by YAPL2Parser#program.
    def enterProgram(self, ctx:YAPL2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#program.
    def exitProgram(self, ctx:YAPL2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#programBlock.
    def enterProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#programBlock.
    def exitProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#classDEF.
    def enterClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#classDEF.
    def exitClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#MethodDef.
    def enterMethodDef(self, ctx:YAPL2Parser.MethodDefContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#MethodDef.
    def exitMethodDef(self, ctx:YAPL2Parser.MethodDefContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#FeactureDecalration.
    def enterFeactureDecalration(self, ctx:YAPL2Parser.FeactureDecalrationContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#FeactureDecalration.
    def exitFeactureDecalration(self, ctx:YAPL2Parser.FeactureDecalrationContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#formal.
    def enterFormal(self, ctx:YAPL2Parser.FormalContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#formal.
    def exitFormal(self, ctx:YAPL2Parser.FormalContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#newExpr.
    def enterNewExpr(self, ctx:YAPL2Parser.NewExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#newExpr.
    def exitNewExpr(self, ctx:YAPL2Parser.NewExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#divideExpr.
    def enterDivideExpr(self, ctx:YAPL2Parser.DivideExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#divideExpr.
    def exitDivideExpr(self, ctx:YAPL2Parser.DivideExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#FunctionExpr.
    def enterFunctionExpr(self, ctx:YAPL2Parser.FunctionExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#FunctionExpr.
    def exitFunctionExpr(self, ctx:YAPL2Parser.FunctionExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#integerExpr.
    def enterIntegerExpr(self, ctx:YAPL2Parser.IntegerExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#integerExpr.
    def exitIntegerExpr(self, ctx:YAPL2Parser.IntegerExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#trueExpr.
    def enterTrueExpr(self, ctx:YAPL2Parser.TrueExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#trueExpr.
    def exitTrueExpr(self, ctx:YAPL2Parser.TrueExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#MethodExpr.
    def enterMethodExpr(self, ctx:YAPL2Parser.MethodExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#MethodExpr.
    def exitMethodExpr(self, ctx:YAPL2Parser.MethodExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#DeclarationExpression.
    def enterDeclarationExpression(self, ctx:YAPL2Parser.DeclarationExpressionContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#DeclarationExpression.
    def exitDeclarationExpression(self, ctx:YAPL2Parser.DeclarationExpressionContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#ifElseExpr.
    def enterIfElseExpr(self, ctx:YAPL2Parser.IfElseExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#ifElseExpr.
    def exitIfElseExpr(self, ctx:YAPL2Parser.IfElseExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#lessExpr.
    def enterLessExpr(self, ctx:YAPL2Parser.LessExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#lessExpr.
    def exitLessExpr(self, ctx:YAPL2Parser.LessExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#BraketedExpr.
    def enterBraketedExpr(self, ctx:YAPL2Parser.BraketedExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#BraketedExpr.
    def exitBraketedExpr(self, ctx:YAPL2Parser.BraketedExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#multiplyExpr.
    def enterMultiplyExpr(self, ctx:YAPL2Parser.MultiplyExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#multiplyExpr.
    def exitMultiplyExpr(self, ctx:YAPL2Parser.MultiplyExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#letExpr.
    def enterLetExpr(self, ctx:YAPL2Parser.LetExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#letExpr.
    def exitLetExpr(self, ctx:YAPL2Parser.LetExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#stringExpr.
    def enterStringExpr(self, ctx:YAPL2Parser.StringExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#stringExpr.
    def exitStringExpr(self, ctx:YAPL2Parser.StringExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#lessEqualExpr.
    def enterLessEqualExpr(self, ctx:YAPL2Parser.LessEqualExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#lessEqualExpr.
    def exitLessEqualExpr(self, ctx:YAPL2Parser.LessEqualExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#notExpr.
    def enterNotExpr(self, ctx:YAPL2Parser.NotExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#notExpr.
    def exitNotExpr(self, ctx:YAPL2Parser.NotExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#whileExpr.
    def enterWhileExpr(self, ctx:YAPL2Parser.WhileExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#whileExpr.
    def exitWhileExpr(self, ctx:YAPL2Parser.WhileExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#addExpr.
    def enterAddExpr(self, ctx:YAPL2Parser.AddExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#addExpr.
    def exitAddExpr(self, ctx:YAPL2Parser.AddExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#isVoidExpr.
    def enterIsVoidExpr(self, ctx:YAPL2Parser.IsVoidExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#isVoidExpr.
    def exitIsVoidExpr(self, ctx:YAPL2Parser.IsVoidExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#objectIdExpr.
    def enterObjectIdExpr(self, ctx:YAPL2Parser.ObjectIdExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#objectIdExpr.
    def exitObjectIdExpr(self, ctx:YAPL2Parser.ObjectIdExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#substractExpr.
    def enterSubstractExpr(self, ctx:YAPL2Parser.SubstractExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#substractExpr.
    def exitSubstractExpr(self, ctx:YAPL2Parser.SubstractExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#falseExpr.
    def enterFalseExpr(self, ctx:YAPL2Parser.FalseExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#falseExpr.
    def exitFalseExpr(self, ctx:YAPL2Parser.FalseExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#parenthExpr.
    def enterParenthExpr(self, ctx:YAPL2Parser.ParenthExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#parenthExpr.
    def exitParenthExpr(self, ctx:YAPL2Parser.ParenthExprContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#equalExpr.
    def enterEqualExpr(self, ctx:YAPL2Parser.EqualExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#equalExpr.
    def exitEqualExpr(self, ctx:YAPL2Parser.EqualExprContext):
        pass



del YAPL2Parser