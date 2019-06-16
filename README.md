# MiniCC

## usage
安装Python依赖库
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
运行脚本
```
bash minicc.sh path-to-c-file path-to-asm-file
(sample:
bash minicc.sh test_examples/test2.c test2.asm
)
```
or
```
python3 compiler.py path-to-c-file path-to-asm-file
(sample:
python3 compiler.py test_examples/test2.c test2.asm
)
```

## 说明
```
上述指令运行后生成如下文件:
a.symtab        简易的符号表
a.syntax        元组语法树
a.syntax.gv     语法树可视化中间文件
a.syntax.gv.png 语法树可视化
a.mid           中间代码
test2.asm       未优化的目标代码
test2_op.asm    优化后的目标代码
```

## 文档
```
详见Doc文件夹

其中samples中为测试样例
```
