from lex import lexer
from globalTypes import *
# @Params
# prog: que contiene el programa como un string
# pos: que contiene la posición inicial de la búsqueda (0)
# long: que contiene la longitud del programa
def globales(prog, pos, long):
    global programa 
    global posicion
    global progLong
    # Lexer will save the position and total length of the program
    programa = prog
    posicion = pos
    progLong = long

def getToken(imprime = True):
    # Checks if lexer has data
    if lexer.lexdata == None: 
        lexer.input(programa)
    # Get token
    t = lexer.token()
    # Something went wrong reading the file
    if not t:
        print('Error getting the next char')
        return
    else:
        # Checks if the next token is end of file ($), this is compared
        # with globalTypes Enum
        if t.value == TokenType.ENDFILE.value: 
            return TokenType.ENDFILE, TokenType.ENDFILE.value
        # Print every token identified by the lexer 
        if imprime: 
            print(str(t.type) + ' = ' + str(t.value))
        return t.type, t.value