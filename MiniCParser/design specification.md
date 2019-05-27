# 语法解析器设计说明

这是一个Mini-C语言的文法解析器，输入是原始的C语言代码，输出是一棵抽象文法树

## 使用方法

项目的接口函数是calcyacc.py里的parse_grammar，调用方式为res = parse_grammar(s)。s是原始的代码字符串，res是返回的文法树

## 包依赖

项目用到了ply里面的lex和yacc工具

## 文法规则

本项目的文法规则是参照设计文档《Mini-C to JVM》
