
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programrightSINGLEEQUALPLUSEQUALMINUSEQUALDIVIDEEQUALTIMESEQUALleftDOUBLEPIPESleftDOUBLEAMPERSANDleftBANGEQUALDOUBLEEQUALleftLANGLERANGLELANGLEEQUALRANGLEEQUALleftPLUSMINUSleftTIMESDIVIDEPERCENTrightUMINUSEXCLAMATIONREMOVEREFADDRleftELSEADDR BANGEQUAL BREAK CHAR COMMA CONTINUE DIVIDE DIVIDEEQUAL DOT DOUBLEAMPERSAND DOUBLEEQUAL DOUBLEMINUS DOUBLEPIPES DOUBLEPLUS ELSE EXCLAMATION FLOAT FLOATLITERAL FOR ID IF INT INTLITERAL LANGLE LANGLEEQUAL LCURLY LEFTARROW LPAREN LSQUARE MINUS MINUSEQUAL PERCENT PLUS PLUSEQUAL RANGLE RANGLEEQUAL RCURLY RETURN RPAREN RSQUARE SEMICOLON SINGLEEQUAL STRUCT TIMES TIMESEQUAL VOID WHILEfunctionDeclaration : typeSpec ID LPAREN parameters RPAREN compoundStatementcompoundStatement : LCURLY optionalLocalDeclarations optionalStatementList RCURLYoptionalStatementList : statementList\n                            | emptyempty :optionalLocalDeclarations : localDeclarations\n                                | emptyparameters : parameterList\n                  | VOIDprogram : declarationListstatementList : statementList statement\n                     | statementstatement : expressionStatement\n                 | compoundStatement\n                 | ifStatement\n                 | whileStatement\n                 | forStatement\n                 | returnStatement\n                 | breakStatement\n                 | continueStatementexpressionStatement : expression SEMICOLON\n                           | SEMICOLONexpression : expression DOT IDexpression : expression LEFTARROW IDexpression : ADDR expressionexpression : TIMES expression %prec REMOVEREFexpression : expression LSQUARE expression RSQUAREexpression : expression SINGLEEQUAL expressionexpression : ID LPAREN argumentExpressionList RPAREN\n                    | ID LPAREN RPARENargumentExpressionList : argumentExpressionList COMMA expression\n                     | expressionexpression : expression DIVIDEEQUAL expression\n                  | expression PLUSEQUAL expression\n                  | expression MINUSEQUAL expression\n                  | expression TIMESEQUAL expressionexpression : expression DOUBLEPLUS\n                  | expression DOUBLEMINUSexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression DOUBLEPIPES expression\n                  | expression DOUBLEAMPERSAND expression\n                  | expression LANGLE expression\n                  | expression RANGLE expression\n                  | expression LANGLEEQUAL expression\n                  | expression RANGLEEQUAL expression\n                  | expression BANGEQUAL expression\n                  | expression DOUBLEEQUAL expression\n                  | expression PERCENT expression\n                  expression : INTLITERALexpression : FLOATLITERALexpression : IDexpression : LPAREN expression RPARENexpression : MINUS expression %prec UMINUSexpression : EXCLAMATION expressiondeclarationList : declarationList declaration\n                       | declarationdeclaration : staticVariableDeclaration\n                  | functionDeclaration staticVariableDeclarationList : staticVariableDeclarationList staticVariableDeclaration\n                                    | staticVariableDeclarationforStatement : FOR LPAREN optionalExpression SEMICOLON optionalExpression SEMICOLON optionalExpression RPAREN statementoptionalExpression : expression\n                            | emptycontinueStatement : CONTINUE SEMICOLONtypeSpec : VOID\n                | INT\n                | FLOAT\n                | CHAR\n                | structSpecifierstructSpecifier : STRUCT ID LCURLY staticVariableDeclarationList RCURLY\n                        | STRUCT IDstaticVariableDeclaration : typeSpec declaratorList SEMICOLON\n                                | typeSpec declarator LSQUARE INTLITERAL RSQUARE SEMICOLONdeclaratorList : declaratorList COMMA declarator\n                | declaratordeclarator : pointer ID\n                 | IDpointer : TIMES\n                | TIMES pointer\n    parameter : typeSpec IDparameterList : parameterList COMMA parameter\n                      | parameterwhileStatement : WHILE LPAREN expression RPAREN statementlocalDeclarations : localDeclarations localDeclaration\n                        | localDeclarationlocalDeclaration : staticVariableDeclarationoptionalElseStatement : ELSE statement\n                            | emptyifStatement : IF LPAREN expression RPAREN statement optionalElseStatementreturnStatement : RETURN expression SEMICOLONbreakStatement : BREAK SEMICOLON'
    
_lr_action_items = {'EXCLAMATION':([21,44,46,48,49,50,51,52,53,54,56,57,58,61,62,63,64,65,68,69,70,71,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[-75,-76,-5,-89,54,-7,-6,-88,-17,54,54,-20,-14,54,-22,54,-12,-15,-16,54,54,-18,54,-13,-19,-87,-2,54,-11,54,54,54,-94,-67,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-21,54,54,-93,54,54,54,54,-86,-5,54,54,-92,-91,-90,54,-64,]),'INTLITERAL':([21,23,44,46,48,49,50,51,52,53,54,56,57,58,61,62,63,64,65,68,69,70,71,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[-75,29,-76,-5,-89,59,-7,-6,-88,-17,59,59,-20,-14,59,-22,59,-12,-15,-16,59,59,-18,59,-13,-19,-87,-2,59,-11,59,59,59,-94,-67,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-21,59,59,-93,59,59,59,59,-86,-5,59,59,-92,-91,-90,59,-64,]),'RETURN':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,56,-7,-6,-88,-17,-20,-14,-22,56,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,56,56,-86,-5,56,-92,-91,-90,56,-64,]),'LPAREN':([18,21,44,46,48,49,50,51,52,53,54,56,57,58,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[25,-75,-76,-5,-89,70,-7,-6,-88,-17,70,70,-20,-14,85,70,-22,70,-12,-15,88,-16,70,70,-18,91,92,70,-13,-19,-87,-2,70,-11,70,70,70,-94,-67,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-21,70,70,-93,70,70,70,70,-86,-5,70,70,-92,-91,-90,70,-64,]),'DOUBLEPIPES':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,96,-57,96,-56,-26,96,-25,-37,-38,96,96,-55,-30,96,96,-43,-48,96,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,96,96,96,-46,-47,96,96,-29,-27,96,]),'VOID':([0,3,6,7,8,13,21,25,26,35,37,40,43,44,45,46,48,51,52,81,83,],[1,-60,1,-61,-59,-58,-75,31,1,1,-63,1,-62,-76,-1,1,-89,1,-88,-87,-2,]),'DOUBLEMINUS':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,104,-57,104,-56,-26,104,-25,-37,-38,104,104,-55,-30,104,104,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,104,-28,-46,-47,-35,-36,-29,-27,104,]),'CHAR':([0,3,6,7,8,13,21,25,26,35,37,40,43,44,45,46,48,51,52,81,83,],[2,-60,2,-61,-59,-58,-75,2,2,2,-63,2,-62,-76,-1,2,-89,2,-88,-87,-2,]),'LCURLY':([19,21,39,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[26,-75,46,-76,-5,-89,46,-7,-6,-88,-17,-20,-14,-22,46,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,46,46,-86,-5,46,-92,-91,-90,46,-64,]),'WHILE':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,60,-7,-6,-88,-17,-20,-14,-22,60,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,60,60,-86,-5,60,-92,-91,-90,60,-64,]),'DOUBLEPLUS':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,97,-57,97,-56,-26,97,-25,-37,-38,97,97,-55,-30,97,97,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,97,-28,-46,-47,-35,-36,-29,-27,97,]),'RANGLEEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,98,-57,98,-56,-26,98,-25,-37,-38,98,98,-55,-30,98,98,98,-48,98,98,-40,-23,-45,-39,-42,98,-24,98,-51,-41,98,98,98,-46,-47,98,98,-29,-27,98,]),'DIVIDEEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,99,-57,99,-56,-26,99,-25,-37,-38,99,99,-55,-30,99,99,-43,-48,99,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,99,99,99,-46,-47,99,99,-29,-27,99,]),'BANGEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,100,-57,100,-56,-26,100,-25,-37,-38,100,100,-55,-30,100,100,100,-48,100,-49,-40,-23,-45,-39,-42,-50,-24,100,-51,-41,100,100,100,-46,-47,100,100,-29,-27,100,]),'MINUS':([21,44,46,48,49,50,51,52,53,54,56,57,58,59,61,62,63,64,65,68,69,70,71,72,74,75,76,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,163,164,166,167,168,],[-75,-76,-5,-89,61,-7,-6,-88,-17,61,61,-20,-14,-52,61,-22,61,-12,-15,-16,61,61,-18,-54,61,-13,-19,-53,101,-87,-57,-2,101,61,-56,-11,61,-26,101,61,61,-25,-94,-67,61,-37,61,61,61,61,61,-38,61,61,61,61,61,61,61,61,61,61,61,-21,61,61,-93,101,101,-55,-30,101,101,101,101,101,101,-40,-23,101,-39,-42,101,-24,101,-51,-41,101,101,101,101,101,101,101,61,61,-29,61,61,-27,-86,101,-5,61,61,-92,-91,-90,61,-64,]),'DOT':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,102,-57,102,-56,-26,102,-25,-37,-38,102,102,-55,-30,102,102,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,102,-28,-46,-47,-35,-36,-29,-27,102,]),'RSQUARE':([29,59,72,77,82,86,89,93,97,104,125,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,],[38,-52,-54,-53,-57,-56,-26,-25,-37,-38,-55,-30,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,156,-28,-46,-47,-35,-36,-29,-27,]),'LANGLE':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,103,-57,103,-56,-26,103,-25,-37,-38,103,103,-55,-30,103,103,103,-48,103,103,-40,-23,-45,-39,-42,103,-24,103,-51,-41,103,103,103,-46,-47,103,103,-29,-27,103,]),'RPAREN':([30,31,32,34,41,47,59,72,77,82,86,89,90,91,93,97,104,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,153,156,159,161,165,],[39,-9,-8,-85,-83,-84,-52,-54,-53,-57,-56,-26,125,126,-25,-37,-38,151,-66,-65,-55,-30,-32,153,155,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,-28,-46,-47,-35,-36,-29,-27,-31,-5,167,]),'DOUBLEEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,107,-57,107,-56,-26,107,-25,-37,-38,107,107,-55,-30,107,107,107,-48,107,-49,-40,-23,-45,-39,-42,-50,-24,107,-51,-41,107,107,107,-46,-47,107,107,-29,-27,107,]),'SEMICOLON':([14,16,18,21,24,27,28,38,44,46,48,49,50,51,52,53,57,58,59,62,63,64,65,68,71,72,75,76,77,78,79,80,81,82,83,84,86,87,88,89,93,94,95,97,104,117,120,122,123,124,125,126,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,151,152,153,155,156,157,158,160,162,163,164,166,167,168,],[21,-78,-80,-75,-79,-77,-80,44,-76,-5,-89,62,-7,-6,-88,-17,-20,-14,-52,-22,62,-12,-15,-16,-18,-54,-13,-19,-53,94,95,117,-87,-57,-2,120,-56,-11,-5,-26,-25,-94,-67,-37,-38,-21,-93,152,-66,-65,-55,-30,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,-28,-46,-47,-35,-36,62,-5,-29,62,-27,-86,161,-5,62,-92,-91,-90,62,-64,]),'RCURLY':([21,35,37,43,44,46,48,49,50,51,52,53,55,57,58,62,63,64,65,66,68,71,75,76,81,83,87,94,95,117,120,157,160,163,164,166,168,],[-75,42,-63,-62,-76,-5,-89,-5,-7,-6,-88,-17,83,-20,-14,-22,-3,-12,-15,-4,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,-86,-5,-92,-91,-90,-64,]),'COMMA':([14,16,18,24,27,28,32,34,41,47,59,72,77,82,86,89,93,97,104,125,126,127,128,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,148,149,150,153,156,159,],[20,-78,-80,-79,-77,-80,40,-85,-83,-84,-52,-54,-53,-57,-56,-26,-25,-37,-38,-55,-30,-32,154,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,-28,-46,-47,-35,-36,-29,-27,-31,]),'PLUS':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,105,-57,105,-56,-26,105,-25,-37,-38,105,105,-55,-30,105,105,105,105,105,105,-40,-23,105,-39,-42,105,-24,105,-51,-41,105,105,105,105,105,105,105,-29,-27,105,]),'IF':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,73,-7,-6,-88,-17,-20,-14,-22,73,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,73,73,-86,-5,73,-92,-91,-90,73,-64,]),'$end':([3,4,6,7,8,13,21,44,45,83,],[-60,0,-10,-61,-59,-58,-75,-76,-1,-2,]),'DIVIDE':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,106,-57,106,-56,-26,106,-25,-37,-38,106,106,-55,-30,106,106,106,106,106,106,106,-23,106,106,-42,106,-24,106,-51,-41,106,106,106,106,106,106,106,-29,-27,106,]),'FOR':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,67,-7,-6,-88,-17,-20,-14,-22,67,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,67,67,-86,-5,67,-92,-91,-90,67,-64,]),'LEFTARROW':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,108,-57,108,-56,-26,108,-25,-37,-38,108,108,-55,-30,108,108,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,108,-28,-46,-47,-35,-36,-29,-27,108,]),'DOUBLEAMPERSAND':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,109,-57,109,-56,-26,109,-25,-37,-38,109,109,-55,-30,109,109,109,-48,109,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,109,109,109,-46,-47,109,109,-29,-27,109,]),'PERCENT':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,110,-57,110,-56,-26,110,-25,-37,-38,110,110,-55,-30,110,110,110,110,110,110,110,-23,110,110,-42,110,-24,110,-51,-41,110,110,110,110,110,110,110,-29,-27,110,]),'TIMES':([1,2,5,9,11,12,15,19,20,21,36,42,44,46,48,49,50,51,52,53,54,56,57,58,59,61,62,63,64,65,68,69,70,71,72,74,75,76,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,163,164,166,167,168,],[-68,-71,-72,15,-69,-70,15,-74,15,-75,15,-73,-76,-5,-89,69,-7,-6,-88,-17,69,69,-20,-14,-52,69,-22,69,-12,-15,-16,69,69,-18,-54,69,-13,-19,-53,111,-87,-57,-2,111,69,-56,-11,69,-26,111,69,69,-25,-94,-67,69,-37,69,69,69,69,69,-38,69,69,69,69,69,69,69,69,69,69,69,-21,69,69,-93,111,111,-55,-30,111,111,111,111,111,111,111,-23,111,111,-42,111,-24,111,-51,-41,111,111,111,111,111,111,111,69,69,-29,69,69,-27,-86,111,-5,69,69,-92,-91,-90,69,-64,]),'PLUSEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,112,-57,112,-56,-26,112,-25,-37,-38,112,112,-55,-30,112,112,-43,-48,112,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,112,112,112,-46,-47,112,112,-29,-27,112,]),'LSQUARE':([16,18,24,28,59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[23,-80,-79,-80,-52,-54,-53,113,-57,113,-56,-26,113,-25,-37,-38,113,113,-55,-30,113,113,-43,-48,-33,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,-34,113,-28,-46,-47,-35,-36,-29,-27,113,]),'SINGLEEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,114,-57,114,-56,-26,114,-25,-37,-38,114,114,-55,-30,114,114,-43,-48,114,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,114,114,114,-46,-47,114,114,-29,-27,114,]),'RANGLE':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,115,-57,115,-56,-26,115,-25,-37,-38,115,115,-55,-30,115,115,115,-48,115,115,-40,-23,-45,-39,-42,115,-24,115,-51,-41,115,115,115,-46,-47,115,115,-29,-27,115,]),'ELSE':([53,57,58,62,65,68,71,75,76,83,94,95,117,120,157,160,163,164,166,168,],[-17,-20,-14,-22,-15,-16,-18,-13,-19,-2,-94,-67,-21,-93,-86,162,-92,-91,-90,-64,]),'LANGLEEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,116,-57,116,-56,-26,116,-25,-37,-38,116,116,-55,-30,116,116,116,-48,116,116,-40,-23,-45,-39,-42,116,-24,116,-51,-41,116,116,116,-46,-47,116,116,-29,-27,116,]),'ID':([1,2,5,9,10,11,12,15,17,19,20,21,22,31,33,36,42,44,46,48,49,50,51,52,53,54,56,57,58,61,62,63,64,65,68,69,70,71,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,102,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[-68,-71,-72,18,19,-69,-70,-81,24,-74,28,-75,-82,-68,41,28,-73,-76,-5,-89,72,-7,-6,-88,-17,72,72,-20,-14,72,-22,72,-12,-15,-16,72,72,-18,72,-13,-19,-87,-2,72,-11,72,72,72,-94,-67,72,72,72,72,72,135,72,72,72,72,140,72,72,72,72,72,72,72,72,-21,72,72,-93,72,72,72,72,-86,-5,72,72,-92,-91,-90,72,-64,]),'ADDR':([21,44,46,48,49,50,51,52,53,54,56,57,58,61,62,63,64,65,68,69,70,71,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[-75,-76,-5,-89,74,-7,-6,-88,-17,74,74,-20,-14,74,-22,74,-12,-15,-16,74,74,-18,74,-13,-19,-87,-2,74,-11,74,74,74,-94,-67,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,-21,74,74,-93,74,74,74,74,-86,-5,74,74,-92,-91,-90,74,-64,]),'STRUCT':([0,3,6,7,8,13,21,25,26,35,37,40,43,44,45,46,48,51,52,81,83,],[10,-60,10,-61,-59,-58,-75,10,10,10,-63,10,-62,-76,-1,10,-89,10,-88,-87,-2,]),'INT':([0,3,6,7,8,13,21,25,26,35,37,40,43,44,45,46,48,51,52,81,83,],[11,-60,11,-61,-59,-58,-75,11,11,11,-63,11,-62,-76,-1,11,-89,11,-88,-87,-2,]),'MINUSEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,118,-57,118,-56,-26,118,-25,-37,-38,118,118,-55,-30,118,118,-43,-48,118,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,118,118,118,-46,-47,118,118,-29,-27,118,]),'FLOAT':([0,3,6,7,8,13,21,25,26,35,37,40,43,44,45,46,48,51,52,81,83,],[12,-60,12,-61,-59,-58,-75,12,12,12,-63,12,-62,-76,-1,12,-89,12,-88,-87,-2,]),'FLOATLITERAL':([21,44,46,48,49,50,51,52,53,54,56,57,58,61,62,63,64,65,68,69,70,71,74,75,76,81,83,85,87,88,91,92,94,95,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,151,152,154,155,157,160,161,162,163,164,166,167,168,],[-75,-76,-5,-89,77,-7,-6,-88,-17,77,77,-20,-14,77,-22,77,-12,-15,-16,77,77,-18,77,-13,-19,-87,-2,77,-11,77,77,77,-94,-67,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-21,77,77,-93,77,77,77,77,-86,-5,77,77,-92,-91,-90,77,-64,]),'BREAK':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,78,-7,-6,-88,-17,-20,-14,-22,78,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,78,78,-86,-5,78,-92,-91,-90,78,-64,]),'CONTINUE':([21,44,46,48,49,50,51,52,53,57,58,62,63,64,65,68,71,75,76,81,83,87,94,95,117,120,151,155,157,160,162,163,164,166,167,168,],[-75,-76,-5,-89,79,-7,-6,-88,-17,-20,-14,-22,79,-12,-15,-16,-18,-13,-19,-87,-2,-11,-94,-67,-21,-93,79,79,-86,-5,79,-92,-91,-90,79,-64,]),'TIMESEQUAL':([59,72,77,80,82,84,86,89,90,93,97,104,121,124,125,126,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,153,156,159,],[-52,-54,-53,119,-57,119,-56,-26,119,-25,-37,-38,119,119,-55,-30,119,119,-43,-48,119,-49,-40,-23,-45,-39,-42,-50,-24,-44,-51,-41,119,119,119,-46,-47,119,119,-29,-27,119,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'forStatement':([49,63,151,155,162,167,],[53,53,53,53,53,53,]),'optionalStatementList':([49,],[55,]),'continueStatement':([49,63,151,155,162,167,],[57,57,57,57,57,57,]),'optionalExpression':([88,152,161,],[122,158,165,]),'compoundStatement':([39,49,63,151,155,162,167,],[45,58,58,58,58,58,58,]),'breakStatement':([49,63,151,155,162,167,],[76,76,76,76,76,76,]),'pointer':([9,15,20,36,],[17,22,17,17,]),'returnStatement':([49,63,151,155,162,167,],[71,71,71,71,71,71,]),'staticVariableDeclaration':([0,6,26,35,46,51,],[3,3,37,43,48,48,]),'parameters':([25,],[30,]),'optionalLocalDeclarations':([46,],[49,]),'statementList':([49,],[63,]),'program':([0,],[4,]),'structSpecifier':([0,6,25,26,35,40,46,51,],[5,5,5,5,5,5,5,5,]),'optionalElseStatement':([160,],[163,]),'parameter':([25,40,],[34,47,]),'empty':([46,49,88,152,160,161,],[50,66,123,123,164,123,]),'localDeclarations':([46,],[51,]),'declarationList':([0,],[6,]),'statement':([49,63,151,155,162,167,],[64,87,157,160,166,168,]),'functionDeclaration':([0,6,],[7,7,]),'declaratorList':([9,36,],[14,14,]),'whileStatement':([49,63,151,155,162,167,],[68,68,68,68,68,68,]),'localDeclaration':([46,51,],[52,81,]),'declaration':([0,6,],[8,13,]),'typeSpec':([0,6,25,26,35,40,46,51,],[9,9,33,36,36,33,36,36,]),'staticVariableDeclarationList':([26,],[35,]),'ifStatement':([49,63,151,155,162,167,],[65,65,65,65,65,65,]),'expressionStatement':([49,63,151,155,162,167,],[75,75,75,75,75,75,]),'parameterList':([25,],[32,]),'declarator':([9,20,36,],[16,27,16,]),'argumentExpressionList':([91,],[128,]),'expression':([49,54,56,61,63,69,70,74,85,88,91,92,96,98,99,100,101,103,105,106,107,109,110,111,112,113,114,115,116,118,119,151,152,154,155,161,162,167,],[80,82,84,86,80,89,90,93,121,124,127,129,130,131,132,133,134,136,137,138,139,141,142,143,144,145,146,147,148,149,150,80,124,159,80,124,80,80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('functionDeclaration -> typeSpec ID LPAREN parameters RPAREN compoundStatement','functionDeclaration',6,'p_functionDeclaration','calcyacc.py',24),
  ('compoundStatement -> LCURLY optionalLocalDeclarations optionalStatementList RCURLY','compoundStatement',4,'p_compoundStatement','calcyacc.py',28),
  ('optionalStatementList -> statementList','optionalStatementList',1,'p_optionalStatementList','calcyacc.py',32),
  ('optionalStatementList -> empty','optionalStatementList',1,'p_optionalStatementList','calcyacc.py',33),
  ('empty -> <empty>','empty',0,'p_empty','calcyacc.py',37),
  ('optionalLocalDeclarations -> localDeclarations','optionalLocalDeclarations',1,'p_optionalLocalDeclarations','calcyacc.py',40),
  ('optionalLocalDeclarations -> empty','optionalLocalDeclarations',1,'p_optionalLocalDeclarations','calcyacc.py',41),
  ('parameters -> parameterList','parameters',1,'p_parameters','calcyacc.py',46),
  ('parameters -> VOID','parameters',1,'p_parameters','calcyacc.py',47),
  ('program -> declarationList','program',1,'p_program','calcyacc.py',53),
  ('statementList -> statementList statement','statementList',2,'p_statementList','calcyacc.py',57),
  ('statementList -> statement','statementList',1,'p_statementList','calcyacc.py',58),
  ('statement -> expressionStatement','statement',1,'p_statement','calcyacc.py',70),
  ('statement -> compoundStatement','statement',1,'p_statement','calcyacc.py',71),
  ('statement -> ifStatement','statement',1,'p_statement','calcyacc.py',72),
  ('statement -> whileStatement','statement',1,'p_statement','calcyacc.py',73),
  ('statement -> forStatement','statement',1,'p_statement','calcyacc.py',74),
  ('statement -> returnStatement','statement',1,'p_statement','calcyacc.py',75),
  ('statement -> breakStatement','statement',1,'p_statement','calcyacc.py',76),
  ('statement -> continueStatement','statement',1,'p_statement','calcyacc.py',77),
  ('expressionStatement -> expression SEMICOLON','expressionStatement',2,'p_expressionStatement','calcyacc.py',81),
  ('expressionStatement -> SEMICOLON','expressionStatement',1,'p_expressionStatement','calcyacc.py',82),
  ('expression -> expression DOT ID','expression',3,'p_expression_dot','calcyacc.py',86),
  ('expression -> expression LEFTARROW ID','expression',3,'p_expression_arrow','calcyacc.py',90),
  ('expression -> ADDR expression','expression',2,'p_expression_getaddr','calcyacc.py',94),
  ('expression -> TIMES expression','expression',2,'p_expression_removeref','calcyacc.py',98),
  ('expression -> expression LSQUARE expression RSQUARE','expression',4,'p_expression_array','calcyacc.py',102),
  ('expression -> expression SINGLEEQUAL expression','expression',3,'p_expression_assign','calcyacc.py',106),
  ('expression -> ID LPAREN argumentExpressionList RPAREN','expression',4,'p_expression_functioncall','calcyacc.py',110),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_expression_functioncall','calcyacc.py',111),
  ('argumentExpressionList -> argumentExpressionList COMMA expression','argumentExpressionList',3,'p_expression_argument_list','calcyacc.py',119),
  ('argumentExpressionList -> expression','argumentExpressionList',1,'p_expression_argument_list','calcyacc.py',120),
  ('expression -> expression DIVIDEEQUAL expression','expression',3,'p_expression_composite','calcyacc.py',131),
  ('expression -> expression PLUSEQUAL expression','expression',3,'p_expression_composite','calcyacc.py',132),
  ('expression -> expression MINUSEQUAL expression','expression',3,'p_expression_composite','calcyacc.py',133),
  ('expression -> expression TIMESEQUAL expression','expression',3,'p_expression_composite','calcyacc.py',134),
  ('expression -> expression DOUBLEPLUS','expression',2,'p_expression_selfoperator','calcyacc.py',138),
  ('expression -> expression DOUBLEMINUS','expression',2,'p_expression_selfoperator','calcyacc.py',139),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calcyacc.py',144),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calcyacc.py',145),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calcyacc.py',146),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calcyacc.py',147),
  ('expression -> expression DOUBLEPIPES expression','expression',3,'p_expression_binop','calcyacc.py',148),
  ('expression -> expression DOUBLEAMPERSAND expression','expression',3,'p_expression_binop','calcyacc.py',149),
  ('expression -> expression LANGLE expression','expression',3,'p_expression_binop','calcyacc.py',150),
  ('expression -> expression RANGLE expression','expression',3,'p_expression_binop','calcyacc.py',151),
  ('expression -> expression LANGLEEQUAL expression','expression',3,'p_expression_binop','calcyacc.py',152),
  ('expression -> expression RANGLEEQUAL expression','expression',3,'p_expression_binop','calcyacc.py',153),
  ('expression -> expression BANGEQUAL expression','expression',3,'p_expression_binop','calcyacc.py',154),
  ('expression -> expression DOUBLEEQUAL expression','expression',3,'p_expression_binop','calcyacc.py',155),
  ('expression -> expression PERCENT expression','expression',3,'p_expression_binop','calcyacc.py',156),
  ('expression -> INTLITERAL','expression',1,'p_expression_intliteral','calcyacc.py',161),
  ('expression -> FLOATLITERAL','expression',1,'p_expression_floatliteral','calcyacc.py',165),
  ('expression -> ID','expression',1,'p_expression_identifier','calcyacc.py',169),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcyacc.py',173),
  ('expression -> MINUS expression','expression',2,'p_expr_uminus','calcyacc.py',177),
  ('expression -> EXCLAMATION expression','expression',2,'p_expr_exclamation','calcyacc.py',186),
  ('declarationList -> declarationList declaration','declarationList',2,'p_declarationList','calcyacc.py',191),
  ('declarationList -> declaration','declarationList',1,'p_declarationList','calcyacc.py',192),
  ('declaration -> staticVariableDeclaration','declaration',1,'p_declaration','calcyacc.py',207),
  ('declaration -> functionDeclaration','declaration',1,'p_declaration','calcyacc.py',208),
  ('staticVariableDeclarationList -> staticVariableDeclarationList staticVariableDeclaration','staticVariableDeclarationList',2,'p_staticVariableDeclarationList','calcyacc.py',213),
  ('staticVariableDeclarationList -> staticVariableDeclaration','staticVariableDeclarationList',1,'p_staticVariableDeclarationList','calcyacc.py',214),
  ('forStatement -> FOR LPAREN optionalExpression SEMICOLON optionalExpression SEMICOLON optionalExpression RPAREN statement','forStatement',9,'p_forStatement','calcyacc.py',225),
  ('optionalExpression -> expression','optionalExpression',1,'p_optionalExpression','calcyacc.py',229),
  ('optionalExpression -> empty','optionalExpression',1,'p_optionalExpression','calcyacc.py',230),
  ('continueStatement -> CONTINUE SEMICOLON','continueStatement',2,'p_continueStatement','calcyacc.py',234),
  ('typeSpec -> VOID','typeSpec',1,'p_typeSpec','calcyacc.py',238),
  ('typeSpec -> INT','typeSpec',1,'p_typeSpec','calcyacc.py',239),
  ('typeSpec -> FLOAT','typeSpec',1,'p_typeSpec','calcyacc.py',240),
  ('typeSpec -> CHAR','typeSpec',1,'p_typeSpec','calcyacc.py',241),
  ('typeSpec -> structSpecifier','typeSpec',1,'p_typeSpec','calcyacc.py',242),
  ('structSpecifier -> STRUCT ID LCURLY staticVariableDeclarationList RCURLY','structSpecifier',5,'p_structSpecifier','calcyacc.py',246),
  ('structSpecifier -> STRUCT ID','structSpecifier',2,'p_structSpecifier','calcyacc.py',247),
  ('staticVariableDeclaration -> typeSpec declaratorList SEMICOLON','staticVariableDeclaration',3,'p_staticVariableDeclaration','calcyacc.py',254),
  ('staticVariableDeclaration -> typeSpec declarator LSQUARE INTLITERAL RSQUARE SEMICOLON','staticVariableDeclaration',6,'p_staticVariableDeclaration','calcyacc.py',255),
  ('declaratorList -> declaratorList COMMA declarator','declaratorList',3,'p_declaratorList','calcyacc.py',262),
  ('declaratorList -> declarator','declaratorList',1,'p_declaratorList','calcyacc.py',263),
  ('declarator -> pointer ID','declarator',2,'p_declarator','calcyacc.py',274),
  ('declarator -> ID','declarator',1,'p_declarator','calcyacc.py',275),
  ('pointer -> TIMES','pointer',1,'p_pointer','calcyacc.py',282),
  ('pointer -> TIMES pointer','pointer',2,'p_pointer','calcyacc.py',283),
  ('parameter -> typeSpec ID','parameter',2,'p_parameter','calcyacc.py',295),
  ('parameterList -> parameterList COMMA parameter','parameterList',3,'p_parameterList','calcyacc.py',299),
  ('parameterList -> parameter','parameterList',1,'p_parameterList','calcyacc.py',300),
  ('whileStatement -> WHILE LPAREN expression RPAREN statement','whileStatement',5,'p_whileStatement','calcyacc.py',312),
  ('localDeclarations -> localDeclarations localDeclaration','localDeclarations',2,'p_localDeclarations','calcyacc.py',317),
  ('localDeclarations -> localDeclaration','localDeclarations',1,'p_localDeclarations','calcyacc.py',318),
  ('localDeclaration -> staticVariableDeclaration','localDeclaration',1,'p_localDeclaration','calcyacc.py',329),
  ('optionalElseStatement -> ELSE statement','optionalElseStatement',2,'p_optionalElseStatement','calcyacc.py',333),
  ('optionalElseStatement -> empty','optionalElseStatement',1,'p_optionalElseStatement','calcyacc.py',334),
  ('ifStatement -> IF LPAREN expression RPAREN statement optionalElseStatement','ifStatement',6,'p_ifStatement','calcyacc.py',341),
  ('returnStatement -> RETURN expression SEMICOLON','returnStatement',3,'p_returnStatement','calcyacc.py',345),
  ('breakStatement -> BREAK SEMICOLON','breakStatement',2,'p_breakStatement','calcyacc.py',349),
]
