
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSINCLUDE USING NAMESPACE STD COUT CIN GET CADENA RETURN VOID INT ENDL IDENTIFICADOR ENTERO ASIGNAR SUMA RESTA MULT DIV POTENCIA MODULO MINUSMINUS PLUSPLUS SI SINO MIENTRAS PARA AND OR NOT MENORQUE MENORIGUAL MAYORQUE MAYORIGUAL IGUAL DISTINTO NUMERAL PARIZQ PARDER CORIZQ CORDER LLAIZQ LLADER PUNTOCOMA COMA COMDOB MAYORDER MAYORIZQdeclaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion\n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    expresion : ENTEROexpresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR'
    
_lr_action_items = {'ENTERO':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,66,67,68,69,70,71,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'MODULO':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,17,-33,-33,17,17,-9,17,17,-10,-12,17,-5,17,17,-4,17,-3,17,17,17,17,17,17,-6,17,-32,-11,17,17,17,17,-30,-29,-28,17,17,17,17,17,17,-24,-21,-20,-23,-19,-22,]),'MULT':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,15,-33,-33,15,15,-9,15,15,-10,-12,15,-5,15,15,15,15,15,15,15,15,15,15,15,-6,15,-32,-11,15,15,15,15,-30,-29,-28,15,15,15,15,15,15,-24,-21,-20,-23,-19,-22,]),'RESTA':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[3,3,3,3,-31,18,3,3,-33,-33,18,18,-9,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,18,18,3,3,-10,3,3,-12,18,-5,18,18,-4,18,-3,18,18,18,18,18,18,-6,18,-32,-11,18,18,18,18,-30,3,3,3,3,3,3,-29,-28,18,18,18,18,18,18,-24,-21,-20,-23,-19,-22,]),'MAYORQUE':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,19,-33,-33,19,19,-9,19,19,58,-12,19,-5,19,19,-4,19,-3,19,19,19,19,19,19,-6,19,-32,-11,19,19,19,19,-30,-29,-28,19,19,19,19,19,19,-24,-21,-20,-23,-19,-22,]),'IGUAL':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,16,-33,-33,16,16,-9,16,16,59,-12,16,-5,16,16,-4,16,-3,16,16,16,16,16,16,-6,16,-32,-11,16,16,16,16,-30,-29,-28,16,16,16,16,16,16,-24,-21,-20,-23,-19,-22,]),'POTENCIA':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,22,-33,-33,22,22,-9,22,22,-10,-12,22,-5,22,22,-4,22,-3,22,22,22,22,22,22,-6,22,-32,-11,22,22,22,22,-30,-29,-28,22,22,22,22,22,22,-24,-21,-20,-23,-19,-22,]),'PARIZQ':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,56,57,58,59,60,61,66,67,68,69,70,71,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,66,67,68,69,70,71,1,1,1,1,1,1,]),'MENORIGUAL':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,25,-33,-33,25,25,-9,25,25,57,-12,25,-5,25,25,-4,25,-3,25,25,25,25,25,25,-6,25,-32,-11,25,25,25,25,-30,-29,-28,25,25,25,25,25,25,-24,-21,-20,-23,-19,-22,]),'$end':([4,5,7,9,10,13,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,72,73,80,81,82,83,84,85,],[-31,-2,0,-33,-33,-9,-10,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,-1,-30,-29,-28,-24,-21,-20,-23,-19,-22,]),'COMDOB':([0,1,2,3,4,6,8,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,65,66,67,68,69,70,71,72,73,80,81,82,83,84,85,],[6,6,6,6,-31,6,6,-33,-9,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,52,6,6,-10,6,6,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,-30,6,6,6,6,6,6,-29,-28,-24,-21,-20,-23,-19,-22,]),'AND':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,26,-33,-33,35,26,-9,26,26,-10,-12,26,-5,26,26,-4,26,-3,26,26,26,26,26,26,-6,26,-32,-11,26,26,26,26,-30,-29,-28,26,26,26,26,26,26,-24,-21,-20,-23,-19,-22,]),'SUMA':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,20,-33,-33,20,20,-9,20,20,-10,-12,20,-5,20,20,-4,20,-3,20,20,20,20,20,20,-6,20,-32,-11,20,20,20,20,-30,-29,-28,20,20,20,20,20,20,-24,-21,-20,-23,-19,-22,]),'LLADER':([4,10,13,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,65,72,73,80,81,82,83,84,85,],[-31,-33,-9,53,-10,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,-30,-29,-28,-24,-21,-20,-23,-19,-22,]),'CORIZQ':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,66,67,68,69,70,71,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'DIV':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,27,-33,-33,27,27,-9,27,27,-10,-12,27,-5,27,27,27,27,27,27,27,27,27,27,27,-6,27,-32,-11,27,27,27,27,-30,-29,-28,27,27,27,27,27,27,-24,-21,-20,-23,-19,-22,]),'PARDER':([4,10,11,13,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,-33,33,-9,-10,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,65,72,73,-30,-29,-28,80,81,82,83,84,85,-24,-21,-20,-23,-19,-22,]),'NOT':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,14,-33,-33,32,14,-9,14,14,-10,-12,14,-5,14,14,-4,14,-3,14,14,14,14,14,14,-6,14,-32,-11,14,14,14,14,-30,-29,-28,14,14,14,14,14,14,-24,-21,-20,-23,-19,-22,]),'MENORQUE':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,21,-33,-33,21,21,-9,21,21,60,-12,21,-5,21,21,-4,21,-3,21,21,21,21,21,21,-6,21,-32,-11,21,21,21,21,-30,-29,-28,21,21,21,21,21,21,-24,-21,-20,-23,-19,-22,]),'ASIGNAR':([9,],[31,]),'OR':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,23,-33,-33,34,23,-9,23,23,-10,-12,23,-5,23,23,-4,23,-3,23,23,23,23,23,23,-6,23,-32,-11,23,23,23,23,-30,-29,-28,23,23,23,23,23,23,-24,-21,-20,-23,-19,-22,]),'DISTINTO':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,24,-33,-33,24,24,-9,24,24,56,-12,24,-5,24,24,-4,24,-3,24,24,24,24,24,24,-6,24,-32,-11,24,24,24,24,-30,-29,-28,24,24,24,24,24,24,-24,-21,-20,-23,-19,-22,]),'CORDER':([4,10,12,13,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,65,72,73,80,81,82,83,84,85,],[-31,-33,36,-9,-10,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,-30,-29,-28,-24,-21,-20,-23,-19,-22,]),'LLAIZQ':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,66,67,68,69,70,71,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'IDENTIFICADOR':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,66,67,68,69,70,71,],[9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'PUNTOCOMA':([4,10,13,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,65,72,73,80,81,82,83,84,85,],[-31,-33,-9,-10,-12,-27,-5,-17,-8,-4,-14,-3,-13,-7,-26,-18,-15,-25,-6,-16,-32,-11,64,-30,-29,-28,-24,-21,-20,-23,-19,-22,]),'MAYORIGUAL':([4,5,9,10,11,12,13,29,30,33,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,62,63,65,72,73,74,75,76,77,78,79,80,81,82,83,84,85,],[-31,28,-33,-33,28,28,-9,28,28,61,-12,28,-5,28,28,-4,28,-3,28,28,28,28,28,28,-6,28,-32,-11,28,28,28,28,-30,-29,-28,28,28,28,28,28,28,-24,-21,-20,-23,-19,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,1,2,3,6,8,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,66,67,68,69,70,71,],[5,11,12,13,29,30,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,62,63,74,75,76,77,78,79,]),'declaracion':([0,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','analizador_sintactico.py',17),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',21),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',27),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',28),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',29),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',30),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',31),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',32),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizador_sintactico.py',53),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',58),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',59),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',60),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',66),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',67),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',68),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',69),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',70),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',71),
  ('expresion -> PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',72),
  ('expresion -> PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',73),
  ('expresion -> PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',74),
  ('expresion -> PARIZQ expresion PARDER MAYORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',75),
  ('expresion -> PARIZQ expresion PARDER IGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',76),
  ('expresion -> PARIZQ expresion PARDER DISTINTO PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',77),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',103),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',104),
  ('expresion -> expresion NOT expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',105),
  ('expresion -> PARIZQ expresion AND expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',106),
  ('expresion -> PARIZQ expresion OR expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',107),
  ('expresion -> PARIZQ expresion NOT expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',108),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizador_sintactico.py',126),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','analizador_sintactico.py',130),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizador_sintactico.py',134),
]