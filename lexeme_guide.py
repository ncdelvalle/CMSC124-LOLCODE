# Any line starting with BTW or in the scope of OBTW-TLDR should be
line = "some line"
(line, "empty_line")

('\"', "string_delimiter")
('some string', "string_literal") #not including ""
('WIN', "troof_literal") #and FAIL
('NOOB', "type_literal") #and other types
('HAI', "start_code_delimiter")
('KTHXBYE', "end_code_delimiter")
('WAZZUP', "var_declaration_start")
('BUHBYE', "var_declaration_end")
('I HAS A', "variable_declaration")
('ITZ', "variable_assignment")
('R', "update_var_value")
('AN', "operator_delimiter")
('SUM OF', "add_keyword")
('DIFF OF', "subtract_keyword")
('PRODUKT OF', "multiply_keyword")
('QUOSHUNT OF', "divide_keyword")
('MOD OF', "modulo_keyword")
('BIGGR OF', "max_keyword")
('SMALLR OF', "min_keyword")
('BOTH OF', "add_keyword")
('EITHER OF', "or_keyword")
('WON OF', "xor_keyword")
('ANY OF', "multi_or_keyword")
('ALL OF', "multi_and_keyword")
('BOTH SAEM', "equal_keyword")
('DIFFRINT', "not_equal_keyword")
('SMOOSH', "concatenation_keyword")
('MAEK', "typecast_keyword")
('A', "typecast_prefix_keyword")
('IS NOW A', "type_convert_keyword")
('VISIBLE', "print_keyword")
('GIMME', "input_keyword")
('O RLY', "if_keyword")
('YA RLY', "if_true_keyword")
('MEBBE', "else_if_keyword")
('NO WAI', "else_keyword")
('OIC', "end_of_if_block_keyword")
('WTF?', "switch_keyword")
('OMG', "switch_case_keyword")
('OMGWTF?', "switch_default_keyword")
('IM IN YR', "initialize_loop_keyword")
('UPPIN', "increment_keyword")
('NERFIN', "decrement_keyword")
('YR', "separator_keyword")
('WILE', "while_keyword")
('TIL', "until_keyword")
('IM OUTTA YR', "break_loop_keyword")
('HOW IZ I', "define_function_keyword")
('IF U SAY SO', "function_end_keyword")
('I IZ', "function_call_keyword")
('MKAY', "end_of_assignment_keyword")
('varname', "variable_identifier")
('17.0', "numbar_literal") # and other types
('\\n', "linebreak")
('+', "print_concatenation_keyword")
('!', "no_newline_suffix")

# sample code
# HAI
# 	WAZZUP
# 		I HAS A choice
# 		I HAS A input
# 	BUHBYE
	
# 	BTW if w/o MEBBE, 1 only, everything else is invalid
# 	VISIBLE "1. Compute age"
# 	VISIBLE "2. Compute tip"
# 	VISIBLE "3. Compute square area"
# 	VISIBLE "0. Exit"

# 	VISIBLE "Choice: "
# 	GIMMEH choice

# 	choice
# 	WTF?
# 		OMG 1
# 			VISIBLE "Enter birth year: "
# 			GIMMEH input
# 			VISIBLE DIFF OF 2022 AN input
# 			GTFO
# 		OMG 2
# 			VISIBLE "Enter bill cost: "
# 			GIMMEH input
# 			VISIBLE "Tip: " PRODUCKT OF input AN 0.1
# 			GTFO
# 		OMG 3
# 			VISIBLE "Enter width: "
# 			GIMMEH input
# 			VISIBLE "Square Area: " PRODUKT OF input AN input
# 			GTFO
# 		OMG 0
# 			VISIBLE "Goodbye"
# 		OMGWTF
# 			VISIBLE "Invalid Input!"
# 	OIC

# KTHXBYE

# expected output
[
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
("BTW if w/o MEBBE, 1 only, everything else is invalid", "empty_line"),
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
("AN", "operator_delimiter"),
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
("AN", "operator_delimiter"),
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
("AN", "operator_delimiter"),
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