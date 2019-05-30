import ply.yacc as yacc
from calclex import tokens

precedence = (
    #('nonassoc','LESSTHAN', 'GREATERTHAN'),
    ('right','SINGLEEQUAL'),
    ('left', 'DOUBLEPIPES'),
    ('left', 'DOUBLEAMPERSAND'),
    ('left','BANGEQUAL','DOUBLEEQUAL'),
    ('left', 'LANGLE','RANGLE','LANGLEEQUAL','RANGLEEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'PERCENT'),
    ('right', 'UMINUS','EXCLAMATION'),
    ('left','ELSE')
)

# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
# )
start = 'program'

def p_functionDeclaration(p):
    '''functionDeclaration : typeSpec ID LPAREN parameters RPAREN compoundStatement'''
    p[0] = ('functionDeclaration',p[1],p[2],p[4],p[6])

def p_compoundStatement(p):
    '''compoundStatement : LCURLY optionalLocalDeclarations optionalStatementList RCURLY'''
    p[0] = ('compoundStatement',p[2],p[3])

def p_optionalStatementList(p):
    '''optionalStatementList : statementList
                            | empty'''
    p[0] = ('optionalStatementList',p[1])

def p_empty(p):
    'empty :'

def p_optionalLocalDeclarations(p):
    '''optionalLocalDeclarations : localDeclarations
                                | empty'''
    p[0] = ('optionalLocalDeclarations',p[1])


def p_parameters(p):
    '''parameters : parameterList
                  | VOID'''
    p[0] = ('parameters',p[1])



def p_program(p):
    '''program : declarationList'''
    p[0] = ('program',p[1])

def p_statementList(p):
    '''statementList : statementList statement
                     | statement'''
    if len(p)==3:
        temp = p[1][1]
        temp.append(p[2])
        p[0] = (p[1][0],temp)
    #    print(p[1])
    else:
        temp = list()
        temp.append(p[1])
        p[0] = ('statementList', temp)

def p_statement(p):
    '''statement : expressionStatement
                 | compoundStatement
                 | ifStatement
                 | whileStatement
                 | returnStatement
                 | breakStatement'''
    p[0] = ('statement', p[1])

def p_expressionStatement(p):
    '''expressionStatement : expression SEMICOLON
                           | SEMICOLON'''
    p[0] = ('expressionStatement',p[1])

def p_expression_assign(p):
    '''expression : ID SINGLEEQUAL expression'''
    p[0] = ('assign-expression', p[1],p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DOUBLEPIPES expression
                  | expression DOUBLEAMPERSAND expression
                  | expression LANGLE expression
                  | expression RANGLE expression
                  | expression LANGLEEQUAL expression
                  | expression RANGLEEQUAL expression
                  | expression BANGEQUAL expression
                  | expression DOUBLEEQUAL expression
                  | expression PERCENT expression
                  '''
    p[0] = ('binary-expression', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number-expression',p[1])

def p_expression_identifier(p):
    'expression : ID'
    p[0] = ('identifier-expression', p[1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ('group-expression', p[2])

def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = ('minus',p[2])

def p_expr_exclamation(p):
    'expression : EXCLAMATION expression'
    p[0] = ('exclamation',p[2])


def p_declarationList(p):
    '''declarationList : declarationList declaration
                       | declaration'''
    if len(p)<=2:
        temp = list()
        temp.append(p[1])
        p[0] = ('declarationList',temp)
    else:
        temp = p[1][1]
        temp.append(p[2])
        p[0] = (p[1][0], temp)

def p_error(p):
    print("Syntax error in input!")

def p_declaration(p):
    '''declaration : staticVariableDeclaration
                  | functionDeclaration'''
    p[0] = ('declaration', p[1])

def p_typeSpec(p):
    '''typeSpec : VOID
                | INT'''
    p[0] = ('typeSpec',p[1])

def p_staticVariableDeclaration(p):
    '''staticVariableDeclaration : typeSpec ID SEMICOLON'''
    p[0] = ('staticVariableDeclaration',p[1],p[2])

def p_parameter(p):
    '''parameter : typeSpec ID'''
    p[0] = ('parameter',p[1],p[2])

def p_parameterList(p):
    '''parameterList : parameterList COMMA parameter
                      | parameter'''
    if len(p)<=2:
        temp = list()
        temp.append(p[1])
        p[0] = ('parameterList',temp)
    else:
        temp = p[1][1]
        temp.append(p[3])
        p[0] = (p[1][0], temp)


def p_whileStatement(p):
    '''whileStatement : WHILE LPAREN expression RPAREN statement'''
    p[0] = ('whileStatement', p[3], p[5])


def p_localDeclarations(p):
    '''localDeclarations : localDeclarations localDeclaration
                        | localDeclaration'''
    if len(p)<=2:
        temp = list()
        temp.append(p[1])
        p[0] = ('localDeclarations',temp)
    else:
        temp = p[1][1]
        temp.append(p[2])
        p[0] = (p[1][0], temp)

def p_localDeclaration(p):
    '''localDeclaration : typeSpec ID SEMICOLON'''
    p[0] = ('localDeclaration',p[1],p[2])

def p_optionalElseStatement(p):
    '''optionalElseStatement : ELSE statement
                            | empty'''
    if len(p) <= 2:
        p[0] = ('optionalElseStatement',None)
    else:
        p[0] = ('optionalElseStatement',p[2])

def p_ifStatement(p):
    '''ifStatement : IF LPAREN expression RPAREN statement optionalElseStatement'''
    p[0] = ('ifStatement',p[3],p[5],p[6])

def p_returnStatement(p):
    '''returnStatement : RETURN expression SEMICOLON'''
    p[0] = ('returnStatement',p[2])

def p_breakStatement(p):
    '''breakStatement : BREAK SEMICOLON'''
    p[0] = ('breakStatement')

parser = yacc.yacc()

s = '''
int main(void){
int a;
if(a>0 || a < 1)
    return 0;
return a;
}
'''

def parse_grammar(s):
    result = parser.parse(s)
    return result

result = parser.parse(s)
print(result)