#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from antlr4 import *

class MelmacALFData(object):
	unit_names = ['TIME','FREQUENCY','DISTANCE','AREA','VOLTAGE','CURRENT','ENERGY','POWER','CAPACITANCE','RESISTANCE','INDUCTANCE']
	parsing_unit = False
	unit_names = ['TIME','FREQUENCY','DISTANCE','AREA','VOLTAGE','CURRENT','ENERGY','POWER','CAPACITANCE','RESISTANCE','INDUCTANCE']
	recent_unit_name = None

	def __init__(self, expr):
		self.handleExpression(expr)

	def handleExpression(self, expr):
		for child in expr.getChildren():
			if isinstance(child, tree.Tree.TerminalNode):
				token=child.getText()
				print(token)

				if token in self.unit_names:
					self.recent_unit_name=token

				#print("Parsed expression %s" % (expr.getText()))
			else:
				self.handleExpression(child)
