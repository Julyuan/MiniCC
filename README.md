# MiniCC
## 编译器描述
我们实现的是一个类 C 语言的编译器，该编译器可以将 C 语言的代码转化成 x86 汇编指令，并可以编译连接生成win32可执行程序。

## 文件说明
```
CodeGenerate/       :代码生成模块
Doc/                :文档
masm32_en/          :MASM32连接运行环境
MiniCParser/        :语法分析模块
Optimizer/          :代码优化模块
SemanticAnalysis/   :语义分析模块
test_exmaples/      :测试用例
utils/              :可视化工具
compiler.py         :编译器接口
minicc_clean.sh     :运行脚本
minicc.sh           :运行脚本
README.md           :README
requirements.txt    :Python依赖库
```

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

其中document.pdf为总体报告，各个md文件为模块报告

其中samples中为测试样例
```

## 组员分工
赵竟霖 :中间代码生成、目标代码生成、代码优化、模块报告
黄文璨: 代码整合、语义分析、符号表设计、错误处理、语法树可视化、模块报告
金连源: 词法分析、语法分析、文档整合、模块报告
