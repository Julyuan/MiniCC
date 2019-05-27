# 语法解析器设计说明

这是一个Mini-C语言的文法解析器，输入是原始的C语言代码，输出是一棵抽象文法树

## 使用方法

项目的接口函数是calcyacc.py里的parse_grammar，调用方式为res = parse_grammar(s)。s是原始的代码字符串，res是返回的文法树

## 包依赖

项目用到了ply里面的lex和yacc工具

## 文法规则

本项目的文法规则是参照设计文档《Mini-C to JVM》  
目前实现的文法规则如下：  
terminals：

1. NUMBER        // 数字
2. PLUS          // 加法符号
3. MINUS         // 减法符号/负号
4. TIMES         // 乘法符号
5. DIVIDE        // 除法符号
6. SINGLEEQUAL   // 赋值符
7. DOUBLEEQUAL   // 等于判断符
8. DOUBLEPIPES   // 或运算符
9. BANGEQUAL     // 不等于判断符
10. LPAREN        // 左圆括号
11. RPAREN        // 右圆括号
12. LCURLY        // 左大括号
13. RCURLY        // 右大括号
14. SEMICOLON     // 冒号
15. COMMA         // 逗号
16. ID            // 变量的标识符
17. LANGLE        // 左尖括号
18. RANGLE        // 右尖括号
19. LANGLEEQUAL   // 小于等于
20. RANGLEEQUAL   // 大于等于
21. EXCLAMATION   // 感叹号
22. PERCENT       // 百分号
23. IF            // if keyword
24. ELSE          // else keyword
25. WHILE         // while keyword
26. RETURN        // return keyword
27. BREAK         // break keyword
28. VOID          // void keyword
29. INT           // int keyword
    
non-terminals：

* program                   // start symbol，代表整一个程序
* declarationList           // 外部声明列表 
* declaration               // 外部声明，包含函数声明和全局变量声明
* staticVariableDeclaration // 静态全局变量声明
* functionDeclaration       // 函数声明
* typeSpec                  // 类型指示（int，void ......)
* parameters                // 函数变量表，可以为VOID
* parameterList             // 函数变量列表
* compoundStatement         // 复合语句（带大括号）
* optionalLocalDeclarations // 可选局部变量声明
* optionalStatementList     // 可选局部语句声明
* statementList             // 内部语句列表
* statement                 // 内部语句
* expressionStatement       // 表达式语句
* ifStatement               // if语句
* whileStatement            // while语句
* returnStatement           // return语句
* breakStatement            // break语句
* expression                // 表达式
* localDeclarations         // 局部声明列表
* localDeclaration          // 局部声明
* optionalElseStatement     // 可选else语句

grammars：

* program : declarationList // 程序顶层的形式，由若干个全局变量和函数组成
* declarationList : declarationList declaration // declarationList的产生式  
      &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| declaration
* declaration : staticVariableDeclaration // declaration包含了静态变量和函数
                  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| functionDeclaration
* functionDeclaration : typeSpec ID LPAREN parameters RPAREN compoundStatement // 函数声明的格式
* compoundStatement : LCURLY optionalLocalDeclarations optionalStatementList RCURLY // 复合语句的格式
* typeSpec : VOID // 目前只支持void、int两种类型  
                &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| INT
* staticVariableDeclaration : typeSpec ID SEMICOLON // 全局静态变量声明格式
* parameter : typeSpec ID //函数声明里单个变量的格式
* parameterList : parameterList COMMA parameter // 变量列表产生式   
         &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| parameter
* parameters : parameterList
   &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | VOID
* statement : expressionStatement //statement导出式  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | compoundStatement  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | ifStatement  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | whileStatement  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | returnStatement  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | breakStatement  
* expression : expression PLUS expression //  expression的导出式  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression MINUS expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression TIMES expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression DIVIDE expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression DOUBLEPIPES expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression LANGLE expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression RANGLE expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression LANGLEEQUAL expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression RANGLEEQUAL expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression BANGEQUAL expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression DOUBLEEQUAL expression  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | expression PERCENT expression
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | NUMBER
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | ID
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | LPAREN expression RPAREN
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | EXCLAMATION expression
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | MINUS expression %prec UMINUS

* returnStatement : RETURN expression SEMICOLON //  return语句的语法规则
* breakStatement : BREAK SEMICOLON              // break语句的语法规则
* ifStatement : IF LPAREN expression RPAREN statement optionalElseStatement // if语句的语法规则
* optionalElseStatement : ELSE statement // else语句的语法规则  
 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | empty
* localDeclarations : localDeclarations localDeclaration
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| localDeclaration
* localDeclaration : typeSpec ID SEMICOLON
* optionalLocalDeclarations : localDeclarations
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| empty
* optionalStatementList : statementList
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| empty