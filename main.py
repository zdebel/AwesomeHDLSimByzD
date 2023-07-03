import lark

verilog_grammar = './grammars/verilog.lark'

verilog_parser = lark.Lark.open(verilog_grammar)

try:
    tree = verilog_parser.parse(open("test_data/verilog/inverter.v").read())
    print(tree)
except Exception as e:
    print(e)