# Generated from smv.g4 by ANTLR 4.7.1
from .smvListener import smvListener
from .smvParser import smvParser

# This class defines a complete listener for a parse tree produced by smvParser.
class LTL_Formula_Data:
    def __init__ (self, depth, formula, ltl_ope_li):
        
        self.depth = depth
        self.formula = formula
        self.ltl_ope_li = ltl_ope_li[:]

class CTL_Formula_Data:
    def __init__ (self, depth, formula, ctl_ope_li):
        
        self.depth = depth
        self.formula = formula
        self.ctl_ope_li = ctl_ope_li[:]

class BasicInfoListener(smvListener):

    def __init__(self):
        #変数の初期値のdict
        self.enter_assgin_flag = False
        self.variable_init_dict = {}
        self.variable_assign_dict = {}
        self.variable_constant_dict = {}
        #検査式分解
        self.enter_ltl_specification_flag = False
        self.ltl_ope_li = []
        self.ltl_depth = 0
        self.enter_ctl_specification_flag = False
        self.ctl_ope_li = []
        self.ctl_depth = 0
        self.ltl_formulas = []
        self.ctl_formulas = []
        #変数の定義
        self.module_type_tf = False
        self.var_dec_par_module = {}
        self.var_dec = {}
        
    # Enter a parse tree produced by smvParser#identifier.
    def enterIdentifier(self, ctx:smvParser.IdentifierContext):
        
        pass

    # Exit a parse tree produced by smvParser#identifier.
    def exitIdentifier(self, ctx:smvParser.IdentifierContext):
        pass


    # Enter a parse tree produced by smvParser#define_identifier.
    def enterDefine_identifier(self, ctx:smvParser.Define_identifierContext):
        pass

    # Exit a parse tree produced by smvParser#define_identifier.
    def exitDefine_identifier(self, ctx:smvParser.Define_identifierContext):
        pass


    # Enter a parse tree produced by smvParser#variable_identifier.
    def enterVariable_identifier(self, ctx:smvParser.Variable_identifierContext):
        pass

    # Exit a parse tree produced by smvParser#variable_identifier.
    def exitVariable_identifier(self, ctx:smvParser.Variable_identifierContext):
        pass


    # Enter a parse tree produced by smvParser#complex_identifier.
    def enterComplex_identifier(self, ctx:smvParser.Complex_identifierContext):
        pass

    # Exit a parse tree produced by smvParser#complex_identifier.
    def exitComplex_identifier(self, ctx:smvParser.Complex_identifierContext):
        pass


    # Enter a parse tree produced by smvParser#integer_number.
    def enterInteger_number(self, ctx:smvParser.Integer_numberContext):
        pass

    # Exit a parse tree produced by smvParser#integer_number.
    def exitInteger_number(self, ctx:smvParser.Integer_numberContext):
        pass


    # Enter a parse tree produced by smvParser#constant.
    def enterConstant(self, ctx:smvParser.ConstantContext):
        pass

    # Exit a parse tree produced by smvParser#constant.
    def exitConstant(self, ctx:smvParser.ConstantContext):
        pass


    # Enter a parse tree produced by smvParser#boolean_constant.
    def enterBoolean_constant(self, ctx:smvParser.Boolean_constantContext):
        pass

    # Exit a parse tree produced by smvParser#boolean_constant.
    def exitBoolean_constant(self, ctx:smvParser.Boolean_constantContext):
        pass


    # Enter a parse tree produced by smvParser#integer_constant.
    def enterInteger_constant(self, ctx:smvParser.Integer_constantContext):
        pass

    # Exit a parse tree produced by smvParser#integer_constant.
    def exitInteger_constant(self, ctx:smvParser.Integer_constantContext):
        pass


    # Enter a parse tree produced by smvParser#symbolic_constant.
    def enterSymbolic_constant(self, ctx:smvParser.Symbolic_constantContext):
        pass

    # Exit a parse tree produced by smvParser#symbolic_constant.
    def exitSymbolic_constant(self, ctx:smvParser.Symbolic_constantContext):
        pass


    # Enter a parse tree produced by smvParser#word_constant.
    def enterWord_constant(self, ctx:smvParser.Word_constantContext):
        pass

    # Exit a parse tree produced by smvParser#word_constant.
    def exitWord_constant(self, ctx:smvParser.Word_constantContext):
        pass


    # Enter a parse tree produced by smvParser#word_width.
    def enterWord_width(self, ctx:smvParser.Word_widthContext):
        pass

    # Exit a parse tree produced by smvParser#word_width.
    def exitWord_width(self, ctx:smvParser.Word_widthContext):
        pass


    # Enter a parse tree produced by smvParser#word_value.
    def enterWord_value(self, ctx:smvParser.Word_valueContext):
        pass

    # Exit a parse tree produced by smvParser#word_value.
    def exitWord_value(self, ctx:smvParser.Word_valueContext):
        pass


    # Enter a parse tree produced by smvParser#range_constant.
    def enterRange_constant(self, ctx:smvParser.Range_constantContext):
        pass

    # Exit a parse tree produced by smvParser#range_constant.
    def exitRange_constant(self, ctx:smvParser.Range_constantContext):
        pass


    # Enter a parse tree produced by smvParser#basic_expr.
    def enterBasic_expr(self, ctx:smvParser.Basic_exprContext):
        #if self.enter_ltl_specification_flag:
            #print(ctx.getChild(0).getText())
        pass

    # Exit a parse tree produced by smvParser#basic_expr.
    def exitBasic_expr(self, ctx:smvParser.Basic_exprContext):
        pass


    # Enter a parse tree produced by smvParser#basic_expr_list.
    def enterBasic_expr_list(self, ctx:smvParser.Basic_expr_listContext):
        pass

    # Exit a parse tree produced by smvParser#basic_expr_list.
    def exitBasic_expr_list(self, ctx:smvParser.Basic_expr_listContext):
        pass


    # Enter a parse tree produced by smvParser#set_body_expr.
    def enterSet_body_expr(self, ctx:smvParser.Set_body_exprContext):
        pass

    # Exit a parse tree produced by smvParser#set_body_expr.
    def exitSet_body_expr(self, ctx:smvParser.Set_body_exprContext):
        pass


    # Enter a parse tree produced by smvParser#case_expr.
    def enterCase_expr(self, ctx:smvParser.Case_exprContext):

        self.case_assign_list = []
        pass

    # Exit a parse tree produced by smvParser#case_expr.
    def exitCase_expr(self, ctx:smvParser.Case_exprContext):
        pass


    # Enter a parse tree produced by smvParser#case_body.
    def enterCase_body(self, ctx:smvParser.Case_bodyContext):
        if self.enter_assgin_flag == True:
            
            temp = []
            for i in range(4):
                if ctx.getChild(i).__class__.__name__ == 'Basic_exprContext':
                    temp.append(ctx.getChild(i).getText())
            self.case_assign_list.insert(0, temp)
            """
            print(ctx.getChild(0).__class__.__name__,ctx.getChild(0).getText() )
            print(ctx.getChild(1).__class__.__name__,ctx.getChild(1).getText())
            print(ctx.getChild(2).__class__.__name__,ctx.getChild(2).getText())
            print(ctx.getChild(3).__class__.__name__,ctx.getChild(3).getText())
            """
        pass

    # Exit a parse tree produced by smvParser#case_body.
    def exitCase_body(self, ctx:smvParser.Case_bodyContext):
        pass


    # Enter a parse tree produced by smvParser#simple_expr.
    def enterSimple_expr(self, ctx:smvParser.Simple_exprContext):
        pass

    # Exit a parse tree produced by smvParser#simple_expr.
    def exitSimple_expr(self, ctx:smvParser.Simple_exprContext):
        pass


    # Enter a parse tree produced by smvParser#next_expr.
    def enterNext_expr(self, ctx:smvParser.Next_exprContext):
        pass

    # Exit a parse tree produced by smvParser#next_expr.
    def exitNext_expr(self, ctx:smvParser.Next_exprContext):
        pass


    # Enter a parse tree produced by smvParser#type_specifier.
    def enterType_specifier(self, ctx:smvParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by smvParser#type_specifier.
    def exitType_specifier(self, ctx:smvParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by smvParser#simple_type_specifier.
    def enterSimple_type_specifier(self, ctx:smvParser.Simple_type_specifierContext):
        pass

    # Exit a parse tree produced by smvParser#simple_type_specifier.
    def exitSimple_type_specifier(self, ctx:smvParser.Simple_type_specifierContext):
        pass


    # Enter a parse tree produced by smvParser#enumeration_type_body.
    def enterEnumeration_type_body(self, ctx:smvParser.Enumeration_type_bodyContext):
        pass

    # Exit a parse tree produced by smvParser#enumeration_type_body.
    def exitEnumeration_type_body(self, ctx:smvParser.Enumeration_type_bodyContext):
        pass


    # Enter a parse tree produced by smvParser#enumeration_type_value.
    def enterEnumeration_type_value(self, ctx:smvParser.Enumeration_type_valueContext):
        pass

    # Exit a parse tree produced by smvParser#enumeration_type_value.
    def exitEnumeration_type_value(self, ctx:smvParser.Enumeration_type_valueContext):
        pass


    # Enter a parse tree produced by smvParser#module_type_specifier.
    def enterModule_type_specifier(self, ctx:smvParser.Module_type_specifierContext):
        self.module_type_tf = True
        

    # Exit a parse tree produced by smvParser#module_type_specifier.
    def exitModule_type_specifier(self, ctx:smvParser.Module_type_specifierContext):
        pass


    # Enter a parse tree produced by smvParser#parameter_list.
    def enterParameter_list(self, ctx:smvParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by smvParser#parameter_list.
    def exitParameter_list(self, ctx:smvParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by smvParser#var_declaration.
    def enterVar_declaration(self, ctx:smvParser.Var_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#var_declaration.
    def exitVar_declaration(self, ctx:smvParser.Var_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#ivar_declaration.
    def enterIvar_declaration(self, ctx:smvParser.Ivar_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#ivar_declaration.
    def exitIvar_declaration(self, ctx:smvParser.Ivar_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#frozenvar_declaration.
    def enterFrozenvar_declaration(self, ctx:smvParser.Frozenvar_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#frozenvar_declaration.
    def exitFrozenvar_declaration(self, ctx:smvParser.Frozenvar_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#var_list.
    def enterVar_list(self, ctx:smvParser.Var_listContext):
        #print(ctx.getChild(1).getText())
        #print(ctx.getChildCount())
        #print("-----")
        #for i in range(ctx.getChildCount()):
         #   print(ctx.getChild(i).getText())
        #else:
        #    print("~~~~~")
        #s
        
        pass
        #print( self.var_dec)

    # Exit a parse tree produced by smvParser#var_list.
    def exitVar_list(self, ctx:smvParser.Var_listContext):
        if ctx.getChildCount() == 4:
            #self.var_dec[ctx.getChild(0).getText()] =  ctx.getChild(2).getText()
            #print(ctx.getChild(2).getChild(0).getText())
            if self.module_type_tf:
                if len(ctx.getChild(2).getChild(0).getText()) >= 7 and ctx.getChild(2).getChild(0).getText()[0:7] == "process":
                    module_instant_dict = {"process_tf":True}
                    temp_text = ctx.getChild(2).getChild(0).getText()[7:]
                else:
                    module_instant_dict = {"process_tf":False}
                    temp_text = ctx.getChild(2).getChild(0).getText()

                if "(" in temp_text :
                    process_module = temp_text.split("(")[0]
                    temp_paras = temp_text.split("(")[1].replace(")", "").split(",")
                    temp_paras = [i for i in temp_paras if i != ""]
                    if len(temp_paras) > 0:
                        module_instant_dict["paras"] = temp_paras
                else:
                    process_module = temp_text
                    
                module_instant_dict["module"]= process_module
                #print(module_instant_dict)
                self.var_dec[ctx.getChild(0).getText()]  = module_instant_dict

            else:
                self.var_dec[ctx.getChild(0).getText()] =  ctx.getChild(2).getText()
        elif ctx.getChildCount() == 5:
            
            #self.var_dec[ctx.getChild(1).getText()] =  ctx.getChild(3).getText()
            #print(ctx.getChild(3).getChild(0).getText())
            if self.module_type_tf:
                if len(ctx.getChild(3).getChild(0).getText()) >= 7 and ctx.getChild(3).getChild(0).getText()[0:7] == "process":
                    module_instant_dict = {"process_tf":True}
                    temp_text = ctx.getChild(3).getChild(0).getText()[7:]
                else:
                    module_instant_dict = {"process_tf":False}
                    temp_text = ctx.getChild(3).getChild(0).getText()

                if "(" in temp_text :
                    process_module = temp_text.split("(")[0]
                    temp_paras = temp_text.split("(")[1].replace(")", "").split(",")
                    temp_paras = [i for i in temp_paras if i != ""]
                    if len(temp_paras) > 0:
                        module_instant_dict["paras"] = temp_paras
                else:
                    process_module = temp_text
                    
                module_instant_dict["module"]= process_module
                    
                #print(module_instant_dict)
                self.var_dec[ctx.getChild(1).getText()] = module_instant_dict
            else:
                self.var_dec[ctx.getChild(1).getText()] =  ctx.getChild(3).getText()

        self.module_type_tf = False
       


    # Enter a parse tree produced by smvParser#simple_var_list.
    def enterSimple_var_list(self, ctx:smvParser.Simple_var_listContext):
        pass

    # Exit a parse tree produced by smvParser#simple_var_list.
    def exitSimple_var_list(self, ctx:smvParser.Simple_var_listContext):
        pass


    # Enter a parse tree produced by smvParser#define_declaration.
    def enterDefine_declaration(self, ctx:smvParser.Define_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#define_declaration.
    def exitDefine_declaration(self, ctx:smvParser.Define_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#define_body.
    def enterDefine_body(self, ctx:smvParser.Define_bodyContext):
        pass

    # Exit a parse tree produced by smvParser#define_body.
    def exitDefine_body(self, ctx:smvParser.Define_bodyContext):
        pass


    # Enter a parse tree produced by smvParser#constants_declaration.
    def enterConstants_declaration(self, ctx:smvParser.Constants_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#constants_declaration.
    def exitConstants_declaration(self, ctx:smvParser.Constants_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#constants_body.
    def enterConstants_body(self, ctx:smvParser.Constants_bodyContext):
        pass

    # Exit a parse tree produced by smvParser#constants_body.
    def exitConstants_body(self, ctx:smvParser.Constants_bodyContext):
        pass


    # Enter a parse tree produced by smvParser#assign_constraint.
    def enterAssign_constraint(self, ctx:smvParser.Assign_constraintContext):
        pass

    # Exit a parse tree produced by smvParser#assign_constraint.
    def exitAssign_constraint(self, ctx:smvParser.Assign_constraintContext):
        pass


    # Enter a parse tree produced by smvParser#assign_list.
    def enterAssign_list(self, ctx:smvParser.Assign_listContext):
        pass

    # Exit a parse tree produced by smvParser#assign_list.
    def exitAssign_list(self, ctx:smvParser.Assign_listContext):
        pass


    # Enter a parse tree produced by smvParser#assign.
    def enterAssign(self, ctx:smvParser.AssignContext):
        self.enter_assgin_flag = True
        if ctx.getChild(0).getText() == 'init':
            self.variable_init_dict[ctx.getChild(2).getText()] = ctx.getChild(6).getText()
            #print(ctx.getChild(2).getText(), ctx.getChild(6).getText() )
        elif ctx.getChild(0).getText() == 'next':
           # self.variable_assign_dict[ctx.getChild(2).getText()] = ctx.getChild(6).getText()
            #print(ctx.getChild(2).getText(), ctx.getChild(6).getText())
            pass
        else:
            
            self.variable_constant_dict[ctx.getChild(0).getText()] = ctx.getChild(3).getText()
            #print(ctx.getChild(0).getText(),ctx.getChild(2).getText() )
        pass

    # Exit a parse tree produced by smvParser#assign.
    def exitAssign(self, ctx:smvParser.AssignContext):
        if  ctx.getChild(0).getText() == 'next':
            self.variable_assign_dict[ctx.getChild(2).getText()] =self.case_assign_list
        self.enter_assgin_flag = False
        pass


    # Enter a parse tree produced by smvParser#trans_constraint.
    def enterTrans_constraint(self, ctx:smvParser.Trans_constraintContext):
        pass

    # Exit a parse tree produced by smvParser#trans_constraint.
    def exitTrans_constraint(self, ctx:smvParser.Trans_constraintContext):
        pass


    # Enter a parse tree produced by smvParser#init_constraint.
    def enterInit_constraint(self, ctx:smvParser.Init_constraintContext):
        pass

    # Exit a parse tree produced by smvParser#init_constraint.
    def exitInit_constraint(self, ctx:smvParser.Init_constraintContext):
        pass


    # Enter a parse tree produced by smvParser#invar_constraint.
    def enterInvar_constraint(self, ctx:smvParser.Invar_constraintContext):
        pass

    # Exit a parse tree produced by smvParser#invar_constraint.
    def exitInvar_constraint(self, ctx:smvParser.Invar_constraintContext):
        pass


    # Enter a parse tree produced by smvParser#fairness_constraint.
    def enterFairness_constraint(self, ctx:smvParser.Fairness_constraintContext):
        pass

    # Exit a parse tree produced by smvParser#fairness_constraint.
    def exitFairness_constraint(self, ctx:smvParser.Fairness_constraintContext):
        pass


    # Enter a parse tree produced by smvParser#module.
    def enterModule(self, ctx:smvParser.ModuleContext):
        #print("~~~~")
        #print(ctx.getChild(1).getText())
        #print("~~~~")
        if ctx.getChildCount() == 2:
            return
        self.current_module_name = ctx.getChild(1).getText()
        self.var_dec_par_module[ctx.getChild(1).getText()] ={}
        self.var_dec = {}
        #print("-----")
        #for i in range(ctx.getChildCount()):
         #   print(ctx.getChild(i).getText())
        #else:
        #    print("~~~~~")
        pass
    # Exit a parse tree produced by smvParser#module.
    def exitModule(self, ctx:smvParser.ModuleContext):
        if ctx.getChildCount() == 2:
            return
        self.var_dec_par_module[self.current_module_name] = self.var_dec
        
        pass


    # Enter a parse tree produced by smvParser#module_parameters.
    def enterModule_parameters(self, ctx:smvParser.Module_parametersContext):
        
        pass

    # Exit a parse tree produced by smvParser#module_parameters.
    def exitModule_parameters(self, ctx:smvParser.Module_parametersContext):
        pass


    # Enter a parse tree produced by smvParser#module_body.
    def enterModule_body(self, ctx:smvParser.Module_bodyContext):
        pass

    # Exit a parse tree produced by smvParser#module_body.
    def exitModule_body(self, ctx:smvParser.Module_bodyContext):
        pass


    # Enter a parse tree produced by smvParser#module_element.
    def enterModule_element(self, ctx:smvParser.Module_elementContext):
        pass

    # Exit a parse tree produced by smvParser#module_element.
    def exitModule_element(self, ctx:smvParser.Module_elementContext):
        pass


    # Enter a parse tree produced by smvParser#isa_declaration.
    def enterIsa_declaration(self, ctx:smvParser.Isa_declarationContext):
        pass

    # Exit a parse tree produced by smvParser#isa_declaration.
    def exitIsa_declaration(self, ctx:smvParser.Isa_declarationContext):
        pass


    # Enter a parse tree produced by smvParser#ctl_specification.
    def enterCtl_specification(self, ctx:smvParser.Ctl_specificationContext):
        self.enter_ctl_specification_flag = True
        pass

    # Exit a parse tree produced by smvParser#ctl_specification.
    def exitCtl_specification(self, ctx:smvParser.Ctl_specificationContext):
        self.enter_ctl_specification_flag = False
        pass


    # Enter a parse tree produced by smvParser#ctl_expr.
    def enterCtl_expr(self, ctx:smvParser.Ctl_exprContext):
        print("-----")
        for i in range(ctx.getChildCount()):
            print(ctx.getChild(i).getText())

        if ctx.getChild(0).getText() in ["AF", "AG", "AX","EF", "EG", "EX"]:
            self.ctl_depth += 1
            self.ctl_ope_li.append(ctx.getChild(0).getText())
        elif ctx.getChildCount() >1 and ctx.getChild(1).getText()in ["U", "->","&","|"]:
            self.ctl_ope_li.append(ctx.getChild(1).getText())
        

    # Exit a parse tree produced by smvParser#ctl_expr.
    def exitCtl_expr(self, ctx:smvParser.Ctl_exprContext):
        

        
        if ctx.getChild(0).getText() in ["AF", "AG", "AX","EF", "EG", "EX"]:
            self.ctl_depth -= 1
            self.ctl_ope_li.pop(-1)
        elif ctx.getChildCount() >1 and ctx.getChild(1).getText()in ["U", "->","&","|"]:
            self.clt_ope_li.append(ctx.getChild(1).getText())

        if ctx.getChildCount() == 1:
            if ctx.getChild(0).getText().count("(") < 2:
                self.ctl_formulas.append(CTL_Formula_Data(self.ctl_depth, ctx.getChild(0).getText(),self.ctl_ope_li)) 
                if  self.ctl_ope_li[-1] in ["|", "&", "U"]:
                    self.ctl_ope_li.pop()


    # Enter a parse tree produced by smvParser#ltl_specification.
    def enterLtl_specification(self, ctx:smvParser.Ltl_specificationContext):
        self.enter_ltl_specification_flag = True
        #print("enterLTL", ctx.getChild(1).getText())
        #print(ctx.getChildCount())
        pass

    # Exit a parse tree produced by smvParser#ltl_specification.
    def exitLtl_specification(self, ctx:smvParser.Ltl_specificationContext):
        self.enter_ltl_specification_flag = False
        pass


    # Enter a parse tree produced by smvParser#ltl_expr.
    def enterLtl_expr(self, ctx:smvParser.Ltl_exprContext):
        if ctx.getChild(0).getText() in ["F", "G", "X"]:
            self.ltl_depth += 1
            self.ltl_ope_li.append(ctx.getChild(0).getText())
        elif ctx.getChildCount() >1 and ctx.getChild(1).getText()in ["U", "->","&","|"]:
            self.ltl_ope_li.append(ctx.getChild(1).getText())
        
        #for i in range(ctx.getChildCount()):
         #   print(ctx.getChild(i).getText())
        #print("~~~~~~~~~~~~~~~")
        
        if ctx.getChildCount() == 1:
            if ctx.getChild(0).getText().count("(") < 2:
                self.ltl_formulas.append(LTL_Formula_Data(self.ltl_depth, ctx.getChild(0).getText(),self.ltl_ope_li)) 
                if  self.ltl_ope_li[-1] in ["|", "&", "U"]:
                    self.ltl_ope_li.pop()

        
    
        
    # Exit a parse tree produced by smvParser#ltl_expr.
    def exitLtl_expr(self, ctx:smvParser.Ltl_exprContext):
        #if ctx.getChild(0).getText() == "F" or :
           # self.ltl_F_flag = False
        #elif ctx.getChild(0).getText() == "G":
         #   self.ltl_G_flag = False
        
        if ctx.getChild(0).getText() in ["F", "G", "X"]:
            self.ltl_depth -= 1
            self.ltl_ope_li.pop(-1)

            


