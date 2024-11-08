import sys
from io import StringIO
from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from antlr4.tree.Trees import Trees

if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[1]} <File to Parse>")
    exit(1)

filepath = sys.argv[1]

def main():
    stream = FileStream(filepath)

    lexer = PythonLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = PythonParser(stream)

    tree = parser.prog()    
    print(tree.toStringTree(recog=parser))

    
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\nFailed to parse {sys.argv[1]}!")
    else:
        print("\nParsed Successfully!")

main()