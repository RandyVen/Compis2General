# Generated from YAPL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#start.
    def enterStart(self, ctx:YAPLParser.StartContext):
        pass

    # Exit a parse tree produced by YAPLParser#start.
    def exitStart(self, ctx:YAPLParser.StartContext):
        pass


    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#classExpr.
    def enterClassExpr(self, ctx:YAPLParser.ClassExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#classExpr.
    def exitClassExpr(self, ctx:YAPLParser.ClassExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#method.
    def enterMethod(self, ctx:YAPLParser.MethodContext):
        pass

    # Exit a parse tree produced by YAPLParser#method.
    def exitMethod(self, ctx:YAPLParser.MethodContext):
        pass


    # Enter a parse tree produced by YAPLParser#attribute.
    def enterAttribute(self, ctx:YAPLParser.AttributeContext):
        pass

    # Exit a parse tree produced by YAPLParser#attribute.
    def exitAttribute(self, ctx:YAPLParser.AttributeContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#add.
    def enterAdd(self, ctx:YAPLParser.AddContext):
        pass

    # Exit a parse tree produced by YAPLParser#add.
    def exitAdd(self, ctx:YAPLParser.AddContext):
        pass


    # Enter a parse tree produced by YAPLParser#new.
    def enterNew(self, ctx:YAPLParser.NewContext):
        pass

    # Exit a parse tree produced by YAPLParser#new.
    def exitNew(self, ctx:YAPLParser.NewContext):
        pass


    # Enter a parse tree produced by YAPLParser#negation.
    def enterNegation(self, ctx:YAPLParser.NegationContext):
        pass

    # Exit a parse tree produced by YAPLParser#negation.
    def exitNegation(self, ctx:YAPLParser.NegationContext):
        pass


    # Enter a parse tree produced by YAPLParser#dispatch.
    def enterDispatch(self, ctx:YAPLParser.DispatchContext):
        pass

    # Exit a parse tree produced by YAPLParser#dispatch.
    def exitDispatch(self, ctx:YAPLParser.DispatchContext):
        pass


    # Enter a parse tree produced by YAPLParser#string.
    def enterString(self, ctx:YAPLParser.StringContext):
        pass

    # Exit a parse tree produced by YAPLParser#string.
    def exitString(self, ctx:YAPLParser.StringContext):
        pass


    # Enter a parse tree produced by YAPLParser#assignment.
    def enterAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YAPLParser#assignment.
    def exitAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YAPLParser#false.
    def enterFalse(self, ctx:YAPLParser.FalseContext):
        pass

    # Exit a parse tree produced by YAPLParser#false.
    def exitFalse(self, ctx:YAPLParser.FalseContext):
        pass


    # Enter a parse tree produced by YAPLParser#integer.
    def enterInteger(self, ctx:YAPLParser.IntegerContext):
        pass

    # Exit a parse tree produced by YAPLParser#integer.
    def exitInteger(self, ctx:YAPLParser.IntegerContext):
        pass


    # Enter a parse tree produced by YAPLParser#while.
    def enterWhile(self, ctx:YAPLParser.WhileContext):
        pass

    # Exit a parse tree produced by YAPLParser#while.
    def exitWhile(self, ctx:YAPLParser.WhileContext):
        pass


    # Enter a parse tree produced by YAPLParser#parenthesis.
    def enterParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by YAPLParser#parenthesis.
    def exitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by YAPLParser#equal.
    def enterEqual(self, ctx:YAPLParser.EqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#equal.
    def exitEqual(self, ctx:YAPLParser.EqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#not.
    def enterNot(self, ctx:YAPLParser.NotContext):
        pass

    # Exit a parse tree produced by YAPLParser#not.
    def exitNot(self, ctx:YAPLParser.NotContext):
        pass


    # Enter a parse tree produced by YAPLParser#isVoid.
    def enterIsVoid(self, ctx:YAPLParser.IsVoidContext):
        pass

    # Exit a parse tree produced by YAPLParser#isVoid.
    def exitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        pass


    # Enter a parse tree produced by YAPLParser#function.
    def enterFunction(self, ctx:YAPLParser.FunctionContext):
        pass

    # Exit a parse tree produced by YAPLParser#function.
    def exitFunction(self, ctx:YAPLParser.FunctionContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThan.
    def enterLessThan(self, ctx:YAPLParser.LessThanContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThan.
    def exitLessThan(self, ctx:YAPLParser.LessThanContext):
        pass


    # Enter a parse tree produced by YAPLParser#bracket.
    def enterBracket(self, ctx:YAPLParser.BracketContext):
        pass

    # Exit a parse tree produced by YAPLParser#bracket.
    def exitBracket(self, ctx:YAPLParser.BracketContext):
        pass


    # Enter a parse tree produced by YAPLParser#true.
    def enterTrue(self, ctx:YAPLParser.TrueContext):
        pass

    # Exit a parse tree produced by YAPLParser#true.
    def exitTrue(self, ctx:YAPLParser.TrueContext):
        pass


    # Enter a parse tree produced by YAPLParser#let.
    def enterLet(self, ctx:YAPLParser.LetContext):
        pass

    # Exit a parse tree produced by YAPLParser#let.
    def exitLet(self, ctx:YAPLParser.LetContext):
        pass


    # Enter a parse tree produced by YAPLParser#divide.
    def enterDivide(self, ctx:YAPLParser.DivideContext):
        pass

    # Exit a parse tree produced by YAPLParser#divide.
    def exitDivide(self, ctx:YAPLParser.DivideContext):
        pass


    # Enter a parse tree produced by YAPLParser#id.
    def enterId(self, ctx:YAPLParser.IdContext):
        pass

    # Exit a parse tree produced by YAPLParser#id.
    def exitId(self, ctx:YAPLParser.IdContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessEqual.
    def enterLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessEqual.
    def exitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#multiply.
    def enterMultiply(self, ctx:YAPLParser.MultiplyContext):
        pass

    # Exit a parse tree produced by YAPLParser#multiply.
    def exitMultiply(self, ctx:YAPLParser.MultiplyContext):
        pass


    # Enter a parse tree produced by YAPLParser#ifElse.
    def enterIfElse(self, ctx:YAPLParser.IfElseContext):
        pass

    # Exit a parse tree produced by YAPLParser#ifElse.
    def exitIfElse(self, ctx:YAPLParser.IfElseContext):
        pass


    # Enter a parse tree produced by YAPLParser#substract.
    def enterSubstract(self, ctx:YAPLParser.SubstractContext):
        pass

    # Exit a parse tree produced by YAPLParser#substract.
    def exitSubstract(self, ctx:YAPLParser.SubstractContext):
        pass



del YAPLParser