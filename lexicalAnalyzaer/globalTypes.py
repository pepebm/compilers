from enum import Enum

class TokenType(Enum):
    # Reserved Words
    IF = 'if'
    ELSE = 'else'
    INT = 'int'
    RETURN = 'return'
    VOID = 'void'
    WHILE = 'while'

    # Standards
    ID
    NUMBER

    # Symbols
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    LESS = '<'
    LESSEQUAL = '<='
    GREATER = '>'
    GREATEREQUAL = '>='
    EQUAL = '='
    DEQUAL = '=='
    NEQUAL = '!='
    SEMICOLOM = ';'
    ENDFILE = '$'
    COMMA = ','
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '['
    RBRACKET = ']'
    OPENBLOCK = '{'
    CLOSEBLOCK = '}'
    