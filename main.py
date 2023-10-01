import os
from antlr4 import *
from antlr4.tree.Trees import Trees

from YAPL2Lexer import YAPL2Lexer
from YAPL2Parser import YAPL2Parser
from YAPL2Visitor import YAPL2Visitor
from first_visitor import FirstVisitor
from intermediateCodeGenerator import IntermediateCodeGenerator
from errors import semanticError

import tkinter as tk
from tkinter import filedialog as fd


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
    buttonsFrame = tk.Frame(window)
    buttonsFrame.pack()
    window.title("YAPL2 Code")
    user_input = tk.Text(width=100)
    errorsWindow = tk.Text(width = 100)
    compileButton = tk.Button(buttonsFrame, text="Compile", command=lambda: main(user_input.get("1.0", tk.END), errorsWindow))
    loadButton = tk.Button(buttonsFrame, text="Load File", command=lambda: loadFile(user_input))
    

    compileButton.pack(side=tk.LEFT)
    loadButton.pack(side=tk.LEFT)
    user_input.pack(fill=tk.X)
    errorsWindow.pack(fill = tk.X)
    
    window.mainloop()

def loadFile(userInputWindow):
    userInputWindow.delete("1.0", tk.END)
    filename = fd.askopenfilename(initialdir = os.getcwd(), title = "Select file")
    with open(filename, 'r') as f:
        lines = f.read()
        userInputWindow.insert(tk.END, lines)

def main(program, errorsWindow):
    errorsWindow.delete("1.0", tk.END)
    data = InputStream(program)
    #lexer
    lexer = YAPL2Lexer(data)
    stream = CommonTokenStream(lexer)
    #parser
    parser = YAPL2Parser(stream)
    tree = parser.program()

    #Semantic analysis
    firstVisitor = FirstVisitor()
    firstVisitor.visit(tree)

    #tablePrint(firstVisitor)
    

    visitor = YAPL2Visitor(firstVisitor.classTable, firstVisitor.functionTable, firstVisitor.attributeTable, firstVisitor.typesTable, firstVisitor.foundErrors)
    visitor.visit(tree)
    # Showing tables
    
    tablePrint(visitor)
    
    if not visitor.classTable.findEntry("Main"):
        error = semanticError(1, "Class Main not defined")
        visitor.foundErrors.append(error)
    
    if not visitor.functionTable.findEntryByName("main", "Main"):
        error = semanticError(1, "Function main not defined in main")
        visitor.foundErrors.append(error)

    if len(visitor.foundErrors) > 0:
        for i in visitor.foundErrors:
            errorsWindow.insert(tk.END,str(i)+"\n")
    else:
        errorsWindow.insert(tk.END, "No errors :D\n")

    intCodeGenerator = IntermediateCodeGenerator(visitor.classTable, visitor.functionTable, visitor.attributeTable, visitor.typesTable)
    intCodeGenerator.visit(tree)
    
if __name__ == "__main__":
    gui()