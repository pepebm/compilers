from ply import *
import pry
# This code was made with ply lexer based on the documentation
# src: https://www.dabeaz.com/ply/ply.html#ply_nn2

# All of the tokens available in the language
tokens = (
    # keywords
	'else', 'if', 'int', 'return', 'void', 'while', 
    # symbols
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LESS', 'LE', 
    'GREATER', 'GE', 'EQUAL', 'COMPARE', 'NE', 'SEMICOLON',
    'COMMA', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
	'LBLOCK', 'RBLOCK', 'ID',  'NUMBER', 'ENDFILE'
)

# Define regular expression of our symbols so it's 
# easy to identify them
t_PLUS 	 = r'\+'
t_MINUS	 = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS 	 = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA	 = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'\{'
t_RBLOCK   = r'}'
t_ENDFILE = r'\$'

t_ignore = ' \t'
# The t_[TokenName] is a syntaxis required by ply.lex
def t_NUMBER(t):
	r'\d+'
	# ID that starts with numbers
	if t.lexer.lexdata[t.lexpos+len(t.value)].isalpha():
		t_error(t)
	t.value = int(t.value)
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return t

def t_LE(t):
	r'<='
	return t

def t_GE(t):
	r'>='
	return t

def t_COMPARE(t):
	r'=='
	return t

def t_NE(t):
	r'!='
	return t

def t_newline(t):
	r'\n'
    # Move to new line
	t.lexer.lineno += 1

def t_comments(t):
    # Regex to identify comment block, do nothing
    # src: https://stackoverflow.com/questions/16160190/regular-expression-to-find-c-style-block-comments
	r'\/\*(\*(?!\/)|[^*])*\*\/'
	t.lexer.lineno += t.value.count('\n')

def t_error(t):
	errorline = t.lexer.lineno
	# ply.lex puts everything in one line so we need to split it
	# to get the correct pos of the error
	line = t.lexer.lexdata.split('\n')[errorline - 1]
	tabPos = line.find(t.lexer.lexdata[t.lexer.lexpos])
	print("Syntax Error @ line " + str(errorline))
	print(line)
	print(' ' * tabPos + '^')
	t.lexer.skip(1)

# Instantiate the lexer object
lexer = lex.lex()