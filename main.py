import os
from antlr4 import *
import sys
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from antlr4.InputStream import InputStream
from antlr4.tree.Trees import Trees

def main():

    filename = input("dame el filename: ")   
    
    data = FileStream(filename)
    print('data')
    print(data)

    #Lexer y Parser de ANTLR
    #comps1
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.program()
    print(Trees.toStringTree(tree,None,parser))
    print('tree')

    print(tree)


    print("Tokens:")
    for token in stream.tokens:
        print(" ",token.text, ':', token.type)
    comand = 'antlr4-parse YAPL.g4 program -gui %s'%filename
    os.system(comand)

   
if __name__ == "__main__":
    main()
    