# Main Program for AFLL Project

import ply.lex as lex #type:ignore
import ply.yacc as yacc #type:ignore
from ruby_lexer import lexer #type:ignore
from ruby_parser import parser #type:ignore

def print_header(title, char='='):
    print(f"\n{char * 50}")
    print(f"{title}")
    print(f"{char * 50}")

def analyze_code(code, construct_name):
    print_header(f"ANALYZING {construct_name}", '=')
    print(f"Input: {code}")
    
    # Lexical analysis
    print_header("LEXICAL ANALYSIS (TOKENS)", '-')
    lexer.input(code)
    for tok in iter(lexer.token, None):
        print(f"{tok.type:15} : {tok.value}")
    
    # Syntactic analysis
    print_header("SYNTACTIC ANALYSIS (PARSE TREE)", '-')
    result = parser.parse(code)
    if result:
        print(result)
    else:
        print("Parsing failed!")

def main():
    print_header("RUBY LANGUAGE CONSTRUCTS - AFLL PROJECT", '=')
    print("Programming Language: RUBY")
    
    
    # Define example code for each construct
    examples = {
        "BEGIN": "begin { x = 10 y = -5 z = x }",
        "IF ELSE": "if x > 10 y = 20 else y = 5 end",
        "RAISE EXCEPTION": 'raise Exception, "This is an error message"',
        "UNTIL": "count = 0 until count == 10 count = count + 1 end",
        "WHILE": "count = 10 while count > 0 count = count - 1 end"
    }
    
    # Analyze each construct
    for construct, code in examples.items():
        analyze_code(code, construct)
    
    # Summary
    print_header("SUMMARY OF IMPLEMENTED CONSTRUCTS", '=')
    print("1. BEGIN: A code block that is executed unconditionally")
    print("   Syntax: begin { statements }")
    print("2. IF ELSE: Conditional execution")
    print("   Syntax: if condition statements end")
    print("   Syntax: if condition statements else statements end")
    print("3. RAISE EXCEPTION: Exception handling")
    print("   Syntax: raise Exception, \"message\"")
    print("   Syntax: raise \"message\"")
    print("4. UNTIL: Loop that executes until a condition becomes true")
    print("   Syntax: statements until condition statements end")
    print("5. WHILE: Loop that executes while a condition remains true")
    print("   Syntax: statements while condition statements end")

if __name__ == "__main__":
    main()