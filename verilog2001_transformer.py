from lark import Transformer

class verilog2001_transformer(Transformer):
    def module_declaration(self, stuff):
        return stuff
    def module(self, stuff):
        return stuff