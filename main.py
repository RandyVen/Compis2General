import sys
import os
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser
from YAPLVisitor_edited_base import YaplVisitorEditedBase
from antlr4.tree.Trees import Trees
import tkinter as tk


def tablePrint(visitor):
    print("==============================SYMBOL TABLE==============================")
    print("==============================ATTRIBUTE TABLE==============================")
    for i in visitor.attributeTable.entries:
        print(i)
    print("==============================TYPES TABLE==============================")
    for i in visitor.typesTable.entries:
        print(i)
    print("==============================CLASS TABLE==============================")
    for i in visitor.classTable.entries:
        print(i)
    print("==============================FUNCTION TABLE==============================")
    for i in visitor.functionTable.entries:
        print(i)
    print("==============================END==============================")

def gui():
    window = tk.Tk()
    window.title("YAPL2 Code")
    user_input = tk.Text()
    compileButton = tk.Button(window, text="Compile", command=lambda: main(user_input.get("1.0", tk.END)))
    
    user_input.pack()
    compileButton.pack()
    
    window.mainloop()

def main(program):
    data = InputStream(program)
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
    
    tablePrint(visitor)

    print(len(visitor.foundErrors))
    for i in visitor.foundErrors:
        print(i)
    
if __name__ == "__main__":
    gui()

    