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
    if lexer.lexdata == None: 
        lexer.input(programa)
    t = lexer.token()
    if not t:
        print('Error getting the next char')
        return
    else:
        if t.value == TokenType.ENDFILE.value: 
            return TokenType.ENDFILE, TokenType.ENDFILE.value 
        if imprime: 
            print(str(t.type) + ' = ' + str(t.value))
        return t.type, t.value