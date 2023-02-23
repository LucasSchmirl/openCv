#####################################################################
#   This Makefile builds all executables to run the openCv program	#
#####################################################################
#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

CC=g++
CPPFLAGS= -g -Wall
OPENCVFLAGS = `pkg-config --cflags --libs opencv`#4` # use "opencv4" when you want to link to version 4
LIBRARIES = $(OPENCVFLAGS)

# find sources
MAIN := $(shell find . -name 'main.cpp')
CHECKVERSION := $(shell find . -name 'openCv_version.cpp')

# name executables
EXE := helloWorld
VERSION := checkVersion

# main target
all: main version
	@echo "\nAll object files created and linked.\nAll executables created (helloWorld, openCv_version).\n\
	Use with: ./helloWorld <path_to_file> and ./checkVersion\n"

main: $(EXE)

version: $(VERSION)


# build executable programs
$(EXE): $(MAIN)
	$(CC) $(CPPFLAGS) -o $(EXE) $< $(LIBRARIES)

$(VERSION): $(CHECKVERSION)
	$(CC) $(CPPFLAGS) -o $(VERSION) $< $(LIBRARIES)

# cleaning target
clean:
	-rm -rf *.o $(EXE) $(VERSION)