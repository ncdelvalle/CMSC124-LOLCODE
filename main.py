import os
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Placeholders
with open('file.lol', 'r') as file:
    sampleCode = file.read()


sampleToks = [
    # ("HAI", "Code Delimiter"),
    # ("I HAS A", "Variable Declaration"),
    # ("var", "Variable Identifier"),
    # ("ITZ", "Variable Assignment"),
    # ("12", "Literal"),
    # ("VISIBLE", "Output Keyword"),
    # ("\"", "String Delimiter"),
    # ("noot noot", "Literal"),
    # ("\"", "String Delimiter"),
    # ("var", "Variable Identifier"),
    # ("KTHXBYE", "Code Delimiter"),
]

sampleSyms = [
    ("var", "12"),
    ("IT", "noot noot 12"),
]

consoleOut = "noot noot 12\n"

# For testing
def placeholders(code):
    textEditor.delete("1.0", tk.END)
    textEditor.insert(tk.END, code)

# Global Vars
root = None
defaultDir = os.path.expanduser("~/Downloads/124-proj/lolcodes")

# Widgets
dir = None
fileExp = None
textEditor = None
lexemeTable = None
symbolTable = None
console = None

# Lexeme Functions
    # Tokenizer
def tokenized(code):
    unfinished = re.split('\n', code)
    tokens = []
  
    for line in unfinished:
        tokens.append(line.split(" "))
    keys = [
        "SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD", "BIGGR",
        "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL"
    ]

    for tok in tokens:
        print(tok)
        i = 0
        while i < len(tok):
            if i + 3 < len(tok):
                if tok[i] == "IF" and tok[i+1] == "U" and tok[i+2] == "SAY" and tok[i+3] == "SO":
                    part1 = tok.pop(i+1)
                    part2 = tok.pop(i+1)
                    part3 = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {part1} {part2} {part3}"
                    continue

            if i + 2 < len(tok):
                if tok[i] == "I" and tok[i+1] == "HAS" and tok[i+2] == "A":
                    a = tok.pop(i+1)
                    b = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {a} {b}"
                    continue

                if tok[i] == "IS" and tok[i+1] == "NOW" and tok[i+2] == "A":
                    a = tok.pop(i+1)
                    b = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {a} {b}"
                    continue

                if tok[i] == "HOW" and tok[i+1] == "IZ" and tok[i+2] == "I":
                    a = tok.pop(i+1)
                    b = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {a} {b}"
                    continue

                if tok[i] == "IM" and tok[i+1] == "IN" and tok[i+2] == "YR":
                    a = tok.pop(i+1)
                    b = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {a} {b}"
                    continue

                if tok[i] == "IM" and tok[i+1] == "OUTTA" and tok[i+2] == "YR":
                    a = tok.pop(i+1)
                    b = tok.pop(i+1)
                    tok[i] = f"{tok[i]} {a} {b}"
                    continue

            if i + 1 < len(tok):
                if tok[i] in keys and tok[i+1] == "OF":
                    tok.pop(i+1)
                    tok[i] = f"{tok[i]} OF"
                    continue

                if tok[i] == "BOTH" and tok[i+1] == "SAEM":
                    tok.pop(i+1)
                    tok[i] = "BOTH SAEM"
                    continue

                if tok[i] == "O" and tok[i+1] == "RLY?":
                    tok.pop(i+1)
                    tok[i] = "O RLY?"
                    continue

                if tok[i] == "NO" and tok[i+1] == "WAI":
                    tok.pop(i+1)
                    tok[i] = "NO WAI"
                    continue

                if tok[i] == "FOUND" and tok[i+1] == "YR":
                    tok.pop(i+1)
                    tok[i] = "FOUND YR"
                    continue

                if tok[i] == "I" and tok[i+1] == "IZ":
                    tok.pop(i+1)
                    tok[i] = "I IZ"
                    continue

                if tok[i] == "AN" and tok[i+1] == "YR":
                    tok.pop(i+1)
                    tok[i] = "AN YR"
                    continue
            i += 1
    print(tokens)
    return tokens

    # Sorter functions
def classify_token(tok): 
    variable_assignment = ["ITZ", "R"]
    switch_case_keyword = ["OMG", "OMGWTF"]
    condition_keyword = ["YA RLY", "MEBBE", "NO WAI"]
    loop_keyword = ["TIL", "WILE"]
    return_keyword = ["GTFO", "FOUND YR"]
    parameter_keyword = ["YR", "AN YR"]
    typecast_keyword = ["MAEK", "IS NOW A"]
    function_keyword = ["I IZ", "MKAY"]
    code_delimiter = ['HAI', "KTHXBYE"]
    var_delimiter = ['WAZZUP', 'BUHBYE']
    comment_delimiter = ['BTW', 'OBTW', 'TLDR']
    state_delimiter = ['O RLY?', 'OIC', 'WTF?']
    loop_delimiter = ['IM IN YR', 'IM OUTTA YR']
    func_delimiter = ['HOW IZ I', 'IF U SAY SO']
    comp_operator = ['BOTH SAEM', 'DIFFRINT']
    arith_operator = ['SUM OF', 'DIFF OF', 'PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF', 'UPPN', 'NERFIN']
    bool_operator = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT', 'ANY OF', 'ALL OF', 'SMOOSH']


    if tok == "I HAS A":
        return (tok, "Variable Declaration")
    #FIX PROPER STRING DELIMTER DETECTION :)    
    elif tok == '"': 
        return(tok, "String Delimiter")
    elif tok in variable_assignment:
        return (tok, "Variable Assignment")
    elif tok == "GIMME":
        return (tok, "Input Keyword")
    elif tok == "VISIBLE": 
        return(tok, "Output Keyword")
    elif tok in switch_case_keyword:
        return (tok, "Switch Case Keyword")
    elif tok in condition_keyword:
        return (tok, "Condition Keyword")
    elif tok in loop_keyword:
        return (tok, "Loop Keyword")
    elif tok in return_keyword:
        return (tok, "Return Keyword")
    elif tok in parameter_keyword:
        return (tok, "Parameter_Keyword")
    elif tok in typecast_keyword:
        return (tok, "Typecast Keyword")
    elif tok in function_keyword:
        return (tok, "Function Keyword")
    elif tok in code_delimiter: 
        return (tok, "Code Delimiter")
    elif  tok in var_delimiter: 
        return (tok, "Variable Delimiter")
    elif tok in comment_delimiter: 
        return (tok, "Comment Delimiter")
    elif tok in state_delimiter: 
        return (tok, "Statement Delimiter")
    elif tok in loop_delimiter: 
        return (tok, "Loop Delimiter")
    elif tok in func_delimiter: 
        return (tok, "Function Delimiter")
    elif tok in comp_operator: 
        return(tok, "Comparison Operator")
    elif tok in arith_operator: 
        return(tok, "Arithmetic Operator")
    elif tok in bool_operator: 
        return(tok, "Boolean Operator")
    elif isTroof(tok): 
        return(tok, "Literal")
    elif isNumbr(tok): 
        return(tok, "Literal")
    elif isNumbar(tok): 
        return(tok, "Literal")
    elif isYarn(tok): 
        return(tok, "Literal")
    elif isType(tok): 
        return(tok, "Literal")
    elif isIdentifier(tok): 
        return(tok, "Identifier")
    #edit something so we can differentiate Identifier
    else: 
        return(tok, "Unknown")


    
def isTroof(tok):
    if tok == "WIN" or tok == "FAIL":
        return True
    else:
        return False

def isNumbr(tok):
    regex = r"-?\d+"
    return re.search(regex, tok)

def isNumbar(tok):
    regex = r"-?\d+$"
    return re.search(regex, tok)

def isYarn(tok):
    regex = r"^-?\d+\.\d+$"
    return re.search(regex, tok)

def isType(tok):
    types = ["NOOB", "NUMBR", "NUMBAR", "YARN", "TROOF"]
    if tok in types:
        return True
    else:
        return False

def isIdentifier(tok):
    regex = r"^[A-Za-z][A-Za-z0-9_]*"
    return re.search(regex, tok)

def isVarDec(tok):
    if tok == "I HAS A":
        return ("I HAS A", "Variable Declaration")

def isVarAss(tok):
    variable_assignment = ["ITZ", "R"]
    if tok in variable_assignment:
        return (tok, "Variable Assignment")


def isInput(tok):
    if tok == "GIMME":
        return ("GIMME", "Input Keyword")
   
def isOutput(tok):
    if tok == "VISIBLE":
        return ("VISIBLE", "Output Keyword")


def isSwitch(tok):
    switch_case_keyword = ["OMG", "OMGWTF"]
    if tok in switch_case_keyword:
        return (tok, "Switch Case Keyword")


def isCondition(tok):
    condition_keyword = ["YA RLY", "MEBBE", "NO WAI"]
    if tok in condition_keyword:
        return (tok, "Condition Keyword")


def isLoop(tok):
    loop_keyword = ["TIL", "WILE"]
    if tok in loop_keyword:
        return (tok, "Loop Keyword")


def isReturn(tok):
    return_keyword = ["GTFO", "FOUND YR"]
    if tok in return_keyword:
        return (tok, "Return Keyword")


def isParameter(tok):
    parameter_keyword = ["YR", "AN YR"]
    if tok in parameter_keyword:
        return (tok, "Parameter_Keyword")


def isTypecast(tok):
    typecast_keyword = ["MAEK", "IS NOW A"]
    if tok in typecast_keyword:
        return (tok, "Typecast Keyword")


def isFunction(tok):
    function_keyword = ["I IZ", "MKAY"]
    if tok in function_keyword:
        return (tok, "Function Keyword")


def isCodeDelimiter(tok): 
    delimiter = ['HAI', "KTHXBYE"]
    if tok in delimiter: 
        return (tok, "Code Delimiter")

def isVariableDelimiter(tok): 
    delimiter = ['WAZZUP', 'BUHBYE']
    if tok in delimiter: 
        return (tok, "Variable Delimiter")

def isCommentDelimiter(tok): 
    delimiter = ['BTW', 'OBTW', 'TLDR']
    if tok in delimiter: 
        return (tok, "Comment Delimiter")
    
def isStatementDelimiter(tok): 
    delimiter = ['O RLY?', 'OIC', 'WTF?']
    if tok in delimiter: 
        return (tok, "Statement Delimiter")
    
def isLoopDelimiter(tok): 
    delimiter = ['IM IN YR', 'IM OUTTA YR']
    if tok in delimiter: 
        return (tok, "Loop Delimiter")

def isFunctionDelimiter(tok): 
    delimiter = ['HOW IZ I', 'IF U SAY SO']
    if tok in delimiter: 
        return (tok, "Function Delimiter")

def isComparisonOperator(tok): 
    operator = ['BOTH SAEM', 'DIFFRINT']
    if tok in operator: 
        return(tok, "Comparison Operator")
    
def isArithmeticOperator(tok): 
    operator = ['SUM OF', 'DIFF OF', 'PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF', 'UPPN', 'NERFIN']
    if tok in operator: 
        return(tok, "Arithmetic Operator")
    
def isBooleanOperator(tok): 
    operator = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT', 'ANY OF', 'ALL OF', 'SMOOSH']
    if tok in operator: 
        return(tok, "Boolean Operator")

# ======================

# Functions
def browse_dir():
    global defaultDir
    newdir = filedialog.askdirectory(initialdir=defaultDir, title="Select folder with code files")
    if newdir:
        defaultDir = newdir
        refresh_dir()

def refresh_dir():
    global fileExp, dir, defaultDir
    if not os.path.isdir(defaultDir):
        defaultDir = os.path.expanduser("~")

    dir.config(text=defaultDir)
    fileExp.delete(0, tk.END)
    try:
        names = sorted(os.listdir(defaultDir))
    except Exception:
        names = []

    for name in names:
        if name.startswith("."):
            continue
        full = os.path.join(defaultDir, name)
        if os.path.isfile(full):
            fileExp.insert(tk.END, name)

def open_file(event):
    sel = fileExp.curselection()
    if not sel:
        return
    name = fileExp.get(sel[0])
    full = os.path.join(defaultDir, name)
    try:
        with open(full, "r", encoding="utf-8") as f:
            data = f.read()
    except Exception as e:
        messagebox.showerror("Error", f"Can't Open File\n{e}")
    textEditor.delete("1.0", tk.END)
    textEditor.insert(tk.END, data)

def execute_code():
    sampleToks.clear()
    codeText = textEditor.get("1.0", tk.END).strip()
    placeholders(codeText)
    tokeners = tokenized(codeText)
    for token in tokeners: 
        if len(token) == 1: 
            sampleToks.append(classify_token(token[0]))
        else: 
            for i in range(len(token)): 
                sampleToks.append(classify_token(token[i]))
    
    # Clear old results
    for child in lexemeTable.get_children():
        lexemeTable.delete(child)
    for child in symbolTable.get_children():
        symbolTable.delete(child)
    console.delete("1.0", tk.END)
    
    # Display results
    for lex, cls in sampleToks:
        lexemeTable.insert("", "end", values=(lex, cls))
    for ident, val in sampleSyms:
        symbolTable.insert("", "end", values=(ident, val))
    console.insert(tk.END, consoleOut)


def create_gui(code):
    global root, dir, fileExp, textEditor, lexemeTable, symbolTable, console

    root = tk.Tk()
    root.title("LOLCODE GUI v. alpha x3")
    root.geometry("1100x700")
    root.minsize(900, 600)

    # File Directory
    header = ttk.Frame(root)
    header.pack(side="top", fill="x", padx=6, pady=4)

    ttk.Label(header, text="File:").pack(side="left")
    dir = ttk.Label(header, text=defaultDir)
    dir.pack(side="left", padx=(6, 12))

    ttk.Button(header, text="Browse...", command=browse_dir).pack(side="left")
    ttk.Button(header, text="Reload", command=refresh_dir).pack(side="left", padx=6)
    ttk.Separator(header, orient="horizontal").pack(side="right", fill="x", expand=True)

    # Main paned window
    mainPane = ttk.Panedwindow(root, orient="horizontal")
    mainPane.pack(fill="both", expand=True, padx=6, pady=4)

    # File explorer
    filePane = ttk.Frame(mainPane, width=220)
    mainPane.add(filePane, weight=0)

    ttk.Label(filePane, text="Files").pack(anchor="w", padx=6, pady=(0, 4))
    fileExp = tk.Listbox(filePane, activestyle="none")
    fileExp.pack(fill="both", expand=True, padx=6, pady=4)
    fileExp.bind("<Double-Button-1>", open_file)

    refresh_dir()

    centerPane = ttk.Panedwindow(mainPane, orient="horizontal")
    mainPane.add(centerPane, weight=1)

    # Text editor
    editorPane = ttk.Frame(centerPane)
    centerPane.add(editorPane, weight=1)

    ttk.Label(editorPane, text="Text Editor").pack(anchor="w", padx=6, pady=(0, 4))
    textEditor = ScrolledText(editorPane, wrap="none", undo=True)
    textEditor.pack(fill="both", expand=True, padx=6, pady=4)

    rightPane = ttk.Frame(centerPane, width=320)
    centerPane.add(rightPane, weight=0)

    # Lexemes
    ttk.Label(rightPane, text="Lexemes").pack(anchor="w", padx=6, pady=(0, 4))
    lexemePane = ttk.Frame(rightPane)
    lexemePane.pack(fill="both", expand=True, padx=6, pady=(0, 6))
    
    
    lexemeTable = ttk.Treeview(lexemePane, columns=("lexeme", "classification"), show="headings", height=10)
    lexemeTable.heading("lexeme", text="Lexeme")
    lexemeTable.heading("classification", text="Classification")
    lexemeTable.column("lexeme", width=140, anchor="w")
    lexemeTable.column("classification", width=140, anchor="w")
    lexemeTable.pack(fill="both", expand=True)

    # Symbol Table
    ttk.Label(rightPane, text="Symbol Table").pack(anchor="w", padx=6, pady=(6, 4))
    symPane = ttk.Frame(rightPane)
    symPane.pack(fill="both", expand=True, padx=6, pady=(0, 6))

    symbolTable = ttk.Treeview(symPane, columns=("identifier", "value"), show="headings", height=8)
    symbolTable.heading("identifier", text="Identifier")
    symbolTable.heading("value", text="Value")
    symbolTable.column("identifier", width=120, anchor="w")
    symbolTable.column("value", width=180, anchor="w")
    symbolTable.pack(fill="both", expand=True)

    # Console
    consolePane = ttk.Frame(root)
    consolePane.pack(side="bottom", fill="both", padx=6, pady=6)

    ttk.Button(consolePane, text="RUN", command=execute_code).pack(side="top", fill="x", padx=8, pady=(0, 6))

    ttk.Label(consolePane, text="Console").pack(anchor="w", padx=6, pady=(0, 4))
    console = ScrolledText(consolePane, height=8, wrap="word", state="normal")
    console.pack(fill="both", expand=True, padx=6, pady=(0, 6))

    placeholders(code)
   
    root.mainloop()

tokenized_tokens = tokenized(sampleCode)
for token in tokenized_tokens: 
    sampleToks.append(classify_token(token[0]))

create_gui(sampleCode)