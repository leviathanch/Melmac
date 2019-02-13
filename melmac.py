#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

from antlr4 import *
from melmac_alf import MelmacALFData
from alf_parser.grammar.ALFLexer import ALFLexer
from alf_parser.grammar.ALFParser import ALFParser
from alf_parser.grammar.ALFListener import ALFListener

class Melmac(object):
	def __init__(self, filename):
		lexer = ALFLexer(FileStream(filename))
		stream = CommonTokenStream(lexer)
		parser = ALFParser(stream)
		tree = parser.start()
		data = MelmacALFData(tree)


if len(sys.argv)>1:
	main = Melmac(sys.argv[1])
