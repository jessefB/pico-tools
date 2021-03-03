#!/usr/bin/env python
import os

## Verify this works on windows.... hopefully.

def make(build):
    # Directory should have all needed systems at this point

    project_directory = "./"
    pico_directory = project_directory + "/.pico"

    # Check to see if CMake has already been run by looking for the cache file
    #if not (os.path.isfile(pico_directory+ "/CMakeCache.txt")):
        # Try to run CMake on the project
    os.system("cmake -S " + pico_directory + " -B " + pico_directory)

    # Next run make
    os.system("make -C " + pico_directory)

    if not build:
        # Finally, try to move the resulting uf2 file up a directory
        os.system("mv " + pico_directory + "/*.uf2 " + project_directory + "/")
