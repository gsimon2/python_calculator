#!/usr/bin/env python 

import ply.yacc as yacc
from lexer_calc import tokens
import sys

# Set precedence for operations
#	Define low to high prioty
#	Left or right associativity
precedence = (
	('left', '+', '-'),
	('left', '*', '/'),
	('right', 'U_MINUS')
)
 
def p_start(p):
	"start : expr"
	p[0] = p[1]
	return p[0]
 
def p_add(p):
	"expr : expr '+' expr"
	p[0] = p[1] + p[3]
 
def p_sub(p):
	"expr : expr '-' expr"
	p[0] = p[1] - p[3]
 
def p_u_minus(p):
	"expr : '-' expr %prec U_MINUS"
	p[0] = -1 * p[2]
 
def p_mult(p):
	"expr : expr '*' expr"
	p[0] = p[1] * p[3]
 
def p_div(p):
	"expr : expr '/' expr"
	if p[3] == 0:
		exit(1)
	p[0] = p[1] / p[3]
 
def p_para(p):
	"expr : '(' expr ')'"
	p[0] = p[2]
 
def p_number(p):
	"expr : NUMBER"
	p[0] = p[1]
 
def p_error(p):
	print('Parsing Error!')
	sys.exit(1)
 
 
class calc_parser():
	def __init__(self):
		self.parser = yacc.yacc()
		
	def parse_input(self, _input):
		return self.parser.parse(_input)
		

if __name__ == "__main__":
	source = sys.stdin.readline()
	calc = calc_parser()
	value = calc.parse_input(source)
	print('The answer is: {}'.format(value))
	
