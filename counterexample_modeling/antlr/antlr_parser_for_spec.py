
import sys
from antlr4 import *
from .smvLexer import smvLexer
from .smvParser import smvParser
from .BasicInfoListener import BasicInfoListener
class Antlr_Parser:
    def __init__(self, strings):
        self.inputs = InputStream("MODULE main " + "LTLSPEC " + strings)
        self.lexer = smvLexer(self.inputs)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = smvParser(self.stream)
        self.listener = BasicInfoListener()
        self.walker = ParseTreeWalker()
    
        self.walker.walk(self.listener, self.parser.module())
        
        for i in self.listener.formulas:
            print(i.depth, i.formula, i.ltl_ope_li)
        
if __name__ == '__main__':
    smv_file_name = "MODULE main " + "LTLSPEC " + 'F (switch = on)'
    Antlr_Parser(smv_file_name)