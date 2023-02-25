#####################################################################
#   This Makefile builds all HELLO_WORLDcutables to run the openCv program	#
#####################################################################
#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

CC=g++
CPPFLAGS= -g -Wall
OPENCVFLAGS = `pkg-config --cflags --libs opencv`#4` # use "opencv4" when you want to link to version 4
LIBRARIES = $(OPENCVFLAGS)

# To add additional cpp files uncomment and change 
# "SRC_NEW_SRC", 'name_of_file.cpp', "NEW_EXE", "newExe" and "newTarget"

# find sources
SRC_MAIN := $(shell find . -name 'main.cpp')
SRC_VERSION := $(shell find . -name 'openCv_version.cpp')
SRC_TACKLE := $(shell find . -name 'tackleImg.cpp')
#SRC_NEW_SRC := $(shell find . -name 'name_of_file.cpp')


# name executables
EXE_MAIN := helloWorld
EXE_VERSION := checkVersion
EXE_TACKLE := tackle
#NEW_EXE := newExe


# main target
all: main version tackle #newTarget
	@echo "\nAll object files created and linked.\nAll executables created.\n\
	Use with: ./helloWorld <path_to_file>"


# name targets seperately
main: $(EXE_MAIN)
version: $(EXE_VERSION)
tackle: $(EXE_TACKLE)
#newTarget: $(EXE_NEW_EXE)


# build exexcutables
$(EXE_MAIN): $(SRC_MAIN)
	$(CC) $(CPPFLAGS) -o $(EXE_MAIN) $< $(LIBRARIES)

$(EXE_VERSION): $(SRC_VERSION)
	$(CC) $(CPPFLAGS) -o $(EXE_VERSION) $< $(LIBRARIES)

$(EXE_TACKLE): $(SRC_TACKLE)
	$(CC) $(CPPFLAGS) -o $(EXE_TACKLE) $< $(LIBRARIES)

#$(EXE_NEW_EXE): $(SRC_NEWFILE)
#	$(CC) $(CPPFLAGS) -o $(EXE_NEW_EXE) $< $(LIBRARIES)


# cleaning target
clean:
	-rm -rf *.o $(EXE_MAIN) $(EXE_VERSION) $(EXE_TACKLE) $(EXE_NEW_EXE)