import os
import sys
from MiniCParser import calcyacc
from CodeGenerate import genmid
from CodeGenerate import mid2masm32

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
OVERVIEW: clang LLVM compiler

USAGE: clang [options] <inputs>

OPTIONS:
  -###                    Print (but do not run) the commands to run for this compilation
  --analyzer-output <value>
                          Static analyzer report output format (html|plist|plist-multi-file|plist-html|text).
  --analyze               Run the static analyzer
  -arcmt-migrate-emit-errors
                          Emit ARC errors even if the migrator can fix them
  -arcmt-migrate-report-output <value>
                          Output path for the plist report
  -B <dir>                Add <dir> to search path for binaries and object files used implicitly
  -CC                     Include comments from within macros in preprocessed output
    ''')


if len(sys.argv)==1:
    myhelp()
    exit()


f = open(sys.argv[1])
s = f.read()
f.close()
# print(s)
result = calcyacc.parser.parse(s)

# print(type(result), len(result))
# print(result)

sys.stdout = Logger('a.mid')
genmid.parse_program(result)
sys.stdout.log.close()
sys.stdout = sys.stdout.terminal

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
