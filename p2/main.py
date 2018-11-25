# Jose Manuel Beauregard Mendez
# A01021716
import sys

def match(c):
    global token, pos, cadena
    if token == c:
        pos+=1
        token = cadena[pos]
        return True
    if pos == len(cadena): 
        sys.exit("True")
    return False

def A():
    global token, pos, cadena
    if token == '3':
        match('3')
    elif token == 'c':
        match('c')
    elif token == '(':
        match('(')
        B()
        match(')')

def B():
    A()
    X()

def X():
    global token
    if token != None:
        match(',')
        B()

def main():
    global token, pos, cadena
    cadena = "(c,(c,(3)),(c))"
    #cadena = "(3,c,(c)"
    print(cadena)
    pos = 0
    token = cadena[pos]
    print(A())

if __name__ == '__main__':
    main()

