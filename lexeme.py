import re

keywords = ["HAI", "KTHXBYE", "WAZZUP",
            "BUHBYE", "BTW", "OBTW",
            "TLDR", "I HAS A", "ITZ", "R",
            "SUM OF", "DIFF OF", "PRODUKT OF",
            "QUOSHUNT OF", "MOD OF", "BIGGR OF",
            "SMALLR OF", "BOTH OF", "EITHER OF",
            "WON OF", "NOT", "ANY OF", "ALL OF",
            "BOTH SAEM", "DIFFRINT", "SMOOSH", 
            "MAEK", "A", "IS NOW A", "VISIBLE", 
            "GIMME", "O RLY?", "MEBBE", "NO WAI",
            "IOC", "WTF?", "OMG", "OMGWTF", 
            "IM IN YR", "UPPIN", "NERFIN",
            "YR", "TIL", "WILE", "IM OUTTA YR",
            "HOW IZ I", "IF U SAY SO", "GTFO", "FOUND YR", "I IZ", "MKAY"]

def isTroof(tok):
    if tok == "WIN" or tok == "FAIL":
        return True:
    else:
        return False:

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

tokens = []
with open("file.lol", "r") as f:
	for line in f:
        temp = []
		codeTok = line.strip().split(" ")
		for x in codeTok:
            temp.append(x)
        tokens.append(temp)
