# Melmac
A tool for parsing and exporting ALF format into different formats

## Building Python3
antlr4 -listener -long-messages -Dlanguage=Python3 alf_parser/grammar/ALF.g4 

## Executing
./melmac.py alf_parser/examples/samplelibrary.alf
