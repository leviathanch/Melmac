#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re


from antlr4 import *
from melmac_alf import MelmacALFData
from ALF.ALFLexer import ALFLexer
from ALF.ALFParser import ALFParser
from ALF.ALFListener import ALFListener

class Melmac(object):
	def __init__(self, filename):
		self.data = MelmacALFData(filename)

if len(sys.argv)>1:
	main = Melmac(sys.argv[1])
