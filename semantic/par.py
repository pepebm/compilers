from lex import tokens
import ply.yacc as yacc
# tells the parser we're to start reading our grammer
start = 'start'
# defines arithmetic hierarchy while reading operations
precedence = (
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PLUS', 'MINUS')
)
# define our grammer with function
# the p_ format is required by the ply's module
def p_start(p):
    'start    : declaration_list'
    p[0] = ('start program',p[1])

def p_declaration_list(p):
    '''     declaration_list    : declaration_list declaration
                                | declaration
    '''
    if len(p) == 3:
        p[0] = ('declaration list', p[1], p[2])
    else: 
        p[0] = ('declaration list', p[1])


def p_declaration(p):
    '''     declaration     : var_declaration
                            | fun_declaration
                            | ENDFILE
    '''
    p[0] = ('declaration', p[1])


def p_var_declaration(p):
    '''     var_declaration : type_specifier ID SEMICOLON
                            | type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON
    '''
    if len(p) == 4:
        p[0] = ('var declaration', p[1], p[2], p[3])
    else: 
        p[0] = ('var declaration', p[1], p[2], p[3], p[4], p[5], p[6])

def p_type_specifier(p):
    '''
            type_specifier  : INT
                            | VOID
    '''
    p[0] = ('type specifier',p[1])

def p_fun_declaration(p):
    'fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'
    p[0] = ('fun declaration', p[1], p[2], p[3], p[4], p[5], p[6])


def p_params(p):
    ''' params      : param_list
                    | VOID
    '''
    p[0] = ('params', p[1])

def p_param_list(p):
    ''' param_list      : param_list COMMA param
                        | param
    '''
    if len(p) == 3:
        p[0] = ('param list', p[1], p[2], p[3])
    else: 
        p[0] = ('param list', p[1])

def p_param(p):
    ''' param   : type_specifier ID
                | type_specifier LBRACKET RBRACKET
    '''
    if len(p) == 3:
        p[0] = ('param', p[1], p[2])
    else: 
        p[0] = ('param', p[1], p[2], p[3])

def p_compound_stmt(p):
    'compound_stmt : LBLOCK local_declarations statement_list RBLOCK'
    p[0] = ('compound stmt', p[1], p[2], p[3], p[4])

def p_local_declarations(p):
    ''' local_declarations  : local_declarations var_declaration
                            |
    '''
    if len(p) == 3:
        p[0] = ("local declarations", p[1], p[2])


def p_statement_list(p):
    ''' statement_list  : statement_list statement
                        |
    '''
    if len(p) == 3:
        p[0] = ('statement list', p[1], p[2])

def p_statement(p):
    ''' statement   : expression_stmt
                    | compound_stmt
                    | selection_stmt
                    | iteration_stmt
                    | return_stmt
    '''
    p[0] = ('statement', p[1])

def p_expression_stmt(p):
    ''' expression_stmt  : expression SEMICOLON
                        | SEMICOLON
    '''
    if len(p) == 3:
        p[0] = ('expression stmt', p[1], p[2])
    else: 
        p[0] = ('expression stmt', p[1])

def p_selection_stmt(p):
    ''' selection_stmt  : IF LPAREN expression RPAREN statement
                        | IF LPAREN expression RPAREN statement ELSE statement
    '''
    if len(p) == 6:
        p[0] = ('selection stmt', p[1], p[2], p[3], p[4], p[5])
    else: 
        p[0] = ('selection stmt', p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_iteration_stmt(p):
    ' iteration_stmt  : WHILE LPAREN expression RPAREN statement'
    p[0] = ('iteration stmt', p[1], p[2], p[3], p[4], p[5])

def p_return_stmt(p):
    ''' return_stmt     : RETURN SEMICOLON
                        | RETURN expression SEMICOLON
    '''
    if len(p) == 4:
        p[0] = ('return stmtm', p[1], p[2])
    else: 
        p[0] = ('return stmt', p[1], p[2], p[3])

def p_expression(p):
    ''' expression      : var EQUAL expression
                        | simple_expression
    '''
    if len(p) == 4:
        p[0] = ('expression', p[1], p[2], p[3])
    else: 
        p[0] = ('expression', p[1])

def p_var(p):
    ''' var     : ID
                | ID LBRACKET expression RBRACKET
    '''
    if len(p) == 5:
        p[0] = ('var', p[1], p[2], p[3], p[4])
    else: 
        p[0] = ('var', p[1])

def p_simple_expression(p):
    ''' simple_expression   : additive_expression relop additive_expression
                            | additive_expression
    '''
    if len(p) == 4:
        p[0] = ('simple expression', p[1], p[2], p[3])
    else: 
        p[0] = ('simple expression', p[1])

def p_relop(p):
    ''' relop   : LE
                | LT
                | GREATER
                | LESS
                | COMPARE
                | NE
    '''
    p[0] = ('relop', p[1])

def p_additive_expression(p):
    '''     additive_expression     : additive_expression addop term
                                    | term
    '''
    if len(p) == 4:
        p[0] = ('additive expression', p[1], p[2], p[3])
    else: 
        p[0] = ('additive expression', p[1])

def p_addop(p):
    '''     addop   : PLUS
                    | MINUS
    '''
    p[0] = p[1]

def p_term(p):
    ''' term    : term mulop factor
                | factor
    '''
    if len(p) == 4:
        p[0] = ('term', p[1], p[2], p[3])
    else: 
        p[0] = ('term', p[1])

def p_mulop(p):
    '''     mulop   : TIMES
                    | DIVIDE
    '''
    p[0] = ('mulop', p[1])

def p_factor(p):
    ''' factor  : LPAREN expression RPAREN
                | ID
                | call
                | NUMBER
    '''
    if len(p) == 4:
        p[0] = ('factor', p[1], p[2] ,p[3])
    else: 
        p[0] = ('factor', p[1])

def p_call(p):
    ' call    : ID LPAREN args RPAREN '
    p[0] = ('call', p[1], p[2], p[3], p[4])

def p_args(p):
    ''' args    : arg_list
                |
    '''
    if len(p) == 2:
        p[0] = ('args', p[1])

def p_arg_list(p):
    ''' arg_list    : arg_list COMMA expression
                    | expression
    '''
    if len(p) == 4:
        p[0] = ('arg list', p[1], p[2] ,p[3])
    else: 
        p[0] = ('arg list', p[1])


def p_error(p):
    if not p:
        print("End of File!")
        return
    while True:
        # Get the next token
        tok = parser.token()
        print("panic mode: next token := ", tok)
        if not tok or tok.type == 'SEMICOLON' or tok.type == 'RBRACKET': break
    parser.restart()

parser = yacc.yacc(
    debug=True,
    write_tables=False,
    tabmodule="_parserjunk",
    errorlog=yacc.NullLogger()
)
