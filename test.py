#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import cProfile
import pstats
import time

from melmac_alf import MelmacALFData

from antlr4 import *
from ALF.ALFParser import ALFParser

class Melmac(object):
	def __init__(self, filename):
		self.data = MelmacALFData(filename)

	def parser(self):
		return self.data.parser

	#def start(self):
	#	return self.data

if len(sys.argv)>1:
	main = Melmac(sys.argv[1])
	pr = cProfile.Profile()
	parser=main.parser()
	parser.addErrorListener(DiagnosticErrorListener());
	#parser.getInterpreter().setPredictionMode(PredictionMode.LL_EXACT_AMBIG_DETECTION);
	parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION

	pr.enable()  # start profiling
	#print("Test")
	parser.start()
	pr.disable()  # end profiling
	pr.dump_stats("log.profile")

	#ps = pstats.Stats(pr).sort_stats('cumulative')
	#ps.print_stats()

	#print(main.start())

