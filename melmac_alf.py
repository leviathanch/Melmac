#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from antlr4 import *

class MelmacALFData(object):
	unit_names = ['TIME','FREQUENCY','DISTANCE','AREA','VOLTAGE','CURRENT','ENERGY','POWER','CAPACITANCE','RESISTANCE','INDUCTANCE']

	def __init__(self, expr):
		self.handleExpression(expr)

	def handleExpression(self, expr):
		for child in expr.getChildren():
			if isinstance(child, tree.Tree.TerminalNode):
				token=child.getText()
				print("Parsed expression %s" % (expr.getText()))
				print(token)
			else:
				self.handleExpression(child)
