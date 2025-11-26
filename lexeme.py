import os
import re

# def isTroof(tok):
#     if tok == "WIN" or tok == "FAIL":
#         return True
#     else:
#         return False

# def isNumbr(tok):
#     regex = r"-?\d+"
#     return re.search(regex, tok)

# def isNumbar(tok):
#     regex = r"-?\d+$"
#     return re.search(regex, tok)

# def isYarn(tok):
#     regex = r"^-?\d+\.\d+$"
#     return re.search(regex, tok)

# def isType(tok):
#     types = ["NOOB", "NUMBR", "NUMBAR", "YARN", "TROOF"]
#     if tok in types:
#         return True
#     else:
#         return False

# def isIdentifier(tok):
#     regex = r"^[A-Za-z][A-Za-z0-9_]*"
#     return re.search(regex, tok)

# def isCodeDelimiter(tok): 
#     delimiter = ['HAI', "KTHXBYE"]
#     if tok in delimiter: 
#         return (tok, "Code Delimiter")

# def isVariableDelimiter(tok): 
#     delimiter = ['WAZZUP', 'BUHBYE']
#     if tok in delimiter: 
#         return (tok, "Variable Delimiter")

# def isCommentDelimiter(tok): 
#     delimiter = ['BTW', 'OBTW', 'TLDR']
#     if tok in delimiter: 
#         return (tok, "Comment Delimiter")
    
# def isStatementDelimiter(tok): 
#     delimiter = ['O RLY?', 'OIC', 'WTF?']
#     if tok in delimiter: 
#         return (tok, "Statement Delimiter")
    
# def isLoopDelimiter(tok): 
#     delimiter = ['IM IN YR', 'IM OUTTA YR']
#     if tok in delimiter: 
#         return (tok, "Loop Delimiter")

# def isFunctionDelimiter(tok): 
#     delimiter = ['HOW IZ I', 'IF U SAY SO']
#     if tok in delimiter: 
#         return (tok, "Function Delimiter")

# def isComparisonOperator(tok): 
#     operator = ['BOTH SAEM', 'DIFFRINT']
#     if tok in operator: 
#         return(tok, "Comparison Operator")
    
# def isArithmeticOperator(tok): 
#     operator = ['SUM OF', 'DIFF OF', 'PRODUKT OF', 'QUOSHUNT OF', 'MOD OF', 'BIGGR OF', 'SMALLR OF', 'UPPN', 'NERFIN']
#     if tok in operator: 
#         return(tok, "Arithmetic Operator")
    
# def isBooleanOperator(tok): 
#     operator = ['BOTH OF', 'EITHER OF', 'WON OF', 'NOT', 'ANY OF', 'ALL OF', 'SMOOSH']
#     if tok in operator: 
#         return(tok, "Boolean Operator")

def tokenized(array):

    # code that has OF attached to it
    of_keys = [
        "SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD", "BIGGR",
        "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL"
    ]

    for tok in array:
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
                if tok[i] in of_keys and tok[i+1] == "OF":
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

    for line in array: 
        make_strings(line)
    return array

def make_strings(line):
    has_quotes = 0
    start_index = -1; 
    end_index = -1
    i = 0
    for word in line: 
        if(word == '"' and start_index == -1): 
            has_quotes = 1
            start_index = i + 1
        elif(word == '"' and start_index != -1):
            end_index = i 
        i+=1
 
    if(has_quotes == 1): 
        line[start_index:end_index] = [' '.join(line[start_index:end_index])]
   

def classify_token(tok): 
    if tok == '\"':
        return (tok, "string_delimiter")
    elif tok == 'some string':
        # Placeholder for recognizing any string literal (excluding delimiters)
        return (tok, "string_literal")
    elif tok == 'WIN':
        return (tok, "troof_literal")
    elif tok == 'FAIL':
        return (tok, "troof_literal")
    elif tok == 'NOOB':
        return (tok, "type_literal")
    elif tok == 'HAI':
        return (tok, "start_code_delimiter")
    elif tok == 'KTHXBYE':
        return (tok, "end_code_delimiter")
    elif tok == 'WAZZUP':
        return (tok, "var_declaration_start")
    elif tok == 'BUHBYE':
        return (tok, "var_declaration_end")
    elif tok == 'I HAS A':
        return (tok, "variable_declaration")
    elif tok == 'ITZ':
        return (tok, "variable_assignment")
    elif tok == 'R':
        return (tok, "update_var_value")
    elif tok == 'AN':
        return (tok, "operator_delimiter")
    elif tok == 'SUM OF':
        return (tok, "add_keyword")
    elif tok == 'DIFF OF':
        return (tok, "subtract_keyword")
    elif tok == 'PRODUKT OF':
        return (tok, "multiply_keyword")
    elif tok == 'QUOSHUNT OF':
        return (tok, "divide_keyword")
    elif tok == 'MOD OF':
        return (tok, "modulo_keyword")
    elif tok == 'BIGGR OF':
        return (tok, "max_keyword")
    elif tok == 'SMALLR OF':
        return (tok, "min_keyword")
    elif tok == 'BOTH OF':
        return (tok, "and_keyword")
    elif tok == 'EITHER OF':
        return (tok, "or_keyword")
    elif tok == 'WON OF':
        return (tok, "xor_keyword")
    elif tok == 'ANY OF':
        return (tok, "multi_or_keyword")
    elif tok == 'ALL OF':
        return (tok, "multi_and_keyword")
    elif tok == 'BOTH SAEM':
        return (tok, "equal_keyword")
    elif tok == 'DIFFRINT':
        return (tok, "not_equal_keyword")
    elif tok == 'SMOOSH':
        return (tok, "concatenation_keyword")
    elif tok == 'MAEK':
        return (tok, "typecast_keyword")
    elif tok == 'A':
        return (tok, "typecast_prefix_keyword")
    elif tok == 'IS NOW A':
        return (tok, "type_convert_keyword")
    elif tok == 'VISIBLE':
        return (tok, "print_keyword")
    elif tok == 'GIMMEH':
        return (tok, "input_keyword")
    elif tok == 'O RLY?':
        return (tok, "if_keyword")
    elif tok == 'YA RLY':
        return (tok, "if_true_keyword")
    elif tok == 'MEBBE':
        return (tok, "else_if_keyword")
    elif tok == 'NO WAI':
        return (tok, "else_keyword")
    elif tok == 'OIC':
        return (tok, "end_of_if_block_keyword")
    elif tok == 'WTF?':
        return (tok, "switch_keyword")
    elif tok == 'OMG':
        return (tok, "switch_case_keyword")
    elif tok == 'OMGWTF':
        return (tok, "switch_default_keyword")
    elif tok == 'IM IN YR':
        return (tok, "initialize_loop_keyword")
    elif tok == 'UPPIN':
        return (tok, "increment_keyword")
    elif tok == 'NERFIN':
        return (tok, "decrement_keyword")
    elif tok == 'YR':
        return (tok, "separator_keyword")
    elif tok == 'WILE':
        return (tok, "while_keyword")
    elif tok == 'TIL':
        return (tok, "until_keyword")
    elif tok == 'IM OUTTA YR':
        return (tok, "break_loop_keyword")
    elif tok == 'HOW IZ I':
        return (tok, "define_function_keyword")
    elif tok == 'IF U SAY SO':
        return (tok, "function_end_keyword")
    elif tok == 'I IZ':
        return (tok, "function_call_keyword")
    elif tok == 'MKAY':
        return (tok, "end_of_assignment_keyword")
    elif tok == 'varname':
        # make function like isNumbr() or isNumbar() using regex probably
        # Placeholder for recognizing any variable identifier
        return (tok, "variable_identifier")
    elif tok == '17.0':
        # Placeholder for recognizing any number literal
        return (tok, "numbar_literal")
    elif tok == '\n':
        return (tok, "linebreak")
    elif tok == '+':
        return (tok, "print_concatenation_keyword")
    elif tok == '!':
        return (tok, "no_newline_suffix")
    else:
        return (tok, "UNKNOWN")

array = []
file = open('file.lol', "r")
for line in file: 
    line = re.sub(r'\t', r'', line)
    array.append(line.split(" "))
file.close()

print(array)
print()

final = []
pattern = r'(")'
pattern2 = r'(\n)'
for line in array: 
    line_array = []
    for word in line: 
        if re.search('"', word): 
            token = re.split(pattern, word)
            line_array.extend(token)
        elif re.search("^.+\n$", word): 
            token = re.split(pattern2, word)
            line_array.extend(token)
        else: 
            line_array.append(word)
    line_array = list(filter(None, line_array))
    final.append(line_array)


print(final)


tokenized_toks = tokenized(final)



result = []

for line in tokenized_toks: 
    for word in line: 
        result.append(classify_token(word))

for i in result: 
    print(i)


