// Generated from smv.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link smvParser}.
 */
public interface smvListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link smvParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(smvParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(smvParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#define_identifier}.
	 * @param ctx the parse tree
	 */
	void enterDefine_identifier(smvParser.Define_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#define_identifier}.
	 * @param ctx the parse tree
	 */
	void exitDefine_identifier(smvParser.Define_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#variable_identifier}.
	 * @param ctx the parse tree
	 */
	void enterVariable_identifier(smvParser.Variable_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#variable_identifier}.
	 * @param ctx the parse tree
	 */
	void exitVariable_identifier(smvParser.Variable_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#complex_identifier}.
	 * @param ctx the parse tree
	 */
	void enterComplex_identifier(smvParser.Complex_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#complex_identifier}.
	 * @param ctx the parse tree
	 */
	void exitComplex_identifier(smvParser.Complex_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#integer_number}.
	 * @param ctx the parse tree
	 */
	void enterInteger_number(smvParser.Integer_numberContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#integer_number}.
	 * @param ctx the parse tree
	 */
	void exitInteger_number(smvParser.Integer_numberContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(smvParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(smvParser.ConstantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#boolean_constant}.
	 * @param ctx the parse tree
	 */
	void enterBoolean_constant(smvParser.Boolean_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#boolean_constant}.
	 * @param ctx the parse tree
	 */
	void exitBoolean_constant(smvParser.Boolean_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#integer_constant}.
	 * @param ctx the parse tree
	 */
	void enterInteger_constant(smvParser.Integer_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#integer_constant}.
	 * @param ctx the parse tree
	 */
	void exitInteger_constant(smvParser.Integer_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#symbolic_constant}.
	 * @param ctx the parse tree
	 */
	void enterSymbolic_constant(smvParser.Symbolic_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#symbolic_constant}.
	 * @param ctx the parse tree
	 */
	void exitSymbolic_constant(smvParser.Symbolic_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#word_constant}.
	 * @param ctx the parse tree
	 */
	void enterWord_constant(smvParser.Word_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#word_constant}.
	 * @param ctx the parse tree
	 */
	void exitWord_constant(smvParser.Word_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#word_width}.
	 * @param ctx the parse tree
	 */
	void enterWord_width(smvParser.Word_widthContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#word_width}.
	 * @param ctx the parse tree
	 */
	void exitWord_width(smvParser.Word_widthContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#word_value}.
	 * @param ctx the parse tree
	 */
	void enterWord_value(smvParser.Word_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#word_value}.
	 * @param ctx the parse tree
	 */
	void exitWord_value(smvParser.Word_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#range_constant}.
	 * @param ctx the parse tree
	 */
	void enterRange_constant(smvParser.Range_constantContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#range_constant}.
	 * @param ctx the parse tree
	 */
	void exitRange_constant(smvParser.Range_constantContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#basic_expr}.
	 * @param ctx the parse tree
	 */
	void enterBasic_expr(smvParser.Basic_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#basic_expr}.
	 * @param ctx the parse tree
	 */
	void exitBasic_expr(smvParser.Basic_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#basic_expr_list}.
	 * @param ctx the parse tree
	 */
	void enterBasic_expr_list(smvParser.Basic_expr_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#basic_expr_list}.
	 * @param ctx the parse tree
	 */
	void exitBasic_expr_list(smvParser.Basic_expr_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#set_body_expr}.
	 * @param ctx the parse tree
	 */
	void enterSet_body_expr(smvParser.Set_body_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#set_body_expr}.
	 * @param ctx the parse tree
	 */
	void exitSet_body_expr(smvParser.Set_body_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#case_expr}.
	 * @param ctx the parse tree
	 */
	void enterCase_expr(smvParser.Case_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#case_expr}.
	 * @param ctx the parse tree
	 */
	void exitCase_expr(smvParser.Case_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#case_body}.
	 * @param ctx the parse tree
	 */
	void enterCase_body(smvParser.Case_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#case_body}.
	 * @param ctx the parse tree
	 */
	void exitCase_body(smvParser.Case_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#simple_expr}.
	 * @param ctx the parse tree
	 */
	void enterSimple_expr(smvParser.Simple_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#simple_expr}.
	 * @param ctx the parse tree
	 */
	void exitSimple_expr(smvParser.Simple_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#next_expr}.
	 * @param ctx the parse tree
	 */
	void enterNext_expr(smvParser.Next_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#next_expr}.
	 * @param ctx the parse tree
	 */
	void exitNext_expr(smvParser.Next_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#type_specifier}.
	 * @param ctx the parse tree
	 */
	void enterType_specifier(smvParser.Type_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#type_specifier}.
	 * @param ctx the parse tree
	 */
	void exitType_specifier(smvParser.Type_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#simple_type_specifier}.
	 * @param ctx the parse tree
	 */
	void enterSimple_type_specifier(smvParser.Simple_type_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#simple_type_specifier}.
	 * @param ctx the parse tree
	 */
	void exitSimple_type_specifier(smvParser.Simple_type_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#enumeration_type_body}.
	 * @param ctx the parse tree
	 */
	void enterEnumeration_type_body(smvParser.Enumeration_type_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#enumeration_type_body}.
	 * @param ctx the parse tree
	 */
	void exitEnumeration_type_body(smvParser.Enumeration_type_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#enumeration_type_value}.
	 * @param ctx the parse tree
	 */
	void enterEnumeration_type_value(smvParser.Enumeration_type_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#enumeration_type_value}.
	 * @param ctx the parse tree
	 */
	void exitEnumeration_type_value(smvParser.Enumeration_type_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#module_type_specifier}.
	 * @param ctx the parse tree
	 */
	void enterModule_type_specifier(smvParser.Module_type_specifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#module_type_specifier}.
	 * @param ctx the parse tree
	 */
	void exitModule_type_specifier(smvParser.Module_type_specifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void enterParameter_list(smvParser.Parameter_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#parameter_list}.
	 * @param ctx the parse tree
	 */
	void exitParameter_list(smvParser.Parameter_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#var_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVar_declaration(smvParser.Var_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#var_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVar_declaration(smvParser.Var_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#ivar_declaration}.
	 * @param ctx the parse tree
	 */
	void enterIvar_declaration(smvParser.Ivar_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#ivar_declaration}.
	 * @param ctx the parse tree
	 */
	void exitIvar_declaration(smvParser.Ivar_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#frozenvar_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFrozenvar_declaration(smvParser.Frozenvar_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#frozenvar_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFrozenvar_declaration(smvParser.Frozenvar_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#var_list}.
	 * @param ctx the parse tree
	 */
	void enterVar_list(smvParser.Var_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#var_list}.
	 * @param ctx the parse tree
	 */
	void exitVar_list(smvParser.Var_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#simple_var_list}.
	 * @param ctx the parse tree
	 */
	void enterSimple_var_list(smvParser.Simple_var_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#simple_var_list}.
	 * @param ctx the parse tree
	 */
	void exitSimple_var_list(smvParser.Simple_var_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#define_declaration}.
	 * @param ctx the parse tree
	 */
	void enterDefine_declaration(smvParser.Define_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#define_declaration}.
	 * @param ctx the parse tree
	 */
	void exitDefine_declaration(smvParser.Define_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#define_body}.
	 * @param ctx the parse tree
	 */
	void enterDefine_body(smvParser.Define_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#define_body}.
	 * @param ctx the parse tree
	 */
	void exitDefine_body(smvParser.Define_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#constants_declaration}.
	 * @param ctx the parse tree
	 */
	void enterConstants_declaration(smvParser.Constants_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#constants_declaration}.
	 * @param ctx the parse tree
	 */
	void exitConstants_declaration(smvParser.Constants_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#constants_body}.
	 * @param ctx the parse tree
	 */
	void enterConstants_body(smvParser.Constants_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#constants_body}.
	 * @param ctx the parse tree
	 */
	void exitConstants_body(smvParser.Constants_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#assign_constraint}.
	 * @param ctx the parse tree
	 */
	void enterAssign_constraint(smvParser.Assign_constraintContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#assign_constraint}.
	 * @param ctx the parse tree
	 */
	void exitAssign_constraint(smvParser.Assign_constraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#assign_list}.
	 * @param ctx the parse tree
	 */
	void enterAssign_list(smvParser.Assign_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#assign_list}.
	 * @param ctx the parse tree
	 */
	void exitAssign_list(smvParser.Assign_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(smvParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(smvParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#trans_constraint}.
	 * @param ctx the parse tree
	 */
	void enterTrans_constraint(smvParser.Trans_constraintContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#trans_constraint}.
	 * @param ctx the parse tree
	 */
	void exitTrans_constraint(smvParser.Trans_constraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#init_constraint}.
	 * @param ctx the parse tree
	 */
	void enterInit_constraint(smvParser.Init_constraintContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#init_constraint}.
	 * @param ctx the parse tree
	 */
	void exitInit_constraint(smvParser.Init_constraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#invar_constraint}.
	 * @param ctx the parse tree
	 */
	void enterInvar_constraint(smvParser.Invar_constraintContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#invar_constraint}.
	 * @param ctx the parse tree
	 */
	void exitInvar_constraint(smvParser.Invar_constraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#fairness_constraint}.
	 * @param ctx the parse tree
	 */
	void enterFairness_constraint(smvParser.Fairness_constraintContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#fairness_constraint}.
	 * @param ctx the parse tree
	 */
	void exitFairness_constraint(smvParser.Fairness_constraintContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(smvParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(smvParser.ModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#module_parameters}.
	 * @param ctx the parse tree
	 */
	void enterModule_parameters(smvParser.Module_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#module_parameters}.
	 * @param ctx the parse tree
	 */
	void exitModule_parameters(smvParser.Module_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#module_body}.
	 * @param ctx the parse tree
	 */
	void enterModule_body(smvParser.Module_bodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#module_body}.
	 * @param ctx the parse tree
	 */
	void exitModule_body(smvParser.Module_bodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#module_element}.
	 * @param ctx the parse tree
	 */
	void enterModule_element(smvParser.Module_elementContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#module_element}.
	 * @param ctx the parse tree
	 */
	void exitModule_element(smvParser.Module_elementContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#isa_declaration}.
	 * @param ctx the parse tree
	 */
	void enterIsa_declaration(smvParser.Isa_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#isa_declaration}.
	 * @param ctx the parse tree
	 */
	void exitIsa_declaration(smvParser.Isa_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#ctl_specification}.
	 * @param ctx the parse tree
	 */
	void enterCtl_specification(smvParser.Ctl_specificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#ctl_specification}.
	 * @param ctx the parse tree
	 */
	void exitCtl_specification(smvParser.Ctl_specificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#ctl_expr}.
	 * @param ctx the parse tree
	 */
	void enterCtl_expr(smvParser.Ctl_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#ctl_expr}.
	 * @param ctx the parse tree
	 */
	void exitCtl_expr(smvParser.Ctl_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#ltl_specification}.
	 * @param ctx the parse tree
	 */
	void enterLtl_specification(smvParser.Ltl_specificationContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#ltl_specification}.
	 * @param ctx the parse tree
	 */
	void exitLtl_specification(smvParser.Ltl_specificationContext ctx);
	/**
	 * Enter a parse tree produced by {@link smvParser#ltl_expr}.
	 * @param ctx the parse tree
	 */
	void enterLtl_expr(smvParser.Ltl_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link smvParser#ltl_expr}.
	 * @param ctx the parse tree
	 */
	void exitLtl_expr(smvParser.Ltl_exprContext ctx);
}