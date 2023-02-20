#####################################################################
#   This Makefile builds all executables to run the openCv program	#
#####################################################################
#	made by Lucas Schmirl 20.02.2022,	last edit: 20.02.2022

CC=g++
CPPFLAGS= -g -Wall
OPENCVFLAGS = `pkg-config --cflags --libs opencv4`
LIBRARIES = $(OPENCVFLAGS)

# find sources
SOURCE := $(shell find . -name 'main.cpp')

# # find headers
# HEADERS := $(shell find . -name '*.hpp')

# name executables
EXE := helloWorld


all: $(EXE)
	@echo "\nAll object files created and linked.\nAll executables created (helloWorld).\nUse with: ./helloWorld <path_to_file>\n"


# build executable programs
$(EXE): $(SOURCE)
	$(CC) $(CPPFLAGS) -o $(EXE) $< $(LIBRARIES)



# cleaning target
clean:
	-rm -rf *.o $(EXE)