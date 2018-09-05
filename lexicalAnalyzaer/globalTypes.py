from enum import Enum

class TokenType(Enum):
    # Reserved Words
    IF = 'if'
    ELSE = 'else'
    INT = 'int'
    RETURN = 'return'
    VOID = 'void'
    WHILE = 'while'

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
    ISEQUAL = '=='
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
    