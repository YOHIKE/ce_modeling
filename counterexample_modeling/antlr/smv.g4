grammar smv;

/* 
options{
    language = Python3;
}
*/
/*
*構文規則
 */
identifier: NODIGIT;


define_identifier : complex_identifier
                    ;

variable_identifier : complex_identifier
                    ;


complex_identifier : identifier 
                    | complex_identifier DOT identifier
                    | complex_identifier OSQU basic_expr CSQU
                    | SELF
                    ;

integer_number : MAINUS_DIGIT
                |DIGIT
                | integer_number DIGIT
                ;

constant: boolean_constant
        | integer_constant
        | symbolic_constant
        |word_constant
        |range_constant
        ;

boolean_constant: BOOLEAN;

integer_constant: integer_number;

symbolic_constant: identifier;

/* []の扱い */
word_constant : ZERO OSQU WORD_SIGN_SPECIFIER CSQU WORD_BASE OSQU word_width CSQU UNDER_BAR  word_value;
word_width:integer_number;

word_value: HEX_DIGIT
            | word_value HEX_DIGIT
            | word_value UNDER_BAR
            ;
range_constant:integer_number DOUBLE_DOT integer_number;

basic_expr : constant
            | variable_identifier
            | define_identifier
            | OPAR basic_expr CPAR
            | OSQU basic_expr_list CSQU
            | (SUR|ABS|MAINUS) basic_expr
            | (MAX|MIN) OPAR basic_expr COMMA basic_expr CPAR 
            |  basic_expr (AND | OR |XOR|XNOR|DOUBLE_COLON|UNION | IN | DOUBLE_DOT | RIGHT_SHIFT|LEFT_SHIFT
                MOD | MAINUS | PLUS | GREATER_EQUAL | GREATER | LESS | LESS_EQUAL | EQUAL | NOT_EQUAL) basic_expr
            /*indexの定義がわからない , index →basic_exprに変更*/
            |  basic_expr OSQU basic_expr CSQU
            /*いらない可能性あり 
            |  basic_expr '[' basic_expr ':' basic_expr ']'
            */
            | (WORDL|BOOL|TOINT) OPAR basic_expr CPAR 
            | CONST OPAR basic_expr_list CPAR 
            | (SWCONST| UWCONST | EXTEND | RESIZE) OPAR basic_expr COMMA basic_expr CPAR 
            | (SIGNED |UNSIGNED|SIZEOF ) OPAR basic_expr CPAR 
            | OCUR  set_body_expr CCUR 
            | case_expr
            | NEXT OPAR basic_expr CPAR
            ;


basic_expr_list:basic_expr  
                | basic_expr_list COMMA basic_expr 
                ;

set_body_expr : basic_expr
                | set_body_expr COMMA basic_expr
                ;

case_expr : CASE case_body ESAC ;

case_body : basic_expr COLON basic_expr SCOL
            | case_body basic_expr COLON basic_expr SCOL
            ;


next_expr:basic_expr;

type_specifier : simple_type_specifier 
                | module_type_specifier
                ;
    
simple_type_specifier: BOOLEAN_WORD
                    | (WORD | UNSIGNED_WORD | SIGNED_WORD )OSQU integer_number CSQU
                    | OCUR enumeration_type_body CCUR
                    | integer_number DOUBLE_DOT integer_number
                    | ARRAY integer_number DOUBLE_DOT integer_number OF simple_type_specifier
                    ;

enumeration_type_body: enumeration_type_value
                    | enumeration_type_body COMMA enumeration_type_value
                    ;

enumeration_type_value : symbolic_constant
                        | integer_number
                        ;

module_type_specifier: identifier (OPAR ( parameter_list)? CPAR )?
                    | PROCESS identifier OPAR (parameter_list)?  CPAR
                    ;

parameter_list : basic_expr 
                | parameter_list COMMA basic_expr
                ;
var_declaration : VAR var_list;

ivar_declaration : IVAR simple_var_list;

frozenvar_declaration : FROZENVAR simple_var_list;

var_list : identifier COLON type_specifier SCOL
        | var_list identifier COLON type_specifier SCOL;

simple_var_list: identifier COLON simple_type_specifier SCOL
                | simple_var_list identifier COLON simple_type_specifier SCOL
                ;
define_declaration : DEFINE define_body ;

define_body : identifier COLON EQUAL basic_expr SCOL
            | define_body identifier COLON EQUAL basic_expr SCOL
            ;

constants_declaration : CONSTANTS constants_body SCOL
                        ;
constants_body: identifier      
                | constants_body COMMA identifier
                ;

assign_constraint : ASSIGN assign_list;

assign_list : assign SCOL
            | assign_list assign SCOL
            ;
assign : complex_identifier COLON EQUAL basic_expr
        | INIT OPAR complex_identifier CPAR COLON EQUAL basic_expr
        | NEXT OPAR complex_identifier CPAR COLON EQUAL next_expr
        ;
simple_expr : basic_expr;

/*;の扱い */
trans_constraint : TRANS_CONST  next_expr SCOL;

init_constraint : INIT_CONST basic_expr SCOL;

invar_constraint : INVAR_CONST basic_expr SCOL;

fairness_constraint: (FAIRNESS_CONST | JUSTICE_CONST)basic_expr SCOL?
                    | COMPASSION_CONST OPAR basic_expr COMMA basic_expr CPAR SCOL?
                    ;

module : MODULE identifier (OPAR module_parameters? CPAR)?  module_body
        |module module;

module_parameters: identifier   
                | module_parameters COMMA identifier
                ;

module_body: module_element 
            | module_body module_element (LESS EOF GREATER)?
            ;

module_element : var_declaration
                | ivar_declaration
                | frozenvar_declaration
                | define_declaration
                | constants_declaration
                | assign_constraint
                | trans_constraint
                | init_constraint
                | invar_constraint
                | fairness_constraint
                | ctl_specification
                /* 
                | invar_specification
                */
                | ltl_specification
                /* 
                | compute_specification
                */
                | isa_declaration
                ;

isa_declaration: ISA identifier;

ctl_specification : SPEC ctl_expr SCOL?
                    ;

ctl_expr : basic_expr
        | OPAR ctl_expr CPAR
        | SUR ctl_expr
        | ctl_expr (AND | OR | XOR | XNOR | ARROW |DOUBLE_ARROW) ctl_expr
        | CTL_TEMPORAL_OPE ctl_expr
        | CTL_TEMPORAL_OPE2 OSQU ctl_expr UNTIL ctl_expr CSQU
        ;

ltl_specification: LTL_SPEC  ltl_expr SCOL?;
                
ltl_expr : basic_expr  
        | OPAR ltl_expr CPAR
        | SUR ltl_expr
        | ltl_expr (LTL_RELATIONAL_OPERATOR|AND|OR|XNOR|XOR|ARROW|DOUBLE_ARROW) ltl_expr
        | LTL_TEMPORAL_OPE ltl_expr
        ;


 /*
*字句規則
 */
COMMENT:'--' ~('\r' | '\n')* { skip(); }
    ;
WHITESPASE: ('\n'|'\r'|'\t'|' ')+ -> skip;
DIGIT : '1'..'9' | ZERO;
ZERO : '0';
MAINUS:'-';
MAINUS_DIGIT: '-''0'..'9';
BOOLEAN : ('TRUE' | 'FALSE');
IDENTIFIER_WORD : ('$' | '#' | '-' );
CTL_TEMPORAL_OPE : 'EG'|'EX'|'EF'|'AG'|'AX'|'AF';
CTL_TEMPORAL_OPE2:'E'|'A';
LTL_RELATIONAL_OPERATOR:'U'|'V'|'S'|'T';
LTL_TEMPORAL_OPE:'Y'|'Z'|'H'|'O'|'X'|'G'|'F';
UNTIL:'U';
SPEC:'SPEC';
SCOL : ';';
OPAR:'(';
CPAR:')';
OCUR:'{';
CCUR:'}';
OSQU:'[';
CSQU:']';
WORDL: 'wordl';
BOOL:'bool';
TOINT:'toint';
CONST:'const';
COMMA:',';
COLON:':';
QUE:'?';
AND:'&';
OR:'|';
XOR:'xor';
XNOR:'xnor';
ARROW:'->';
DOUBLE_ARROW:'<->';
EQUAL:'=';
NOT_EQUAL:'!=';
LESS_EQUAL:'<=';
LESS:'<';
GREATER:'>';
GREATER_EQUAL:'>=';
PLUS:'+';

MOD:'mod';
MAX:'max';
MIN:'min';
RIGHT_SHIFT:'>>';
LEFT_SHIFT:'<<';
DOUBLE_COLON:'::';
SWCONST:'swconst';
UWCONST:'uwconst';
SIGNED:'signed';
SIZEOF:'sizeof';
UNSIGNED:'unsigned';
EXTEND:'extend';
RESIZE:'resize';
UNION:'union';
IN:' in ';
DOUBLE_DOT:'..';
SUR:'!';
ABS:'abs';
UNDER_BAR:'_';
DOT:'.';
SELF: 'self';
CASE:'case';
ESAC:'esac';
ISA:'ISA';
BOOLEAN_WORD:'boolean';
WORD:'word';
UNSIGNED_WORD:'unsigned word';
SIGNED_WORD:'signed word';
ARRAY:'array';
OF:' of ';
PROCESS:'process';
VAR:'VAR';
IVAR:'IVAR';
FROZENVAR:'FROZENVAR';
DEFINE:'DEFINE';
CONSTANTS:'CONSTANTS';
ASSIGN:'ASSIGN';
INIT:'init';
NEXT:'next';
TRANS_CONST:'TRANS';
INIT_CONST:'INIT';
INVAR_CONST:'INVAR';
FAIRNESS_CONST:'FAIRNESS';
JUSTICE_CONST:'JUSTICE';
COMPASSION_CONST:'COMPASSION';
MODULE:'MODULE';
LTL_SPEC:'LTLSPEC';
SPACE:' ';
NODIGIT : [a-zA-Z_] [a-zA-Z_0-9]*;
WORD_BASE:'b'|'B'|'o'|'O'|'d'|'D'|'h'|'H';
WORD_SIGN_SPECIFIER: 'u'|'s';
HEX_DIGIT:'0'..'9'|'a'..'f'|'A'..'F';