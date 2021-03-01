#!/usr/bin/env python
import os
import shutil


def new(projectName):
    # General variables
    working_path = "./"
    project_name = projectName
    source_files = "main.cpp"
    libraries = "pico_stdlib"
    cmake_list_source = "/Applications/pico/pico-sdk/external/CMakeLists.txt"
    pico_import_source = "/Applications/pico/pico-sdk/external/pico_sdk_import.cmake"


    directory = ".pico"
    build_path = os.path.join(working_path, directory)


    # Build custom CMakeLists.txt
    def build_cmake_list():

        replace_key = {
            '$project' : project_name,
            '$executables' : "../" + source_files,
            '$libraries' : libraries
        }

        f = open(build_path + "/CMakeLists.txt", 'w')
        src = open(cmake_list_source, 'r')

        for line in src:

            for key in replace_key:
                if key in line:
                    line = line.replace(key, replace_key[key])
            f.write(line)

        f.close()
        src.close()

    
    # Create the '.build' directory
    print("Attempting project structure build... ", end='')

    os.mkdir(build_path)

    print("done.")



    # Add build tools (pico_sdk_import.cmake)
    print("Attempting project tools build... ", end='')

    build_cmake_list()
    shutil.copy(pico_import_source, build_path)

    print("done.")