import lark

verilog_grammar = './grammars/verilog2001.lark'

verilog_parser = lark.Lark.open(verilog_grammar)

try:
    tree = verilog_parser.parse(open("test_data/verilog/inverter.v").read())
    print(tree.pretty())
except Exception as e:
    print(e)