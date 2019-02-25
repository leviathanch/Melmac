#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from antlr4 import *

from ALF.ALFListener import ALFListener
from ALF.ALFLexer import ALFLexer
from ALF.ALFParser import ALFParser

class ALFPrintListener(ALFListener):
	def enterCell(self, ctx):
		print("CELL: "+ctx.identifier().getText())
		#print(ctx.getText())
		#print("CELL: %s" % ctx.alf_id())
	
	def enterIdentifier(self, ctx):
		print("identifier: "+ctx.getText())

class MelmacALFData(object):
	def __init__(self, filename):
		print("Opening file: "+filename)
		lexer = ALFLexer(FileStream(filename))
		stream = CommonTokenStream(lexer)
		stream.fill()
		self.parser = ALFParser(stream)
		self.parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
		tree = self.parser.start()
		printer = ALFPrintListener()
		walker = ParseTreeWalker()
		walker.walk(printer, tree)

