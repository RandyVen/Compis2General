import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from antlr4 import *
from antlr4.tree.Trees import Trees
from YAPL2Lexer import YAPL2Lexer
from YAPL2Parser import YAPL2Parser
from YAPL2Visitor import YAPL2Visitor
from first_visitor import FirstVisitor
from intermediate_code_generator import IntermediateCodeGenerator
from errors import semanticError

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

def set_dark_mode(widget):
    widget.configure(bg="#2E2E2E", fg="white")

def gui():
    window = tk.Tk()
    window.configure(bg="#2E2E2E")  # Set the main window background color
    buttonsFrame = tk.Frame(window, bg="#2E2E2E")
    codeAndIC = tk.Frame(window, bg="#2E2E2E")
    buttonsFrame.pack(side=tk.LEFT)  # Move buttons to the left side
    codeAndIC.pack(fill=tk.BOTH, expand=True)
    window.title("YAPL2 Code")

    user_input = tk.Text(codeAndIC)
    set_dark_mode(user_input)
    intermediateCode = tk.Text(codeAndIC)
    set_dark_mode(intermediateCode)

    errorsWindow = tk.Text(width=100)
    set_dark_mode(errorsWindow)  # Set dark mode for errorsWindow

    # Create a ttk.Style object for customizing widget styles
    style = ttk.Style()
    style.theme_use('clam')  # Use the 'clam' theme (you can choose other themes)

    # Define dark mode colors for buttons
    dark_button_background = '#2E2E2E'
    dark_button_foreground = 'white'

    # Configure the style for buttons
    style.configure('Dark.TButton', background=dark_button_background, foreground=dark_button_foreground)
    
    compileButton = ttk.Button(buttonsFrame, text="Compile", command=lambda: main(user_input.get("1.0", tk.END), errorsWindow, intermediateCode), style='Dark.TButton')
    loadButton = ttk.Button(buttonsFrame, text="Load File", command=lambda: loadFile(user_input), style='Dark.TButton')

    compileButton.pack(side=tk.LEFT, fill=tk.X)
    loadButton.pack(side=tk.LEFT, fill=tk.BOTH)
    user_input.pack(side=tk.LEFT, fill=tk.Y)
    intermediateCode.pack(side=tk.RIGHT, fill=tk.Y)
    errorsWindow.pack(fill=tk.BOTH, expand=True)

    window.mainloop()

def loadFile(userInputWindow):
    userInputWindow.delete("1.0", tk.END)
    filename = fd.askopenfilename(initialdir=os.getcwd(), title="Select file")
    with open(filename, 'r') as f:
        lines = f.read()
        userInputWindow.insert(tk.END, lines)

def main(program, errorsWindow, interMediateCodeWindow):
    errorsWindow.delete("1.0", tk.END)
    interMediateCodeWindow.delete("1.0", tk.END)
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
    
    #tablePrint(visitor)
    
    if not visitor.classTable.findEntry("Main"):
        error = semanticError(1, "Class Main not defined")
        visitor.foundErrors.append(error)
    
    if not visitor.functionTable.findEntryByName("main", "Main"):
        error = semanticError(1, "Function main not defined in main")
        visitor.foundErrors.append(error)

    if len(visitor.foundErrors) > 0:
        for i in visitor.foundErrors:
            errorsWindow.insert(tk.END, str(i) + "\n")
            interMediateCodeWindow.insert(tk.END, "Trash in trash out, fix errors")
            return -1
    else:
        errorsWindow.insert(tk.END, "No errors :D\n")

    intCodeGenerator = IntermediateCodeGenerator(visitor.classTable, visitor.functionTable, visitor.attributeTable, visitor.typesTable)
    intermediateCode = intCodeGenerator.visit(tree)
    interMediateCodeWindow.insert(tk.END, str(intermediateCode))

if __name__ == "__main__":
    gui()
