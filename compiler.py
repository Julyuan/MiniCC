import os
import sys
from MiniCParser import calcyacc
from CodeGenerate import genmid
from CodeGenerate import mid2masm32
from SemanticAnalysis import scoped_symbol_table
from Optimizer import optim
from utils.visualize_syntax_tree import show_syntax_tree

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass


def myhelp():
    print('''
OVERVIEW: MINICC compiler

USAGE: python3 compiler.py <inputfile> <outputfile>
    ''')

# help
if len(sys.argv)==1:
    myhelp()
    exit()

# analysis parse tree
f = open(sys.argv[1])
s = f.read()
f.close()

result = calcyacc.parser.parse(s)

if result==None:
    print('Error while generating abstract syntax tree.')
    exit()

# show syntax tree by picture
show_syntax_tree(result, 'a.syntax.gv', viewnow=True)

# write syntax tree tuple to file
f = open('a.syntax', 'w')
f.write(str(result))
f.close()

# generate middle file
sys.stdout = Logger('a.mid')
genmid.parse_program(result)
sys.stdout.log.close()
sys.stdout = sys.stdout.terminal

# analysis symbol table and write to file
f = open('a.symtab', 'w')
f.write(scoped_symbol_table.show_symbol_table(genmid.symbol_table).strip())
f.close()


# generate target code and write it to file
f = open('a.mid')
prog = f.read().strip()
f.close()
prog=[_.strip() for _ in prog.split(">"*9)]

asm_name=''
if len(sys.argv) <= 2:
    asm_name = 'a.asm'
else:
    asm_name = sys.argv[2]

sys.stdout = Logger(asm_name)
mid2masm32.parse_prog(prog)
sys.stdout.log.close()
sys.stdout = sys.stdout.terminal

# do optimization and write it to file
f=open(asm_name,"r")
asm_prog=f.read().strip()
f.close()

sys.stdout = Logger(asm_name+'op')
optim.optimize(asm_prog)
sys.stdout.log.close()
sys.stdout = sys.stdout.terminal
