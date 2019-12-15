
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'startAND COMMA DELETE EE EQ FROM GE GROUPBY GT IDENTIFIER INSERT INTO LE LPAREN LT NE NEWLINE NOT NUMBER OR ORDERBY QUOTED_IDENTIFIER RPAREN SELECT SET STAR UPDATE USE VALUES WHEREstart : SELECT select_statement\n    | UPDATE update_statement\n    | DELETE delete_statement\n    | INSERT insert_statement\n    | USE use_statementuse_statement : IDENTIFIERselect_statement : args FROM IDENTIFIER \n    | args FROM IDENTIFIER WHERE where_clause\n    | args FROM IDENTIFIER WHERE where_clause GROUPBY IDENTIFIER ORDERBY order_list\n    | args FROM IDENTIFIER WHERE where_clause GROUPBY IDENTIFIER\n    | args FROM IDENTIFIER WHERE where_clause ORDERBY order_list\n    | args FROM IDENTIFIER GROUPBY IDENTIFIER ORDERBY order_list\n    | args FROM IDENTIFIER ORDERBY order_listupdate_statement : IDENTIFIER SET update_list WHERE where_clausedelete_statement : FROM IDENTIFIER WHERE where_clauseinsert_statement : INTO IDENTIFIER LPAREN column_list RPAREN VALUES LPAREN value_list RPARENargs : STAR\n    | arg_listwhere_clause : term \n    | term OR termterm : factor \n    | factor AND factorfactor : condition\n    | NOT factor\n    | LPAREN where_clause RPARENcondition : IDENTIFIER operators IDENTIFIER\n    | IDENTIFIER operators NUMBERupdate_list : update_list COMMA update_expression\n    | update_expressioncolumn_list : column_list COMMA IDENTIFIER\n    | IDENTIFIERvalue_list : value_list COMMA NUMBER\n    | value_list COMMA IDENTIFIER\n    | NUMBER\n    | IDENTIFIERupdate_expression : IDENTIFIER EQ NUMBER\n    | IDENTIFIER EQ IDENTIFIERarg_list : arg_list COMMA IDENTIFIER\n    | IDENTIFIERorder_list : order_list COMMA IDENTIFIER\n    | IDENTIFIERoperators : EE\n    | EQ\n    | NE\n    | LT\n    | LE\n    | GT\n    | GE'
    
_lr_action_items = {'SELECT':([0,],[2,]),'UPDATE':([0,],[3,]),'DELETE':([0,],[4,]),'INSERT':([0,],[5,]),'USE':([0,],[6,]),'$end':([1,7,12,14,16,18,19,25,39,40,41,42,47,49,50,53,65,73,74,75,76,77,80,81,82,83,89,90,],[0,-1,-2,-3,-4,-5,-6,-7,-15,-19,-21,-23,-8,-41,-13,-14,-24,-26,-27,-20,-22,-25,-10,-11,-12,-40,-9,-16,]),'STAR':([2,],[10,]),'IDENTIFIER':([2,3,6,15,17,20,21,22,30,31,32,33,34,35,36,37,43,44,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,84,85,91,],[9,13,19,23,24,25,26,27,38,45,38,48,49,51,38,27,38,38,73,-42,-43,-44,-45,-46,-47,-48,38,38,79,80,49,49,83,86,49,93,]),'FROM':([4,8,9,10,11,26,],[15,20,-39,-17,-18,-38,]),'INTO':([5,],[17,]),'COMMA':([9,11,26,28,29,45,46,49,50,51,52,54,79,81,82,83,86,87,88,89,92,93,],[-39,21,-38,37,-29,-31,68,-41,72,-37,-36,-28,-30,72,72,-40,-35,91,-34,72,-32,-33,]),'SET':([13,],[22,]),'WHERE':([23,25,28,29,51,52,54,],[30,32,36,-29,-37,-36,-28,]),'LPAREN':([24,30,32,36,43,44,63,64,78,],[31,44,44,44,44,44,44,44,84,]),'GROUPBY':([25,40,41,42,47,65,73,74,75,76,77,],[33,-19,-21,-23,69,-24,-26,-27,-20,-22,-25,]),'ORDERBY':([25,40,41,42,47,48,65,73,74,75,76,77,80,],[34,-19,-21,-23,70,71,-24,-26,-27,-20,-22,-25,85,]),'EQ':([27,38,],[35,57,]),'NOT':([30,32,36,43,44,63,64,],[43,43,43,43,43,43,43,]),'NUMBER':([35,55,56,57,58,59,60,61,62,84,91,],[52,74,-42,-43,-44,-45,-46,-47,-48,88,92,]),'EE':([38,],[56,]),'NE':([38,],[58,]),'LT':([38,],[59,]),'LE':([38,],[60,]),'GT':([38,],[61,]),'GE':([38,],[62,]),'RPAREN':([40,41,42,45,46,65,66,73,74,75,76,77,79,86,87,88,92,93,],[-19,-21,-23,-31,67,-24,77,-26,-27,-20,-22,-25,-30,-35,90,-34,-32,-33,]),'OR':([40,41,42,65,73,74,76,77,],[63,-21,-23,-24,-26,-27,-22,-25,]),'AND':([41,42,65,73,74,77,],[64,-23,-24,-26,-27,-25,]),'VALUES':([67,],[78,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'select_statement':([2,],[7,]),'args':([2,],[8,]),'arg_list':([2,],[11,]),'update_statement':([3,],[12,]),'delete_statement':([4,],[14,]),'insert_statement':([5,],[16,]),'use_statement':([6,],[18,]),'update_list':([22,],[28,]),'update_expression':([22,37,],[29,54,]),'where_clause':([30,32,36,44,],[39,47,53,66,]),'term':([30,32,36,44,63,],[40,40,40,40,75,]),'factor':([30,32,36,43,44,63,64,],[41,41,41,65,41,41,76,]),'condition':([30,32,36,43,44,63,64,],[42,42,42,42,42,42,42,]),'column_list':([31,],[46,]),'order_list':([34,70,71,85,],[50,81,82,89,]),'operators':([38,],[55,]),'value_list':([84,],[87,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> SELECT select_statement','start',2,'p_start','yacc1.py',48),
  ('start -> UPDATE update_statement','start',2,'p_start','yacc1.py',49),
  ('start -> DELETE delete_statement','start',2,'p_start','yacc1.py',50),
  ('start -> INSERT insert_statement','start',2,'p_start','yacc1.py',51),
  ('start -> USE use_statement','start',2,'p_start','yacc1.py',52),
  ('use_statement -> IDENTIFIER','use_statement',1,'p_use_statement','yacc1.py',56),
  ('select_statement -> args FROM IDENTIFIER','select_statement',3,'p_select_statement','yacc1.py',61),
  ('select_statement -> args FROM IDENTIFIER WHERE where_clause','select_statement',5,'p_select_statement','yacc1.py',62),
  ('select_statement -> args FROM IDENTIFIER WHERE where_clause GROUPBY IDENTIFIER ORDERBY order_list','select_statement',9,'p_select_statement','yacc1.py',63),
  ('select_statement -> args FROM IDENTIFIER WHERE where_clause GROUPBY IDENTIFIER','select_statement',7,'p_select_statement','yacc1.py',64),
  ('select_statement -> args FROM IDENTIFIER WHERE where_clause ORDERBY order_list','select_statement',7,'p_select_statement','yacc1.py',65),
  ('select_statement -> args FROM IDENTIFIER GROUPBY IDENTIFIER ORDERBY order_list','select_statement',7,'p_select_statement','yacc1.py',66),
  ('select_statement -> args FROM IDENTIFIER ORDERBY order_list','select_statement',5,'p_select_statement','yacc1.py',67),
  ('update_statement -> IDENTIFIER SET update_list WHERE where_clause','update_statement',5,'p_update_statement','yacc1.py',78),
  ('delete_statement -> FROM IDENTIFIER WHERE where_clause','delete_statement',4,'p_delete_statement','yacc1.py',83),
  ('insert_statement -> INTO IDENTIFIER LPAREN column_list RPAREN VALUES LPAREN value_list RPAREN','insert_statement',9,'p_insert_statement','yacc1.py',88),
  ('args -> STAR','args',1,'p_args','yacc1.py',93),
  ('args -> arg_list','args',1,'p_args','yacc1.py',94),
  ('where_clause -> term','where_clause',1,'p_where_clause','yacc1.py',98),
  ('where_clause -> term OR term','where_clause',3,'p_where_clause','yacc1.py',99),
  ('term -> factor','term',1,'p_term','yacc1.py',109),
  ('term -> factor AND factor','term',3,'p_term','yacc1.py',110),
  ('factor -> condition','factor',1,'p_factor','yacc1.py',118),
  ('factor -> NOT factor','factor',2,'p_factor','yacc1.py',119),
  ('factor -> LPAREN where_clause RPAREN','factor',3,'p_factor','yacc1.py',120),
  ('condition -> IDENTIFIER operators IDENTIFIER','condition',3,'p_condition','yacc1.py',130),
  ('condition -> IDENTIFIER operators NUMBER','condition',3,'p_condition','yacc1.py',131),
  ('update_list -> update_list COMMA update_expression','update_list',3,'p_update_list','yacc1.py',137),
  ('update_list -> update_expression','update_list',1,'p_update_list','yacc1.py',138),
  ('column_list -> column_list COMMA IDENTIFIER','column_list',3,'p_column_list','yacc1.py',142),
  ('column_list -> IDENTIFIER','column_list',1,'p_column_list','yacc1.py',143),
  ('value_list -> value_list COMMA NUMBER','value_list',3,'p_value_list','yacc1.py',150),
  ('value_list -> value_list COMMA IDENTIFIER','value_list',3,'p_value_list','yacc1.py',151),
  ('value_list -> NUMBER','value_list',1,'p_value_list','yacc1.py',152),
  ('value_list -> IDENTIFIER','value_list',1,'p_value_list','yacc1.py',153),
  ('update_expression -> IDENTIFIER EQ NUMBER','update_expression',3,'p_update_expression','yacc1.py',160),
  ('update_expression -> IDENTIFIER EQ IDENTIFIER','update_expression',3,'p_update_expression','yacc1.py',161),
  ('arg_list -> arg_list COMMA IDENTIFIER','arg_list',3,'p_arg_list','yacc1.py',168),
  ('arg_list -> IDENTIFIER','arg_list',1,'p_arg_list','yacc1.py',169),
  ('order_list -> order_list COMMA IDENTIFIER','order_list',3,'p_order_list','yacc1.py',176),
  ('order_list -> IDENTIFIER','order_list',1,'p_order_list','yacc1.py',177),
  ('operators -> EE','operators',1,'p_operators','yacc1.py',184),
  ('operators -> EQ','operators',1,'p_operators','yacc1.py',185),
  ('operators -> NE','operators',1,'p_operators','yacc1.py',186),
  ('operators -> LT','operators',1,'p_operators','yacc1.py',187),
  ('operators -> LE','operators',1,'p_operators','yacc1.py',188),
  ('operators -> GT','operators',1,'p_operators','yacc1.py',189),
  ('operators -> GE','operators',1,'p_operators','yacc1.py',190),
]
