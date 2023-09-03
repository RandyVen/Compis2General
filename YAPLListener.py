# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#programBlock.
    def enterProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#programBlock.
    def exitProgramBlock(self, ctx:YAPLParser.ProgramBlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#classDEF.
    def enterClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        pass

    # Exit a parse tree produced by YAPLParser#classDEF.
    def exitClassDEF(self, ctx:YAPLParser.ClassDEFContext):
        pass


    # Enter a parse tree produced by YAPLParser#MethodDef.
    def enterMethodDef(self, ctx:YAPLParser.MethodDefContext):
        pass

    # Exit a parse tree produced by YAPLParser#MethodDef.
    def exitMethodDef(self, ctx:YAPLParser.MethodDefContext):
        pass


    # Enter a parse tree produced by YAPLParser#FeactureDecalration.
    def enterFeactureDecalration(self, ctx:YAPLParser.FeactureDecalrationContext):
        pass

    # Exit a parse tree produced by YAPLParser#FeactureDecalration.
    def exitFeactureDecalration(self, ctx:YAPLParser.FeactureDecalrationContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#newExpr.
    def enterNewExpr(self, ctx:YAPLParser.NewExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#newExpr.
    def exitNewExpr(self, ctx:YAPLParser.NewExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#divideExpr.
    def enterDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#divideExpr.
    def exitDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#FunctionExpr.
    def enterFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#FunctionExpr.
    def exitFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#integerExpr.
    def enterIntegerExpr(self, ctx:YAPLParser.IntegerExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#integerExpr.
    def exitIntegerExpr(self, ctx:YAPLParser.IntegerExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#trueExpr.
    def enterTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#trueExpr.
    def exitTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#MethodExpr.
    def enterMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#MethodExpr.
    def exitMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#DeclarationExpression.
    def enterDeclarationExpression(self, ctx:YAPLParser.DeclarationExpressionContext):
        pass

    # Exit a parse tree produced by YAPLParser#DeclarationExpression.
    def exitDeclarationExpression(self, ctx:YAPLParser.DeclarationExpressionContext):
        pass


    # Enter a parse tree produced by YAPLParser#ifElseExpr.
    def enterIfElseExpr(self, ctx:YAPLParser.IfElseExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#ifElseExpr.
    def exitIfElseExpr(self, ctx:YAPLParser.IfElseExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessExpr.
    def enterLessExpr(self, ctx:YAPLParser.LessExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessExpr.
    def exitLessExpr(self, ctx:YAPLParser.LessExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#BraketedExpr.
    def enterBraketedExpr(self, ctx:YAPLParser.BraketedExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#BraketedExpr.
    def exitBraketedExpr(self, ctx:YAPLParser.BraketedExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#multiplyExpr.
    def enterMultiplyExpr(self, ctx:YAPLParser.MultiplyExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#multiplyExpr.
    def exitMultiplyExpr(self, ctx:YAPLParser.MultiplyExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#letExpr.
    def enterLetExpr(self, ctx:YAPLParser.LetExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#letExpr.
    def exitLetExpr(self, ctx:YAPLParser.LetExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#neggateExpr.
    def enterNeggateExpr(self, ctx:YAPLParser.NeggateExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#neggateExpr.
    def exitNeggateExpr(self, ctx:YAPLParser.NeggateExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#stringExpr.
    def enterStringExpr(self, ctx:YAPLParser.StringExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#stringExpr.
    def exitStringExpr(self, ctx:YAPLParser.StringExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessEqualExpr.
    def enterLessEqualExpr(self, ctx:YAPLParser.LessEqualExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessEqualExpr.
    def exitLessEqualExpr(self, ctx:YAPLParser.LessEqualExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#notExpr.
    def enterNotExpr(self, ctx:YAPLParser.NotExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#notExpr.
    def exitNotExpr(self, ctx:YAPLParser.NotExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#whileExpr.
    def enterWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#whileExpr.
    def exitWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#addExpr.
    def enterAddExpr(self, ctx:YAPLParser.AddExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#addExpr.
    def exitAddExpr(self, ctx:YAPLParser.AddExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#isVoidExpr.
    def enterIsVoidExpr(self, ctx:YAPLParser.IsVoidExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#isVoidExpr.
    def exitIsVoidExpr(self, ctx:YAPLParser.IsVoidExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#objectIdExpr.
    def enterObjectIdExpr(self, ctx:YAPLParser.ObjectIdExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#objectIdExpr.
    def exitObjectIdExpr(self, ctx:YAPLParser.ObjectIdExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#substractExpr.
    def enterSubstractExpr(self, ctx:YAPLParser.SubstractExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#substractExpr.
    def exitSubstractExpr(self, ctx:YAPLParser.SubstractExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#falseExpr.
    def enterFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#falseExpr.
    def exitFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#parenthExpr.
    def enterParenthExpr(self, ctx:YAPLParser.ParenthExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#parenthExpr.
    def exitParenthExpr(self, ctx:YAPLParser.ParenthExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#equalExpr.
    def enterEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#equalExpr.
    def exitEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        pass



del YAPLParser