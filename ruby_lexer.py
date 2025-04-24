# import ply.lex as lex

# # List of token names.   This is always required
# tokens = (
#    'NUMBER',
#    'PLUS',
#    'MINUS',
#    'TIMES',
#    'DIVIDE',
#    'LPAREN',
#    'RPAREN',
# )

# # Regular expression rules for simple tokens
# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'

# # A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)    
#     return t

# # Define a rule so we can track line numbers
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# # A string containing ignored characters (spaces and tabs)
# t_ignore  = ' \t'

# # Error handling rule
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# #To use the lexer, you first need to feed it some input text using its input() method. 
# # After that, repeated calls to token() produce tokens. The following code shows how this works:


# # Test it out
# data = '''
# 3 + 4 * 10
#   + -20 *2
# '''

# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)







# Ruby Lexer Implementation for AFLL Project

import ply.lex as lex #type:ignore

# List of token names
tokens = (
    'BEGIN',
    'END',
    'IF',
    'ELSE',
    'RAISE',
    'EXCEPTION',
    'UNTIL',
    'WHILE',
    'ID',
    'NUM',
    'ASSIGN',
    'MINUS',
    'GTHAN',
    'LTHAN',
    'GTHAN_ASSIGN',
    'LTHAN_ASSIGN',
    'ASSIGN_ASSIGN',
    'COMMA',
    'STRING',
    'LBRACE',
    'RBRACE',
)

# Regular expression rules for simple tokens
t_ASSIGN = r'='
t_MINUS = r'-'
t_GTHAN = r'>'
t_LTHAN = r'<'
t_COMMA = r','
t_LBRACE = r'{'
t_RBRACE = r'}'

# Regular expression rules for compound operators
def t_GTHAN_ASSIGN(t):
    r'>='
    return t

def t_LTHAN_ASSIGN(t):
    r'<='
    return t

def t_ASSIGN_ASSIGN(t):
    r'=='
    return t

# Keywords
reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'else': 'ELSE',
    'raise': 'RAISE',
    'Exception': 'EXCEPTION',
    'until': 'UNTIL',
    'while': 'WHILE',
}

# Regular expression rules for identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'ID')
    return t

# Regular expression rules for numbers
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regular expression rules for string literals
def t_STRING(t):
    r'"[^"]*"'
    # Remove the quotes
    t.value = t.value[1:-1]
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test function
def test_lexer(data):
    print("LEXICAL ANALYSIS")
    print("-" * 50)
    print(f"Input: {data}")
    print("-" * 50)
    
    # Give the lexer some input
    lexer.input(data)
    
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: break
        print(f"Token: {tok.type}, Value: {tok.value}")
    
    print("-" * 50)

# Main function to test all constructs
if __name__ == "__main__":
    print("RUBY LANGUAGE CONSTRUCTS - LEXER TEST")
    print("=" * 50)
    
    # Test BEGIN construct
    print("\n1. BEGIN CONSTRUCT")
    begin_example = "begin { x = 10 y = -5 z = x }"
    test_lexer(begin_example)
    
    # Test IF ELSE construct
    print("\n2. IF ELSE CONSTRUCT")
    if_else_example = "if x > 10 y = 20 else y = 5 end"
    test_lexer(if_else_example)
    
    # Test RAISE EXCEPTION construct
    print("\n3. RAISE EXCEPTION CONSTRUCT")
    raise_example = 'raise Exception, "This is an error message"'
    test_lexer(raise_example)
    
    # Test UNTIL construct
    print("\n4. UNTIL CONSTRUCT")
    until_example = "count = 0 until count == 10 count = count + 1 end"
    test_lexer(until_example)
    
    # Test WHILE construct
    print("\n5. WHILE CONSTRUCT")
    while_example = "count = 10 while count > 0 count = count - 1 end"
    test_lexer(while_example)