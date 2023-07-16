import os
from antlr4 import *
import sys
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from YAPLVisitor import YAPLVisitor
from antlr4.InputStream import InputStream


def main():
    
    data = InputStream(sys.stdin.readline())

    #Lexer y Parser de ANTLR
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.program()

    visitor = YAPLVisitor()
    resultTree = visitor.visit(tree)
    print (resultTree)

   
if __name__ == "__main__":
    main()
    