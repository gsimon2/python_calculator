#!/usr/bin/env python 

import sys
import ply.lex as lex
 
tokens = ["NUMBER"]
 
def t_NUMBER(t):
	r"[0-9]+"
	t.value = int(t.value)
	return t
 
def t_WHITESPACE(t):
	r"[\n\t ]"
	pass
 
literals = ['+', '-', '*', '/', '(', ')']
 
def t_error(t):
	print('Undefined token translation!')
	sys.exit(1)
 
lexer = lex.lex()
