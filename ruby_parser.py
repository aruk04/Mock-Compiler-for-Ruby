# # Yacc example

# import ply.yacc as yacc

# # Get the token map from the lexer.  This is required.
# from lex_example import tokens


# # To specify the grammar rules we have to define functions in our yacc file. 
# # The syntax for the same is as follows: 



# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]

# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]

# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]

# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]

# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]

# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]

# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]

# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# # Error rule for syntax errors
# def p_error(p):
#     print("Syntax error in input!")

# # Build the parser
# parser = yacc.yacc()

# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)


# Ruby Parser Implementation for AFLL Project


import ply.yacc as yacc #type:ignore
from ruby_lexer import tokens

# Parse tree node class
class Node:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children else []
        self.value = value
    
    def __str__(self, level=0):
        result = "  " * level + f"{self.type}"
        if self.value is not None:
            result += f": {self.value}"
        result += "\n"
        
        for child in self.children:
            result += child.__str__(level + 1)
        return result

# Starting rule - the program can be any of our constructs
def p_program(p):
    '''program : begin_block
               | if_block
               | raise_block
               | until_block
               | while_block'''
    p[0] = Node('PROGRAM', [p[1]])

# 1. BEGIN Construct
def p_begin_block(p):
    'begin_block : BEGIN LBRACE statement_list RBRACE'
    p[0] = Node('BEGIN_BLOCK', [p[3]])

# 2. IF ELSE Construct (two forms)
def p_if_block_simple(p):
    'if_block : IF condition statement_list END'
    p[0] = Node('IF_BLOCK', [p[2], p[3]])

def p_if_block_with_else(p):
    'if_block : IF condition statement_list ELSE statement_list END'
    p[0] = Node('IF_ELSE_BLOCK', [p[2], p[3], p[5]])

# 3. RAISE EXCEPTION Construct (two forms)
def p_raise_exception(p):
    'raise_block : RAISE EXCEPTION COMMA STRING'
    p[0] = Node('RAISE_EXCEPTION', [], p[4])

def p_raise_string(p):
    'raise_block : RAISE STRING'
    p[0] = Node('RAISE_STRING', [], p[2])

# 4. UNTIL Construct
def p_until_block(p):
    'until_block : statement_list UNTIL condition statement_list END'
    p[0] = Node('UNTIL_BLOCK', [p[1], p[3], p[4]])

# 5. WHILE Construct
def p_while_block(p):
    'while_block : statement_list WHILE condition statement_list END'
    p[0] = Node('WHILE_BLOCK', [p[1], p[3], p[4]])

# Statement list - one or more statements
def p_statement_list_single(p):
    'statement_list : statement'
    p[0] = Node('STATEMENT_LIST', [p[1]])

def p_statement_list_multiple(p):
    'statement_list : statement_list statement'
    p[1].children.append(p[2])
    p[0] = p[1]

# Single statement - currently just assignment
def p_statement(p):
    'statement : assignment'
    p[0] = p[1]

# Assignment statement
def p_assignment_num(p):
    'assignment : ID ASSIGN NUM'
    p[0] = Node('ASSIGN', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_assignment_minus_num(p):
    'assignment : ID ASSIGN MINUS NUM'
    p[0] = Node('ASSIGN', [Node('ID', [], p[1]), Node('NUM', [], -p[4])])

def p_assignment_id(p):
    'assignment : ID ASSIGN ID'
    p[0] = Node('ASSIGN', [Node('ID', [], p[1]), Node('ID', [], p[3])])

# Condition expressions
def p_condition_gthan(p):
    'condition : ID GTHAN NUM'
    p[0] = Node('GREATER_THAN', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_condition_lthan(p):
    'condition : ID LTHAN NUM'
    p[0] = Node('LESS_THAN', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_condition_gthan_equal(p):
    'condition : ID GTHAN_ASSIGN NUM'
    p[0] = Node('GREATER_EQUAL', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_condition_lthan_equal(p):
    'condition : ID LTHAN_ASSIGN NUM'
    p[0] = Node('LESS_EQUAL', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_condition_equal_num(p):
    'condition : ID ASSIGN_ASSIGN NUM'
    p[0] = Node('EQUAL', [Node('ID', [], p[1]), Node('NUM', [], p[3])])

def p_condition_equal_id(p):
    'condition : ID ASSIGN_ASSIGN ID'
    p[0] = Node('EQUAL', [Node('ID', [], p[1]), Node('ID', [], p[3])])

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test function
def test_parser(data):
    print("SYNTACTIC ANALYSIS")
    print("-" * 50)
    print(f"Input: {data}")
    print("-" * 50)
    
    result = parser.parse(data)
    if result:
        print("Parse Successful!")
        print("Parse Tree:")
        print(result)
    else:
        print("Parsing failed!")
    
    print("-" * 50)

# Main function to test all constructs
if __name__ == "__main__":
    print("RUBY LANGUAGE CONSTRUCTS - PARSER TEST")
    print("=" * 50)
    
    # Test BEGIN construct
    print("\n1. BEGIN CONSTRUCT")
    begin_example = "begin { x = 10 y = -5 z = x }"
    test_parser(begin_example)
    
    # Test IF ELSE construct
    print("\n2. IF ELSE CONSTRUCT")
    if_else_example = "if x > 10 y = 20 else y = 5 end"
    test_parser(if_else_example)
    
    # Test RAISE EXCEPTION construct
    print("\n3. RAISE EXCEPTION CONSTRUCT")
    raise_example = 'raise Exception, "This is an error message"'
    test_parser(raise_example)
    
    # Test UNTIL construct
    print("\n4. UNTIL CONSTRUCT")
    until_example = "count = 0 until count == 10 count = count + 1 end"
    test_parser(until_example)
    
    # Test WHILE construct
    print("\n5. WHILE CONSTRUCT")
    while_example = "count = 10 while count > 0 count = count - 1 end"
    test_parser(while_example)