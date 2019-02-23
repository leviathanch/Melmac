PWD:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
ANTLR4_JAR:=$(PWD)/alf_parser/thirdparty/antlr4/tool/target/antlr4-4.7-complete.jar
ANTLR4_PATH:=$(PWD)/alf_parser/thirdparty/antlr4/tool
ANTLR4_CMD:=java -jar $(ANTLR4_JAR)
MAVEN_PATH:=/usr/bin/mvn

all: parser
	./melmac.py alf_parser/examples/samplelibrary.alf

parser: $(ANTLR4_JAR)
	mkdir -p ALF
	cp alf_parser/grammar/ALF.g4 ALF/
	#antlr4 -long-messages -Dlanguage=Python3 ALF/ALF.g4
	#$(ANTLR4_CMD) -long-messages -Dlanguage=Python3 ALF/ALF.g4
	$(ANTLR4_CMD) -Dlanguage=Python3 ALF/ALF.g4

$(ANTLR4_JAR): $(MAVEN_PATH)
	cd $(ANTLR4_PATH) && $(MAVEN_PATH) package

$(MAVEN_PATH):
	echo "Please install Maven!"

