import re

keywords = ["HAI", "KTHXBYE", "WAZZUP",
            "BUHBYE", "BTW", "OBTW",
            "TLDR", "I HAS A", "ITZ", "R",
            "SUM OF", "DIFF OF", "PRODUKT OF",
            "QUOSHUNT OF", "MOD OF", "BIGGR OF",
            "SMALLR OF", "BOTH OF", "EITHER OF",
            "WON OF", "NOT", "ANY OF", "ALL OF",
            "BOTH SAEM", "DIFFRINT", "SMOOSH", 
            "MAEK", "IS NOW A", "VISIBLE", 
            "GIMME", "O RLY?", "MEBBE", "NO WAI",
            "OIC", "WTF?", "OMG", "OMGWTF", 
            "IM IN YR", "UPPIN", "NERFIN", "AN YR",
            "YR", "TIL", "WILE", "IM OUTTA YR",
            "HOW IZ I", "IF U SAY SO", "GTFO", "FOUND YR", "I IZ", "MKAY"]

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

def tokenized():
    tokens = []

    # Read file into list[list[str]]
    with open("file.lol", "r") as f:
        for line in f:
            tokens.append(line.strip().split(" "))

    keys = [
        "SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD", "BIGGR",
        "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL"
    ]

    for tok in tokens:
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

    return tokens

sample = tokenized()
print(sample)