import sys
import tkinter as tk
from tkinter import simpledialog

arith_toks = ["add_keyword", 
                "subtract_keyword", 
                "multiply_keyword", 
                "divide_keyword", 
                "modulo_keyword", 
                "max_keyword", 
                "min_keyword"]

bool_toks =  ["and_keyword", 
                "or_keyword", 
                "xor_keyword", 
                "multi_or_keyword", 
                "multi_and_keyword"]

comp_toks =  ["equal_keyword", 
                "not_equal_keyword"]

flow_con_toks = ["initialize_loop_keyword",
                       "if_keyword",
                       "switch_keyword"]

expr_toks = ["add_keyword", 
                    "subtract_keyword", 
                    "multiply_keyword", 
                    "divide_keyword", 
                    "modulo_keyword",
                    "typecast_keyword",
                    "variable_identifier",
                    "max_keyword", 
                    "min_keyword", 
                    "and_keyword", 
                    "or_keyword", 
                    "xor_keyword", 
                    "not_keyword", 
                    "multi_or_keyword", 
                    "multi_and_keyword",
                    "equal_keyword", 
                    "not_equal_keyword",
                    "concatenation_keyword"
                    ]

# Global Containers
tokens = []             # should be set to list of (token_value, token_type) tuples
current_index = 0
current_token = None    # pointer
current_line = 1        # lolcode line tracker
symbol_table = {}       # name -> {"value": ..., "type": ...}

"""
SYNTAX AND TOKEN HELPERS
"""

# Checks next token
def peek(offset=0):
    global tokens, current_index
    i = current_index + offset
    if i < 0 or i >= len(tokens):
        return None
    return tokens[i]

# Moves the pointer to the next token
def next_tok():
    global current_index, current_token, tokens, current_line
    current_index += 1
    if current_index < len(tokens):
        current_token = tokens[current_index]
        if current_token is not None and current_token[1] == "linebreak": # for line tracing
            current_line += 1
    else:
        current_token = None

# Skips comments and whitespaces
def skip_empty_lines():
    global current_token
    while current_token is not None and (current_token[1] == "empty_line" or current_token[1] == "linebreak"):
        next_tok()

def if_linebreak():
    global current_token
    if current_token is not None and current_token[1] == "linebreak":
        next_tok()
        skip_empty_lines()

# Prints syntax errors
def error(msg, line=None):
    if line is None:
        line = current_line
    print(f"[SyntaxError] {msg} (line {line})")
    sys.exit(1) # ends program

# Return True if the next token is R
def peek_assignment():
    global current_index, tokens

    if current_index + 1 >= len(tokens):
        return False

    next_tok = tokens[current_index + 1]

    if next_tok[1] == "update_variable_keyword":  # R
        return True
    
    return False

# Return True if the next token is 
def peek_typecast():
    global current_index, tokens

    if current_index + 1 >= len(tokens):
        return False

    next_tok = tokens[current_index + 1]

    if next_tok[1] == "type_convert_keyword": # IS NOW A
        return True

    return False

"""
SEMANTICS HELPERS
"""

def update_symbol_table():
    global symbol_table
    # WIP
    return

# Parse inputs to int or float automatically
def auto_cast(value):
    if isinstance(value, (int, float)):
        return value

    if isinstance(value, str):
        # Try integer
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)

        # Try float
        try:
            return float(value)
        except ValueError:
            return value  # treat as YARN

    return value

# Upload variable-value pairs to the symbol table
def store_variable(name, value):
    global symbol_table
    if value is None:
        # uninitialized -> NOOB
        symbol_table[name] = {"value": "NOOB", "type": "NOOB"}
    else:
        # set type based on python type
        if isinstance(value, bool):
            t = "TROOF"
        elif isinstance(value, int):
            t = "NUMBR"
        elif isinstance(value, float):
            t = "NUMBAR"
        elif isinstance(value, str):
            t = "YARN"
        else:
            t = "UNKNOWN"
        symbol_table[name] = {"value": value, "type": t}

""" PROGRAM SYNTAX """
def program():
    global tokens, current_index, current_token, current_line
    current_token = tokens[0]
    nodes = []
    update_symbol_table()
    skip_empty_lines() # Skips comments and whitespaces

    # Expect start code delimiter HAI
    if current_token is None or current_token[1] != "start_code_delimiter":
        print(current_token)
        error("Start code delimiter (HAI) not found", current_line)

    nodes.append(("START", current_token))
    next_tok()
    if_linebreak()

    # variable declaration section (WAZZUP)
    if current_token is not None and current_token[1] == "var_declaration_start":  # WAZZUP
        next_tok()  # pass WAZZUP
        if_linebreak()

        varDeclarationList = var_declaration_list()
        nodes.append(("VAR_DEC_LIST", varDeclarationList))

        skip_empty_lines()

        if current_token is not None and current_token[1] == "var_declaration_end": # BUHBYE
            next_tok()
            if_linebreak()
        else:
            error("End variable declaration delimiter (BUHBYE) not found", current_line)

    # Optional function definitions
    if current_token is not None and current_token[1] == "define_function_keyword":
        while current_token is not None and current_token[1] == "define_function_keyword":
            nodes.append(function_def())
            if_linebreak()  # skip linebreak after each function

    # STATEMENTS_LIST
    statementList = statement_list()
    nodes.append(("STAT_LIST", statementList))

    if current_token is not None and current_token[1] == "end_code_delimiter": # KTHXBYE
        nodes.append(("END", current_token))
        next_tok()
    else:
        print(current_token)
        error("End code delimiter (KTHXBYE) not found", current_line)

    return nodes

"""
WAZZUP (Variable Declaration Section)
"""
def var_declaration():
    global current_token

    if current_token is None or current_token[1] != "variable_declaration":
        error("Expected variable declaration start 'I HAS A'", current_line)
    
    # consume 'I HAS A'
    next_tok()

    # Expect identifier
    if current_token is None or current_token[1] != "variable_identifier":
        error("Expected variable identifier after 'I HAS A'", current_line)
    name = current_token[0]
    next_tok()

    # Default: no assignment -> NOOB
    value = None

    # Optional assignment: ITZ <expr>
    if current_token is not None and current_token[1] == "variable_assignment":
        # consume 'ITZ'
        next_tok()

        if current_token is None:
            error("Expected a literal or expression after 'ITZ'", current_line)

        # Parse the expression
        value, _ = parse_expression()

    # Semantic: store variable
    store_variable(name, value)

    if value is None:
        return ('VARIABLE', name, 'NOOB')
    else:
        return ('VARIABLE', name, value)

def var_declaration_list():
    global current_token, current_line
    nodes = []

    while current_token is not None and current_token[1] != "var_declaration_end":
        skip_empty_lines()

        if current_token is not None and current_token[1] == "var_declaration_end":
            break

        # Expect a variable declaration
        if current_token is None or current_token[1] != "variable_declaration":
            print(current_token)
            error("Expected variable declaration start 'I HAS A'", current_line)

        node = var_declaration()
        update_symbol_table()  # semantic update
        if node is not None:
            nodes.append(node)
        if_linebreak()

    return nodes

""" STATEMENT PARSING """
# Returns True if the current token can begin a statement
def is_statement_start(tok):
    if tok is None:
        return False

    ttype = tok[1]

    # Prints
    if ttype == "print_keyword":
        return True

    # Assignment starting tokens
    if ttype == "variable_identifier":
        return True

    # Input
    if ttype == "input_keyword":
        return True

    # Flow control keywords
    if ttype in flow_con_toks:
        return True

    # Expressions
    if ttype in expr_toks:
        return True

    return False

# Returns statement nodes
def statement_list():
    global current_token

    nodes = []

    while True:
        # Skip empty lines
        skip_empty_lines()
        if current_token is None:
            break

        # Stop if end of program
        if current_token[1] == "end_code_delimiter":
            break

        # Stop if BUHBYE
        if current_token[1] == "var_declaration_end":
            break

        # Not a statement start → end of statement_list
        if not is_statement_start(current_token):
            break

        # Parse one statement
        node = statement()
        nodes.append(node)

        if_linebreak()

    return nodes

# Assigns statements to specific parsers
def statement():
    global current_token

    if current_token is None:
        error("Unexpected EOF while parsing statement")

    ttype = current_token[1]

    # 1. variable declaration
    if ttype == "variable_declaration":
        return var_decl()

    # 2. assignment and typecast
    if ttype == "variable_identifier":
        if peek_typecast():
            return parse_full_typecast()
        elif peek_assignment():
            return assignment()

    # 3. print statement
    if ttype == "print_keyword":
        return print_stmt()

    # 4. input statement
    if ttype == "input_keyword":
        return input_stmt()

    # 5. switch statement
    if ttype == "switch_keyword":
        return switch_stmt()

    # 6. loop statement
    if ttype == "initialize_loop_keyword":
        return loop_stmt()

    # 7. function def
    if ttype == "define_function_keyword":
        return function_def()

    # 8. return statement
    if ttype == "return_keyword":
        return return_stmt()

    # 9. expressions anad if statements
    if ttype in expr_toks:
        return expr_stmt()

    # No valid statement start
    error("Invalid statement start: " + str(current_token))

# variable declaration parser
def var_decl():
    global current_token

    if current_token is None or current_token[1] != "variable_declaration":
        error("Expected variable declaration start 'I HAS A'", current_line)

    # consume 'I HAS A'
    next_tok()

    # expect identifier
    if current_token is None or current_token[1] != "variable_identifier":
        error("Expected variable identifier after 'I HAS A'", current_line)
    name = current_token[0]
    next_tok()

    value = None
    declared_type = None

    # optional ITZ
    if current_token is not None and current_token[1] == "variable_assignment":
        next_tok()  # consume ITZ

        if current_token is None:
            error("Expected token after 'ITZ'", current_line)

        # ITZ <expr>
        if current_token[1] in expr_toks or current_token[1] in arith_toks + bool_toks + comp_toks:
            value, declared_type = parse_expression()
            store_variable(name, value)
            return ('VARIABLE', name, value)

        # ITZ A <type>
        elif current_token[1] == "type_keyword":
            declared_type = current_token[0]
            next_tok()
            store_variable(name, None)
            symbol_table[name]["type"] = declared_type
            return ('VARIABLE', name, 'NOOB')

        # ITZ LIEK A <identifier>
        elif current_token[1] == "like_type_keyword":
            next_tok()  # consume LIEK
            if current_token is None or current_token[1] != "type_reference_keyword":
                error("Expected 'A <identifier>' after 'LIEK'", current_line)
            ref_name = current_token[0]
            next_tok()
            if ref_name not in symbol_table:
                error(f"Referenced variable '{ref_name}' does not exist", current_line)
            declared_type = symbol_table[ref_name]["type"]
            store_variable(name, None)
            symbol_table[name]["type"] = declared_type
            return ('VARIABLE', name, 'NOOB')

        else:
            error("Invalid token after ITZ in variable declaration", current_line)
    else:
        # no ITZ → default NOOB
        store_variable(name, None)
        return ('VARIABLE', name, 'NOOB')

# Variable value assignment parser
def assignment():
    global current_token

    # Expect identifier
    if current_token is None or current_token[1] != "variable_identifier":
        error("Expected variable identifier at start of assignment", current_line)
    name = current_token[0]
    next_tok()

    # Expect assignment operator 'R'
    if current_token is None or current_token[1] != "update_variable_keyword":
        error("Expected 'R' in assignment", current_line)
    next_tok()

    # Expect expression
    if current_token is None:
        error("Expected expression after 'R'", current_line)

    # parse_expression() returns evaluated value and type
    value,_ = parse_expression()

    # Semantic check: variable must exist
    if name not in symbol_table:
        error(f"Variable '{name}' not declared", current_line)

    # Update variable value and type in symbol table
    store_variable(name, value)

    # Return assignment node
    return ('ASSIGNMENT', name, value)

# Print statement parser
def print_stmt():
    global current_token

    if current_token is None or current_token[1] != "print_keyword":
        error("Expected 'VISIBLE'", current_line)
    next_tok()  # consume VISIBLE

    # First expression
    if current_token is None:
        error("Expected expression after 'VISIBLE'", current_line)
    value, _ = parse_expression()
    if value is None:
        value = ""  # empty if AN or nothing found

    # Concatenation loop (AN or other concat tokens)
    concat_tokens = {
        "print_concatenation_keyword",
        "and_keyword",
        "concat",
        "CONCAT",
        "plus",
        "+",
    }

    if current_token is not None and current_token[1] in expr_toks:
        error(f"Syntax Error: missing + for string concatenation", current_line)

    while current_token is not None and current_token[1] in concat_tokens:
        next_tok()  # consume AN / concat token
        if current_token is None:
            break
        next_value, _ = parse_expression()
        if next_value is None:
            break  # stop if next token is AN or invalid
        value = str(value) + str(next_value)

    # Optional '!' for no newline
    no_newline = False
    if current_token is not None and current_token[1] == "no_newline_suffix":
        no_newline = True
        next_tok()

    if no_newline:
        print(value, end="")
    else:
        print(value)

    return ("PRINT", value)

# Input statement parser
def input_stmt():
    global current_token

    # Expect GIMMEH
    if current_token is None or current_token[1] != "input_keyword":
        error("Expected 'GIMMEH' for input statement", current_line)
    next_tok()

    # Expect identifier
    if current_token is None or current_token[1] != "variable_identifier":
        error("Expected identifier after 'GIMMEH'", current_line)

    varname = current_token[0]
    next_tok()

    # Request input
    root = tk.Tk()
    root.withdraw()  # hide main root window

    user_value = simpledialog.askstring("LOLcode Input", f"GIMMEH {varname}:")
    root.destroy()

    # Auto-cast (NUMBR, NUMBAR, or fallback to YARN)
    user_value = auto_cast(user_value)

    # Store into symbol table
    store_variable(varname, user_value)

    return ("INPUT", varname, user_value)

# Switch statement parser
def switch_stmt(switch_value):
    global current_token

    # Expect WTF?
    if current_token is None or current_token[1] != "switch_keyword":
        error("Expected 'WTF?' after expression", current_line)
    next_tok()
    skip_empty_lines()

    chosen_block = []
    found_branch = False
    gtfo_triggered = False

    # Handle OMG/switch cases
    while current_token is not None and current_token[1] == "switch_case_keyword":
        next_tok()  # consume OMG
        skip_empty_lines()

        # Parse case literal
        if current_token is None or current_token[1] not in (
            "numbr_literal", "numbar_literal", "string_literal", "troof_literal"
        ):
            error("Expected literal after OMG", current_line)

        case_val, _ = parse_literal()
        skip_empty_lines()

        if not found_branch and not gtfo_triggered and case_val == switch_value:
            # Case matches
            block = []
            while current_token is not None and current_token[1] not in (
                "switch_case_keyword", "switch_default_keyword", "end_of_if_block_keyword"
            ):
                if current_token[1] == "break_keyword":
                    gtfo_triggered = True
                    next_tok()  # consume GTFO
                    skip_empty_lines()
                    break
                block.append(statement())
                skip_empty_lines()

            chosen_block = block
            found_branch = True
        else:
            while current_token is not None and current_token[1] not in (
                "switch_case_keyword", "switch_default_keyword", "end_of_if_block_keyword"
            ):
                next_tok()
                skip_empty_lines()

        # If GTFO triggered, break outer loop
        if gtfo_triggered:
            while current_token is not None and current_token[1] != "end_of_if_block_keyword":
                next_tok()
                skip_empty_lines()
            break

    if current_token is not None and current_token[1] == "switch_default_keyword" and not gtfo_triggered:
        next_tok()  # consume OMGWTF
        skip_empty_lines()

        if not found_branch:
            block = []
            while current_token is not None and current_token[1] != "end_of_if_block_keyword":
                if current_token[1] == "break_keyword":
                    gtfo_triggered = True
                    next_tok()
                    skip_empty_lines()
                    break
                block.append(statement())
                skip_empty_lines()
            chosen_block = block

        else:
            # Skip default block
            while current_token is not None and current_token[1] != "end_of_if_block_keyword":
                if current_token[1] == "break_keyword":
                    gtfo_triggered = True
                    next_tok()
                    skip_empty_lines()
                    break
                next_tok()
                skip_empty_lines()

    # Expect OIC
    if current_token is None or current_token[1] != "end_of_if_block_keyword":
        print(current_token)
        error("Expected 'OIC' to close WTF? block", current_line)

    next_tok()
    skip_empty_lines()

    return chosen_block

# Switch helper
def statement_list_until_switch_branch():
    global current_token
    stmts = []

    while current_token is not None:
        t = current_token[1]

        # Stop on next case, default, end, or GTFO
        if t in ("switch_case_keyword", "switch_default_keyword", "end_of_if_block_keyword", "break_keyword"):
            break

        if not is_statement_start(current_token):
            break

        stmts.append(statement())

        # skip blank lines
        while current_token is not None and current_token[1] in ("linebreak", "empty_line"):
            next_tok()
            skip_empty_lines()

    return stmts

# If statement parser
def if_stmt(cond_value):
    global current_token

    # Expect 'O RLY?' keyword
    if current_token is None or current_token[1] != "if_keyword":
        error("Expected 'O RLY?' after expression", current_line)
    next_tok()
    skip_empty_lines()

    # Expect 'YA RLY'
    if current_token is None or current_token[1] not in ("if_then_keyword", "if_true_keyword"):
        error("Expected 'YA RLY' after 'O RLY?'", current_line)
    next_tok()
    skip_empty_lines()

    chosen_block = []
    found_branch = False

    if cond_value == "WIN":
        # Parse statements until next MEBBE, NO WAI, or OIC
        chosen_block = statement_list_until_if_branch()
        found_branch = True
    else:
        # Skip tokens until next MEBBE / NO WAI / OIC
        while current_token is not None and current_token[1] not in ("else_if_keyword", "else_keyword", "end_of_if_block_keyword"):
            next_tok()
            skip_empty_lines()

    # Handle optional MEBBE
    while current_token is not None and current_token[1] in ("else_if_keyword", "else_if_keyword"):
        next_tok()  # consume MEBBE
        skip_empty_lines()

        m_val, _ = parse_expression()  # evaluate MEBBE condition
        skip_empty_lines()

        if not found_branch and m_val == "WIN":
            # parse statements for first true MEBBE
            chosen_block = statement_list_until_if_branch()
            found_branch = True
        else:
            # skip statements until next branch or OIC
            while current_token is not None and current_token[1] not in ("else_if_keyword", "else_keyword", "end_of_if_block_keyword"):
                next_tok()
                skip_empty_lines()

    # Handle optional NO WAI
    if current_token is not None and current_token[1] in ("else_keyword", "no_wai_keyword"):
        next_tok()  # consume NO WAI
        skip_empty_lines()
        if not found_branch:
            chosen_block = statement_list_until_if_branch()
            found_branch = True
        else:
            # skip NO WAI statements
            while current_token is not None and current_token[1] != "end_of_if_block_keyword":
                next_tok()
                skip_empty_lines()

    # Expect OIC
    if current_token is None or current_token[1] != "end_of_if_block_keyword":
        error("Expected 'OIC' to close IF statement", current_line)
    next_tok()
    skip_empty_lines()

    return chosen_block

# If Helper
def statement_list_until_if_branch():
    global current_token
    stmts = []

    while current_token is not None:
        ttype = current_token[1]

        # Stop at IF branch boundaries
        if ttype in ("else_if_keyword", "else_if_keyword", "else_keyword", "no_wai_keyword", "end_of_if_block_keyword"):
            break

        # Stop if token cannot start a statement
        if not is_statement_start(current_token):
            break

        stmts.append(statement())

        # Skip linebreaks / empty lines between statements
        while current_token is not None and current_token[1] in ("linebreak", "empty_line"):
            next_tok()
    return stmts

# Expression dispatcher
def expr_stmt():
    global current_token
    # Parse the expression
    cond_value,_ = parse_expression()

    if cond_value is None:
        error("Expected expression for expression-statement", current_line)

    # Skip empty lines before potential IF
    while current_token is not None and current_token[1] in ("linebreak", "empty_line"):
        next_tok()

    # If O RLY? follows, delegate to if_stmt
    if current_token is not None and current_token[1] == "if_keyword":
        # if_stmt now returns the chosen branch's statements
        return if_stmt(cond_value)
    
    if current_token is not None and current_token[1] == "switch_keyword":
        return switch_stmt(cond_value)

    # Otherwise wrap as an expression statement
    return [("EXPR_STMT", cond_value)]

def parse_expression(): 
    global current_token

    if current_token is None:
        error("Unexpected EOF in expression", current_line)

    ttype = current_token[1]

    # AN token is just a separator
    if ttype == "and_keyword":
        return None, None

    # Literals
    if ttype in ["string_delimiter", "numbr_literal", "numbar_literal", "troof_literal", "noob_literal"]:
        return parse_literal()

    # Variables
    if ttype == "variable_identifier":
        name = current_token[0]
        if name not in symbol_table:
            error(f"Variable '{name}' not declared", current_line)
        value = symbol_table[name]["value"]
        expr_type = symbol_table[name].get("type", None)
        next_tok()
        return value, expr_type

    # Unary Not
    if ttype == "not_keyword":
        next_tok()
        operand, _ = parse_expression()
        operand = True if operand == "WIN" else False
        value = not operand
        value = "WIN" if value else "FAIL"
        return value, "TROOF"

    # Multi-operand logical operations
    if ttype in ["multi_and_keyword", "multi_or_keyword"]:
        op = ttype
        next_tok()  # consume ALL OF / ANY OF

        results = []
        while True:
            # stop if MKAY is next
            if current_token is None:
                error("Expected MKAY to end multi-operand logical check", current_line)
            if current_token[1] == "end_of_assignment_keyword":  # MKAY
                break

            # parse next operand
            value, _ = parse_expression()
            if value is None:
                error("Expected operand in multi-operand logical check", current_line)

            results.append(True if value == "WIN" else False)

            # skip optional AN separator
            if current_token is not None and current_token[1] == "and_keyword":
                next_tok()

        # consume MKAY
        next_tok()

        # compute result
        if op == "multi_and_keyword":
            result = all(results)
        else:
            result = any(results)

        return "WIN" if result else "FAIL", "TROOF"

    # Typecasting and binary operations
    if ttype in arith_toks + bool_toks + comp_toks + [
        "concatenation_keyword", "type_convert_keyword", "typecast_keyword",
        "and_keyword", "or_keyword", "xor_keyword"
    ]:
        op = ttype
        next_tok()

        # TYPECAST: MAEK A <expr> <type_literal>
        if op == "typecast_keyword":
            if current_token is None or current_token[1] != "typecast_prefix":
                error("Expected 'A' after MAEK", current_line)
            next_tok()
            left, _ = parse_expression()
            if current_token is None or current_token[1] != "type_literal":
                error("Expected type literal after expression in MAEK cast", current_line)
            target_type = current_token[0]
            next_tok()
            try:
                if target_type == "NUMBR": return int(float(left)), "NUMBR"
                if target_type == "NUMBAR": return float(left), "NUMBAR"
                if target_type == "TROOF": return (str(left).upper() in ["WIN", "TRUE", "1"]), "TROOF"
                if target_type == "YARN": return str(left), "YARN"
                if target_type == "NOOB": return None, "NOOB"
            except:
                error(f"Cannot cast '{left}' to {target_type}", current_line)

        # TYPECAST: <type_literal> OF <expr>
        if op == "type_convert_keyword":
            target_type = current_token[0]
            next_tok()
            if current_token is None or current_token[1] != "of_keyword":
                error("Expected 'OF' in full typecast", current_line)
            next_tok()
            left, _ = parse_expression()
            try:
                if target_type == "NUMBR": return int(float(left)), "NUMBR"
                if target_type == "NUMBAR": return float(left), "NUMBAR"
                if target_type == "TROOF": return (str(left).upper() in ["WIN", "TRUE", "1"]), "TROOF"
                if target_type == "YARN": return str(left), "YARN"
                if target_type == "NOOB": return None, "NOOB"
            except:
                error(f"Cannot cast '{left}' to {target_type}", current_line)

        # Binary operations
        left, left_type = parse_expression()
        if left is None:
            return None, None

        # Consume AN if present
        if current_token is not None and current_token[1] == "and_keyword":
            next_tok()
        right, _ = parse_expression()
        if right is None:
            error(f"Missing right-hand operand for {op}", current_line)

        if left == "WIN":
                left = True
        elif left == "FAIL":
            left = False

        if right == "WIN":
            right = True
        elif right == "FAIL":
            right = False

        if op == "add_keyword":
            left = float(left) + float(right)
            left_type = "NUMBR"
        elif op == "subtract_keyword": 
            left = float(left) - float(right)
            left_type = "NUMBR"
        elif op == "multiply_keyword":
            left = float(left) * float(right)
            left_type = "NUMBR"
        elif op == "divide_keyword":
            left = float(left) / float(right)
            left_type = "NUMBAR"
        elif op == "modulo_keyword":
            left = float(left) % float(right)
            left_type = "NUMBR"
        elif op == "max_keyword":
            left = max(float(left), float(right))
            left_type = "NUMBR"
        elif op == "min_keyword":
            left = min(float(left), float(right))
            left_type = "NUMBR"
        elif op == "and_keyword":
            left = left and right
            left = "WIN" if left else "FAIL"
            left_type = "TROOF"
        elif op == "or_keyword":
            left = left or right
            left = "WIN" if left else "FAIL"
            left_type = "TROOF"
        elif op == "xor_keyword":
            left = (left != right)
            left = "WIN" if left else "FAIL"
            left_type = "TROOF"
        elif op == "equal_keyword":
            left = left == right
            left = "WIN" if left else "FAIL"
            left_type = "TROOF"
        elif op == "not_equal_keyword":
            left = left != right
            left = "WIN" if left else "FAIL"
            left_type = "TROOF"

        return left, left_type

    error(f"Unknown expression start: {current_token}")

# Literals Parser
def parse_literal():
    global current_token

    if current_token is None:
        error("Expected literal, found EOF", current_line)

    ttype = current_token[1]
    value = None

    # String literal enclosed in delimiters
    if ttype == "string_delimiter":
        next_tok()  # consume opening "
        if current_token is None or current_token[1] != "string_literal":
            error("Expected string literal after opening quote", current_line)
        value = current_token[0]
        next_tok()  # consume string literal
        if current_token is None or current_token[1] != "string_delimiter":
            error("Expected closing quote for string literal", current_line)
        next_tok()  # consume closing "
        return value, "YARN"

    # Number literals
    elif ttype == "numbr_literal":
        value = int(current_token[0])
        next_tok()
        return value, "NUMBR"
    elif ttype == "numbar_literal":
        value = float(current_token[0])
        next_tok()
        return value, "NUMBAR"

    # Boolean literals
    elif ttype == "troof_literal":
        value = current_token[0]
        next_tok()
        return value, "TROOF"
    
    # NOOB literal
    elif ttype == "noob_literal":
        next_tok()
        return "NOOB", "NOOB"

    else:
        error(f"Unknown literal start: {current_token}", current_line)

def parse_full_typecast():
    global current_token

    # Expect identifier
    if current_token is None or current_token[1] != "variable_identifier":
        error("Expected variable identifier before 'IS NOW A'", current_line)

    varname = current_token[0]

    if varname not in symbol_table:
        error(f"Variable '{varname}' not declared", current_line)

    next_tok()  # consume identifier

    # Expect IS NOW A
    if current_token is None or current_token[1] != "type_convert_keyword":
        error("Expected 'IS NOW A' keyword in full typecast", current_line)

    next_tok()  # consume IS NOW A

    # Expect type literal
    if current_token is None or current_token[1] != "type_literal":
        error("Expected type literal after 'IS NOW A'", current_line)

    new_type = current_token[0]  # NUMBR, NUMBAR, TROOF, YARN
    next_tok()

    # Convert value
    old_value = symbol_table[varname]["value"]

    try:
        if new_type == "NUMBR":
            new_value = int(old_value)
        elif new_type == "NUMBAR":
            new_value = float(old_value)
        elif new_type == "TROOF":
            # LOLCODE truthiness: NOOB is false; others based on Python truthiness
            new_value = bool(old_value)
        elif new_type == "YARN":
            new_value = str(old_value)
        else:
            error(f"Unknown type '{new_type}' in full typecast", current_line)
    except Exception:
        error(f"Cannot cast '{old_value}' to {new_type}", current_line)

    # Store value
    symbol_table[varname]["value"] = new_value
    symbol_table[varname]["type"] = new_type

    return ("FULL_TYPECAST", varname, new_type)


# ======= WORK IN PROGRESS ==========
def loop_stmt():
    return True

def function_def():
    return True

def return_stmt():
    return True


# Test
tokens = [
("HAI", "start_code_delimiter"),
("\n", "linebreak"),
("WAZZUP", "var_declaration_start"),
("\n", "linebreak"),
("I HAS A", "variable_declaration"),
("choice", "variable_identifier"),
("\n", "linebreak"),
("I HAS A", "variable_declaration"),
("input", "variable_identifier"),
("\n", "linebreak"),
("BUHBYE", "var_declaration_end"),
("\n", "linebreak"),
("    ", "empty_line"),
("    ", "empty_line"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("1. Compute age", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("2. Compute tip", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("3. Compute square area", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("0. Exit", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("", "empty_line"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Choice: ", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("GIMMEH", "input_keyword"),
("choice", "variable_identifier"),
("\n", "linebreak"),
("", "empty_line"),
("choice", "variable_identifier"),
("\n", "linebreak"),
("WTF?", "switch_keyword"),
("\n", "linebreak"),
("OMG", "switch_case_keyword"),
("1", "numbr_literal"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Enter birth year: ", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("GIMMEH", "input_keyword"),
("input", "variable_identifier"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("DIFF OF", "subtract_keyword"),
("2022", "numbr_literal"),
("AN", "and_keyword"),
("input", "variable_identifier"),
("\n", "linebreak"),
("GTFO", "break_keyword"),
("\n", "linebreak"),
("OMG", "switch_case_keyword"),
("2", "numbr_literal"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Enter bill cost: ", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("GIMMEH", "input_keyword"),
("input", "variable_identifier"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Tip: ", "string_literal"),
("\"", "string_delimiter"),
("+", "print_concatenation_keyword"),
("PRODUCKT", "variable_identifier"),
("OF", "variable_identifier"),
("input", "variable_identifier"),
("AN", "and_keyword"),
("0.1", "numbar_literal"),
("\n", "linebreak"),
("GTFO", "break_keyword"),
("\n", "linebreak"),
("OMG", "switch_case_keyword"),
("3", "numbr_literal"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Enter width: ", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("GIMMEH", "input_keyword"),
("input", "variable_identifier"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Square Area: ", "string_literal"),
("\"", "string_delimiter"),
("+", "print_concatenation_keyword"),
("PRODUKT OF", "multiply_keyword"),
("input", "variable_identifier"),
("AN", "and_keyword"),
("input", "variable_identifier"),
("\n", "linebreak"),
("GTFO", "break_keyword"),
("\n", "linebreak"),
("OMG", "switch_case_keyword"),
("0", "numbr_literal"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Goodbye", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("OMGWTF", "switch_default_keyword"),
("\n", "linebreak"),
("VISIBLE", "print_keyword"),
("\"", "string_delimiter"),
("Invalid Input!", "string_literal"),
("\"", "string_delimiter"),
("\n", "linebreak"),
("OIC", "end_of_if_block_keyword"),
("\n", "linebreak"),
("", "empty_line"),
("KTHXBYE", "end_code_delimiter"),
("\n", "linebreak"),
("", "empty_line")
]

# Run parser
parsed = program()

print(parsed)
# And print the symbol table for semantic results
print("\nSymbol table:")
print(symbol_table)