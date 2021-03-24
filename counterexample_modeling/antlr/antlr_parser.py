
import sys
from antlr4 import *
from .smvLexer import smvLexer
from .smvParser import smvParser
from .BasicInfoListener import BasicInfoListener
class Antlr_Parser:
    def __init__(self, smv_file_name):
        self.inputs = FileStream(smv_file_name)
        self.lexer = smvLexer(self.inputs)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = smvParser(self.stream)
        self.listener = BasicInfoListener()
        self.walker = ParseTreeWalker()

        self.walker.walk(self.listener, self.parser.module())
    
        self.get_variables(self.listener.ctl_formulas+self.listener.ltl_formulas)
        self.ltl_formula_li = self.create_ltl_spec()
        #print(self.ltl_formula_li)
        self.ctl_formula_li = self.create_ctl_spec()
        print(self.ctl_formula_li)
        self.formulas_li = self.ltl_formula_li

    def get_variables(self,formulas):
        self.formula_li = [i.formula for i in formulas]
        self.var_li = []
        for i in self.formula_li:
            temp_var = ""
            for j in i:
                if j in [">", "<", "="]:
                    if temp_var not in self.var_li:
                        self.var_li.append(temp_var)
                    break
                elif j not in ["(", ")", "!", "-", " "]:
                    temp_var+=j
        #print(var_li)
    
    def create_ltl_spec(self):
        skip_li = ["U","&", "->", "|"]
        skip_ltl_li = []
        ltl_temp_li = ["G", "X", "F"]
        formulas_li = []
        connect_ope = ""
        formula = ""
        print(self.listener.ltl_formulas)
        for i in self.listener.ltl_formulas:
            
            ope_li = i.ltl_ope_li
            ope_li = sorted(set(ope_li), key = ope_li.index)

            
            for j in ope_li:
                if connect_ope != "" and i.depth == pre_depth:
                    formula += connect_ope
                    formula += " "
                    connect_ope = ""
                    break

                if j in ltl_temp_li:
                    if j not in skip_ltl_li:
                        formula+=j
                        formula+= " "
                elif j not in skip_li:
                    connect_ope = j

            if connect_ope == "":
                formulas_li.append("LTLSPEC " +formula+ i.formula) 
                formula = ""
            else:
    
                formula += i.formula
                formula += " "
                pre_depth = i.depth       
        formulas_li = sorted(set(formulas_li), key = formulas_li.index)
        return formulas_li

    def create_ctl_spec(self):
        skip_li = ["U","&", "->", "|"]
        skip_ctl_li = []
        ctl_temp_li = ["AG", "AX", "AF","EG","EX","EF"]
        formulas_li = []
        connect_ope = ""
        formula = ""
        for i in self.listener.ctl_formulas:
            
            ope_li = i.ctl_ope_li
            ope_li = sorted(set(ope_li), key = ope_li.index)
            

            for j in ope_li:
                if connect_ope != "" and i.depth == pre_depth:
                    formula += connect_ope
                    formula += " "
                    connect_ope = ""
                    break

                if j in ctl_temp_li:
                    if j not in skip_ctl_li:
                        formula+=j
                        formula+= " "
                elif j not in skip_li:
                    connect_ope = j

            if connect_ope == "":
                formulas_li.append("SPEC " +formula+ i.formula) 
                formula = ""
            else:
    
                formula += i.formula
                formula += " "
                pre_depth = i.depth       
        formulas_li = sorted(set(formulas_li), key = formulas_li.index)
        return formulas_li
if __name__ == '__main__':
    smv_file_name = 'test.smv'
    Antlr_Parser(smv_file_name)