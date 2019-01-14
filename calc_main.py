#!/usr/bin/env python 

import sys
from parser_calc import calc_parser
from tkinter import Tk, Label, Button, Entry, END


class calculator():
	
	def __init__(self, root_window):
		self.parser = calc_parser()
		self.root_window = root_window
		self.build_layout()
 
	def solve(self, _input):
		return self.parser.parse_input(_input)

	def build_layout(self):
		self.root_window.title("Calculator")
		
		# Number buttons
		self.button_0 = Button(self.root_window, text = "0", command = lambda : self.button_press_event(button = 0))
		self.button_0.grid(row=6, column = 2)
		self.button_1 = Button(self.root_window, text = "1", command = lambda : self.button_press_event(button = 1))
		self.button_1.grid(row=5, column = 1)
		self.button_2 = Button(self.root_window, text = "2", command = lambda : self.button_press_event(button = 2))
		self.button_2.grid(row=5, column = 2)
		self.button_3 = Button(self.root_window, text = "3", command = lambda : self.button_press_event(button = 3))
		self.button_3.grid(row=5, column = 3)
		self.button_4 = Button(self.root_window, text = "4", command = lambda : self.button_press_event(button = 4))
		self.button_4.grid(row=4, column = 1)
		self.button_5 = Button(self.root_window, text = "5", command = lambda : self.button_press_event(button = 5))
		self.button_5.grid(row=4, column = 2)
		self.button_6 = Button(self.root_window, text = "6", command = lambda : self.button_press_event(button = 6))
		self.button_6.grid(row=4, column = 3)
		self.button_7 = Button(self.root_window, text = "7", command = lambda : self.button_press_event(button = 7))
		self.button_7.grid(row=3, column = 1)
		self.button_8 = Button(self.root_window, text = "8", command = lambda : self.button_press_event(button = 8))
		self.button_8.grid(row=3, column = 2)
		self.button_9 = Button(self.root_window, text = "9", command = lambda : self.button_press_event(button = 9))
		self.button_9.grid(row=3, column = 3)
		
		# Math operator buttons
		self.button_add = Button(self.root_window, text = "+", command = lambda : self.button_press_event(button = '+'))
		self.button_add.grid(row=3, column = 5)
		self.button_sub = Button(self.root_window, text = "-", command = lambda : self.button_press_event(button = '-'))
		self.button_sub.grid(row=3, column = 6)
		self.button_mult = Button(self.root_window, text = "*", command = lambda : self.button_press_event(button = '*'))
		self.button_mult.grid(row=4, column = 5)
		self.button_divide = Button(self.root_window, text = "/", command = lambda : self.button_press_event(button = '/'))
		self.button_divide.grid(row=4, column = 6)
		self.button_left_para = Button(self.root_window, text = "(", command = lambda : self.button_press_event(button = '('))
		self.button_left_para.grid(row=5, column = 5)
		self.button_right_para = Button(self.root_window, text = ")", command = lambda : self.button_press_event(button = ')'))
		self.button_right_para.grid(row=5, column = 6)
		
		# Clear and enter buttons
		self.button_clear = Button(self.root_window, text = "clear", command = lambda : self.button_press_event(button = 'clear'))
		self.button_clear.grid(row=7, column = 0, columnspan=4)
		self.button_enter = Button(self.root_window, text = "enter", command = lambda : self.button_press_event(button = 'enter'))
		self.button_enter.grid(row=7, column = 3, columnspan=4)
		
		
		# Text box entry
		self.text_box = Entry(self.root_window, justify="right")
		self.text_box.grid(row=1, columnspan=7)
		self.char_pos = 0
	
	
	def button_press_event(self, button):
		
		# Update insertion position for the text box
		if button != "clear":
			self.char_pos  = self.char_pos +1
			
		# Number buttons
		if button == 0:
			self.text_box.insert(self.char_pos, 0)
		if button == 1:
			self.text_box.insert(self.char_pos, 1)
		if button == 2:
			self.text_box.insert(self.char_pos, 2)
		if button == 3:
			self.text_box.insert(self.char_pos, 3)
		if button == 4:
			self.text_box.insert(self.char_pos, 4)
		if button == 5:
			self.text_box.insert(self.char_pos, 5)
		if button == 6:
			self.text_box.insert(self.char_pos, 6)
		if button == 7:
			self.text_box.insert(self.char_pos, 7)
		if button == 8:
			self.text_box.insert(self.char_pos, 8)
		if button == 9:
			self.text_box.insert(self.char_pos, 9)
			
		# Math operator buttons
		if button == "+":
			self.text_box.insert(self.char_pos, "+")
		if button == "-":
			self.text_box.insert(self.char_pos, "-")
		if button == "*":
			self.text_box.insert(self.char_pos, "*")
		if button == "/":
			self.text_box.insert(self.char_pos, "/")
		if button == "(":
			self.text_box.insert(self.char_pos, "(")
		if button == ")":
			self.text_box.insert(self.char_pos, ")")
		
		# Clear and enter buttons
		if button == "clear":
			self.text_box.delete(0,END)
			self.char_pos = 0
		if button == "enter":
			_input = self.text_box.get()
			result = self.solve(_input)
			self.text_box.delete(0,END)
			self.char_pos = len(str(result))
			self.text_box.insert(self.char_pos, result)
			

if __name__ == "__main__":
	root_window = Tk()
	calc = calculator(root_window)
	root_window.mainloop()
	
	# Command line usage
	"""
	source = sys.stdin.readline()
	value = calc.solve(source)
	print('The answer is: {}'.format(value))
	"""
