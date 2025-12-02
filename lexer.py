import re

# https://www.geeksforgeeks.org/python/python-re-compile/
# pattern matching
identifier_reg = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
numbr_reg = re.compile(r"-?\d+")
numbar_reg = re.compile(r"^-?\d+\.\d+$")
string_reg = re.compile(r'^".*"$')
comment_reg = re.compile(r'^>.*<$')


# accepts an array, returns the array with combined strings, and multiple-word tokens
def tokenized(array):

    # keywords that has OF attached to it
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
        make_BTW_comments(line)
    return array


def make_strings(line):
    has_quotes = 0
    start_index = -1; 
    end_index = -1
    i = 0
    for word in line: 
        if(word == '"' and start_index == -1): 
            has_quotes = 1
            start_index = i 
        elif(word == '"' and start_index != -1):
            end_index = i + 1 
        i+=1
 
    if(has_quotes == 1): 
        line[start_index:end_index] = [' '.join(line[start_index:end_index])]
        line.insert(start_index, '"')
        line.insert(start_index+2, '"')

def make_BTW_comments(line):
    isBTW = 0
    start_index = -1; 
    end_index = -1
    i = 0
    for word in line: 
        if(word == "BTW" and start_index == -1): 
            isBTW = 1
            start_index = i + 1
        elif(word == '\n' and start_index != -1):
            end_index = i
        i+=1
 
    if(isBTW == 1): 
        line[start_index:end_index] = [' '.join(line[start_index:end_index])]
        line[start_index] = ">" + line[start_index]
        # print(line[start_index])
        line[start_index] = line[start_index] + "<"
        

# accepts a token, returns a tuple of token and its classfication
def classify_token(tok):
    if tok == "\"":
        return (tok, "string_delimiter")
    elif tok == 'WIN' or tok == "FAIL":
        return (tok, "troof_literal")
    elif tok in ["NOOB", "NUMBR", "NUMBAR", "YARN", "TROOF"]:
        return (tok, "type_literal")
    # string literals (between "") ----------
    elif string_reg.match(tok):
        return (tok[1:-1], "string_literal")
    elif comment_reg.match(tok):
        return (tok[1:-1], "comment_literal")
    # exact keywords ------------------------
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
    elif tok == 'NOT':
        return (tok, "not_keyword")
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
        return (tok, "typecast_prefix")
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
    elif tok == 'GTFO':
        return (tok, "break_keyword")
    elif tok == "FOUND YR":
        return (tok, "return_keyword")
    elif tok == "BTW":
        return (tok, "singleline_comment_delimiter")
    elif tok == "OBTW":
        return (tok, "multiline_comment_delimiter")
    # numbar and numbr literals ---------
    elif numbar_reg.fullmatch(tok):
        return (tok, "numbar_literal")
    elif numbr_reg.fullmatch(tok):
        return (tok, "numbr_literal")
    # signs -----------------------------
    elif tok == "+":
        return (tok, "print_concatenation_keyword")
    elif tok == '!':
        return (tok, "no_newline_suffix")
    elif tok == '\n':
        return (tok, "linebreak")
    elif identifier_reg.match(tok):
        return (tok, "variable_identifier")
    
    #default if doesn't enter anything --
    return (tok, "UNKNOWN")


def code_to_tuples(codeText):
    final = []

    # Split code into lines, keeping newlines
    lines = codeText.splitlines(True)

    array = []
    for line in lines: 
        line = re.sub(r'\t', r'', line)
        array.append(line.split(" "))



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
    
    # Pass tokenized lines to your existing classification function
    tokenized_toks = tokenized(final)  # assuming tokenized() exists



    result = []
    for line in tokenized_toks:
        for word in line:
            result.append(classify_token(word))  # assuming classify_token() exists

 
    return result