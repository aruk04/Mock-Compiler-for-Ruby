# Ruby Language Constructs Parser

This project implements a parser for a subset of Ruby language constructs using [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/). The parser builds a hierarchical parse tree to represent Ruby statements such as conditional blocks, loops, and exception handling.

---

## 🧠 Features

The parser currently supports the following Ruby constructs:

- `if` and `if-else` blocks  
- `raise` statements (two formats)  
- `until` loops  
- `while` loops  
- Assignments (`x = 10`, `y = -5`, `z = a`)
- Relational conditions: `>`, `<`, `>=`, `<=`, `==`

---

## 📁 File Structure

```bash
.
├── main.py             # Entry point to run the lexer and parser on Ruby constructs
├── ruby_lexer.py       # Defines tokens using PLY's lex module
├── ruby_parser.py      # Defines grammar and parser using PLY's yacc module
└── README.md           # Project documentation
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
https://github.com/aruk04/Mock-Compiler-for-Ruby.git
```

2. **Install dependencies**

```bash
pip install ply
```

---

## ▶️ How to Run

To test the parser:

```bash
python main.py
```

You’ll see the syntactic analysis of various Ruby constructs with the generated parse tree.

---

## ✅ Example

Input:

```ruby
if x > 10
  y = 20
else
  y = 5
end
```

Output:
```
SYNTACTIC ANALYSIS
--------------------------------------------------
Input: if x > 10 y = 20 else y = 5 end
--------------------------------------------------
Parse Successful!
Parse Tree:
PROGRAM
  IF_ELSE_BLOCK
    GREATER_THAN
      ID: x
      NUM: 10
    STATEMENT_LIST
      ASSIGN
        ID: y
        NUM: 20
    STATEMENT_LIST
      ASSIGN
        ID: y
        NUM: 5
```

---

## 📌 Notes

- This parser is meant for educational purposes and handles only a limited set of Ruby-like syntax.

---


