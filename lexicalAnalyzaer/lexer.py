# @Params
# prog: que contiene el programa como un string
# pos: que contiene la posición inicial de la búsqueda (0)
# long: que contiene la longitud del programa
def globales(prog, pos, long):
    global programa 
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long

def getToken(imprime = True):
