import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'return' : 'RETURN',
    'break' : 'BREAK',
    'void'  : 'VOID',
    'int'   : 'INT'
}
tokens = [
    'NUMBER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'SINGLEEQUAL',
    'DOUBLEEQUAL',
    'DOUBLEPIPES',
    'BANGEQUAL',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'SEMICOLON',
    'COMMA',
    'ID',
    'LANGLE',
    'RANGLE',
    'LANGLEEQUAL',
    'RANGLEEQUAL',
    'EXCLAMATION',
    'PERCENT'
] + list(reserved.values())

t_DOUBLEPIPES = r'\|\|'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LCURLY    = r'\{'
t_RCURLY    = r'\}'
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

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
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
data = '''
int main(void){
int a;
if(a>0 || a < 1)
    return 0;
return a;
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok)