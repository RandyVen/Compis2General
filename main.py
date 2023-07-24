from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from YAPLVisitor_edited_base import YaplVisitorEditedBase
from antlr4.tree.Trees import Trees

def main():
    filename = input('filename:')
    file = filename
    data = FileStream(file)
    #lexer
    lexer = YAPLLexer(data)
    stream = CommonTokenStream(lexer)
    #parser
    parser = YAPLParser(stream)
    tree = parser.program()

    #Semantic analysis
    visitor = YaplVisitorEditedBase()
    result = visitor.visit(tree)
    # Showing tables
    
if __name__ == "__main__":
    main()
    #tablePrint()