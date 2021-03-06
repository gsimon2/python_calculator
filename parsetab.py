
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightU_MINUSNUMBERstart : exprexpr : expr '+' exprexpr : expr '-' exprexpr : '-' expr %prec U_MINUSexpr : expr '*' exprexpr : expr '/' exprexpr : '(' expr ')'expr : NUMBER"
    
_lr_action_items = {')':([3,10,11,12,13,14,15,16,],[-8,-4,16,-2,-5,-3,-6,-7,]),'(':([0,2,5,6,7,8,9,],[5,5,5,5,5,5,5,]),'+':([1,3,10,11,12,13,14,15,16,],[6,-8,-4,6,-2,-5,-3,-6,-7,]),'*':([1,3,10,11,12,13,14,15,16,],[7,-8,-4,7,7,-5,7,-6,-7,]),'-':([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,],[2,8,2,-8,2,2,2,2,2,-4,8,-2,-5,-3,-6,-7,]),'NUMBER':([0,2,5,6,7,8,9,],[3,3,3,3,3,3,3,]),'/':([1,3,10,11,12,13,14,15,16,],[9,-8,-4,9,9,-5,9,-6,-7,]),'$end':([1,3,4,10,12,13,14,15,16,],[-1,-8,0,-4,-2,-5,-3,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[4,]),'expr':([0,2,5,6,7,8,9,],[1,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> expr','start',1,'p_start','parser_calc.py',11),
  ('expr -> expr + expr','expr',3,'p_add','parser_calc.py',15),
  ('expr -> expr - expr','expr',3,'p_sub','parser_calc.py',19),
  ('expr -> - expr','expr',2,'p_u_minus','parser_calc.py',23),
  ('expr -> expr * expr','expr',3,'p_mult','parser_calc.py',27),
  ('expr -> expr / expr','expr',3,'p_div','parser_calc.py',31),
  ('expr -> ( expr )','expr',3,'p_para','parser_calc.py',37),
  ('expr -> NUMBER','expr',1,'p_number','parser_calc.py',41),
]
