from par import parser

def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    programa = prog
    posicion = pos
    progLong = long

def printAST(lvl, count):
    if type(lvl) is tuple:
        for idx, l in enumerate(lvl):
            if type(l) is tuple or type(l) is str:
                if len(lvl) > 1:
                    if idx < 1:
                        if len(lvl) == 2 and type(lvl[1]) is str:
                            print('|', '-' * count, lvl[0])
                        else: 
                            print('|', '-' * count, lvl[0])
                    elif type(l) is str: 
                        print('|', '-' * count, l)
                printAST(l, count + 1)

def parse(imprime = True):
    t = parser.parse(programa)
    if imprime:
        printAST(t, 0)
        return t
    else:
        return t
