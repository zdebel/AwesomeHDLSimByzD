from lark import Lark, logger
import logging
from lark import Transformer

def parseVerilogTree(tree, level = 0):
    print(tree.data)
    for c in tree.children:
        for i in range(0, level):
            print('#', end='')
        if (hasattr(c, 'children')):
            parseVerilogTree(c, level + 1)


verilog_grammar = '/home/zdebel/kodasy/AwesomeHDLSimByzD/grammars/verilog2001.lark'
verilog_parser = Lark.open(verilog_grammar, start="source_text")
try:
    tree = verilog_parser.parse(open("/home/zdebel/kodasy/AwesomeHDLSimByzD/test_data/verilog/fifo.v").read())
    print(tree.pretty())
    print("#### !!!! ####")
    parseVerilogTree(tree)
except Exception as e:
    print(e)
    exit()

