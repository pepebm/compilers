from sys import exit
# Globals
tables, values, current, n = [], [], 0, 0

# This functions works has a main function to this segment. It implements
# symbol tree's for each scope of the C- script. Then, based on the inference rules
# written in the documentation, this python script parse's the result of the ply parser output.
# This script was written with an recursive point-of-view.
def semantica(arbol, imprime=True):
    global current, n
    n = 2
    tabla(arbol)
    if imprime:
        for t in tables: print(t)
    # reset
    current = 0
    semanticRecursive(arbol, 0)
    

# Creates a symbol table for each scope, for it to travel ply lists, it is
# necessary to do a recursive approach
def tabla(t, scope=0):
    global current

    # lambda function
    def isEmpty(var, scope): return True if var not in tables[scope] else False
    

    if t is None or type(t) is int:
        return
    if t[0] == 'start program':
        tables.append({'scope': scope})
        tabla(t[1], scope)
    elif t[0] in ['declaration list', 'compound stmt', 'local declarations', 'statement list']:
        for x in range(1, len(t)):
            tabla(t[x], scope)
    elif t[0] in ['statement', 'expression stmt', 'expression', 'selection stmt', 'iteration stmt']:
        for x in range(1, len(t)):
            tabla(t[x], scope)
    elif t[0] in ['return stmtm',  'simple expression', 'additive expression', 'term']:
        for x in range(1, len(t)):
            tabla(t[x], scope)
    elif t[0] in ['factor', 'args', 'arg list']:
        for x in range(1, len(t)):
            tabla(t[x], scope)
    elif t[0] == 'declaration':
        tabla(t[1], scope)
    elif t[0] == 'var declaration':
        if isEmpty(t[2], scope):
            if len(t) == 4:
                tables[scope][t[2]] = t[1][1]
            else:
                tables[scope][t[2]] = f"{t[1][1]},{t[3]},{str(t[4])},{t[5]}"
    elif t[0] == 'fun declaration':
        current += 1
        tables.append({'scope': current})
        if isEmpty(t[2], scope):
            if t[4][1] == 'void':
                tables[0][t[2]] = f"{t[1][1]},fun,void"
            else:
                tables[0][t[2]] = f"{t[1][1]},fun"
                checkParams(t[2], t[4], current)
            tabla(t[6], current)
    elif t[0] == 'var':
        if not valVars(t[1], scope):
            exit()
    elif t[0] == 'call':
        if not valVars(t[1], scope):
            exit()
        else:
            for x in t:
                tabla(x, scope)

# Functions that recieves a AST tree generated by a ply parser
# Based on the Inference rules found in the documentation, this recursive function
# traveles the tree's lists parsing it
def semanticRecursive(t, scope):
    global current


    if t is None or type(t) is int:
        return
    nextStep = t[0]
    if nextStep in ['start program', 'declaration', 'statement', 'expression stmt']:
        semanticRecursive(t[1], scope)
    elif nextStep in ['declaration list', 'compound stmt', 'statement list']:
        for x in t:
            semanticRecursive(x, scope)
    elif nextStep == 'fun declaration':
        current += 1
        semanticRecursive(t[6], current)
    elif nextStep == 'expression':
        if len(t) == 4:
            if t[1][1] in tables[scope] and tables[scope][t[1][1]] == 'int':
                if typeCheck(t[3], t[1][1], scope):
                    return True
                else:
                    print(f"Error: Assigned value {t[1][1]} is different than {tables[scope][t[1][1]]}")
                    exit()
        else:
            semanticRecursive(t[1], scope)
    elif nextStep == 'simple expression':
        if len(t) == 2:
            checkFunc(t[1], scope)

# Makes a type check of the variable (v) inside an expression (exp) of a given scope
def typeCheck(exp, v, scope):
    if exp[0] == 'expression': return typeCheck(exp[1], v, scope)
    elif exp[0] == 'simple expression' or exp[0] == 'additive expression' or exp[0] == 'term':
        for e in range(1, len(exp)): return typeCheck(exp[e], v, scope)
    elif exp[0] == 'factor':
        if type(exp[1]) is int:
            if v in tables[scope]:
                if tables[scope][v] == 'int': return True
            elif v in tables[0]:
                if tables[0][v] == 'int': return True
            else:
                if exp[1] in ['input', 'output']:
                    return True
                else:
                    print(f"Error: Variable {exp[1]} is not declared in this scope")
                    exit()
        else:
            return typeCheck(exp[2], v, scope) if len(exp) == 4 else typeCheck(exp[1], v, scope)
    elif exp[0] == 'call':
        if exp[1] in tables[0]:
            temp = tables[0][exp[1]].split(",")
            if temp[0] == tables[scope][v]: return True
            else:
                print(f"Error: Values do not match up {temp[0]} and {tables[scope][v]}")
        else:
            if exp[1] in ['input','output']:
                return True
            else:
                print(f"Error: Unkown method {exp[1]}")
                exit()
    elif exp[0] == 'var':
        if exp[1] in tables[scope]:
            return True if tables[scope][exp[1]] == tables[scope][v] else False
        elif exp[1] in tables[0]:
            return True if tables[0][exp[1]] == tables[0][v] else False
        else:
            print("Unkown error")
            return False


# Creates values for each function (exp) of a given scope
def checkFunc(exp, scope):
    global values, n
    if exp[0] == 'call':
        if exp[1] in tables[0]:
            values = tables[0][exp[1]].split(",")
            checkFunc(exp[3], scope)
        else:
            if exp[1] in ['input', 'output']:
                return True
            else:
                print(f"Error: {exp[1]} is not defined in this scope")
                exit()
    elif exp[0] == 'args' or exp[0] == 'expression': 
        checkFunc(exp[1], scope)
    elif exp[0] in ['arg list', 'simple expression', 'additive expression', 'term']:
        for e in exp: checkFunc(e, scope)
    elif exp[0] == 'var':
        if exp[1] in tables[scope]:
            temp = tables[scope][exp[1]].split(",")
            if temp[0] == values[n]:
                n += 2
                return True
            else:
                print(f"Error: Value of {values[n]} is not {temp[0]}")
                exit()
        elif exp[1] in tables[0]:
            temp = tables[0][exp[1]].split(",")
            if temp[0] == values[n]: return True
            else:
                print(f"Error: Value {values[n]}, is not {temp[0]}")
                exit()
    elif exp[0] == 'factor':
        if type(exp[1]) is int:
            if 'int' == values[n]:
                n += 2
                return True
        else:
            return checkFunc(exp[2], scope) if len(exp) == 4 else checkFunc(exp[1], scope)


# Inserts the params passed in to functions scope
def checkParams(func, params, scope):
    if params[0] == 'params': 
        checkParams(func, params[1], scope)
    if params[0] == 'param list':
        for p in range(1, len(params)): checkParams(func, params[p], scope)
    elif params[0] == 'param':
        tables[scope][params[2]] = params[1][1]
        tables[0][func] = f"{tables[0][func]},{params[1][1]},{params[2]}"


# Validates declared variables inside a scope
def valVars(var, scope):
    t = tables
    res = True
    if var not in tables[scope]:
        if var not in tables[0]:
            res = False
            if var in ['input', 'output']:
                res = True
            else:
                print(f"Error: Variable not declared \"{var}\"")
        else:
            res = True
    return res

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
