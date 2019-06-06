import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'return' : 'RETURN',
    'break' : 'BREAK',
    'void'  : 'VOID',
    'int'   : 'INT',
    'float' : 'FLOAT',
    'char'  : 'CHAR',
    'struct' : 'STRUCT',
    'for' : 'FOR',
    'continue' : 'CONTINUE'
}
tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOUBLEPLUS',
    'DOUBLEMINUS',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVIDEEQUAL',
    'SINGLEEQUAL',
    'DOUBLEEQUAL',
    'DOUBLEPIPES',
    'DOUBLEAMPERSAND',
    'BANGEQUAL',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'LSQUARE',
    'RSQUARE',
    'SEMICOLON',
    'COMMA',
    'ID',
    'LANGLE',
    'RANGLE',
    'LANGLEEQUAL',
    'RANGLEEQUAL',
    'EXCLAMATION',
    'PERCENT',
    'DOT',
    'ADDR',
    'LEFTARROW',
    'FLOATLITERAL',
    'INTLITERAL'
] + list(reserved.values())

t_ADDR = r'&'
t_LEFTARROW = r'\->'
t_DOUBLEAMPERSAND = r'&&'
t_DOUBLEPIPES = r'\|\|'
t_DOUBLEPLUS = r'\+\+'
t_DOUBLEMINUS = r'--'
t_PLUSEQUAL = r'\+='
MINUSEQUAL = r'-='
TIMESEQUAL = r'*='
DIVIDEEQUAL = r'/='
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LCURLY    = r'\{'
t_RCURLY    = r'\}'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
t_SEMICOLON = r';'
t_COMMA     = r','
t_DOUBLEEQUAL = r'=='
t_SINGLEEQUAL = r'='
t_BANGEQUAL = r'!='
t_LANGLE = r'<'
t_RANGLE = r'>'
t_LANGLEEQUAL = r'<='
t_RANGLEEQUAL = r'>='
t_EXCLAMATION = r'!'
t_PERCENT = r'%'
t_DOT = r'\.'

def t_FLOATLITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t
lexer = lex.lex()


# Test it out
data = '''int a,b[10];
int f(int x,int y){
	b[2]=2;
	if(x<=1)
		return x;
	return f(x-1,y)+f(x-2,y);
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok)