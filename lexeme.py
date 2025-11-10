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