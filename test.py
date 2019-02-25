#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import cProfile
import pstats
import time

from antlr4 import *
from ALF.ALFParser import ALFParser
from ALF.ALFLexer import ALFLexer

filename="alf_parser/examples/samplelibrary.alf"

lexer = ALFLexer(FileStream(filename))
stream = CommonTokenStream(lexer)
stream.fill()
parser = ALFParser(stream)

parser.addErrorListener(DiagnosticErrorListener());
parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION

pr = cProfile.Profile()

pr.enable()  # start profiling
parser.start()
pr.disable()  # end profiling

ps = pstats.Stats(pr)
ps.dump_stats("log.profile")

