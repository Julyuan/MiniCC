# 运行方法

1. 需要预装ply  
2. 修改calcyacc.py里212行的s，s就是源代码的内容  
3. 命令行输入python calcyacc.py，即可获得结果

# 说明

目前实现了如下的功能：

1. 函数和全局变量的声明
2. while语句（包含break）和if语句（包含else）
3. 函数返回return
4. int和void数据类型

注意事项：

1. 一个代码段里变量的声明需要放在最前面
2. 函数如果没有变量也要加void
3. 数据只支持void和int，还没有float
4. 外部调用接口是parse_grammar，输入代码，返回语法树