import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Placeholders
sampleCode = '''HAI
I HAS A var ITZ 12
VISIBLE "noot noot" var
KTHXBYE
'''

sampleToks = [
    ("HAI", "Code Delimiter"),
    ("I HAS A", "Variable Declaration"),
    ("var", "Variable Identifier"),
    ("ITZ", "Variable Assignment"),
    ("12", "Literal"),
    ("VISIBLE", "Output Keyword"),
    ("\"", "String Delimiter"),
    ("noot noot", "Literal"),
    ("\"", "String Delimiter"),
    ("var", "Variable Identifier"),
    ("KTHXBYE", "Code Delimiter"),
]

sampleSyms = [
    ("var", "12"),
    ("IT", "noot noot 12"),
]

consoleOut = "noot noot 12\n"

# For testing
def placeholders():
    textEditor.delete("1.0", tk.END)
    textEditor.insert(tk.END, sampleCode)

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
    # codeText = textEditor.get("1.0", tk.END).strip()
    
    placeholders()

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

def create_gui():
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

    placeholders()
    root.mainloop()

create_gui()