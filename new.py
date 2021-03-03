#!/usr/bin/env python
import os
import shutil


## Add robustness. Try/catch, user frinedly, etc. Make it awesome


def new(projectName):
    # General variables
    working_path = "./"
    project_name = projectName
    # This needs to be figured out for multi file support
    source_files = "main.cpp"
    libraries = "pico_stdlib"
    # os.path.join? for next lines?
    cmake_list_source = os.environ("PICO_SDK_PATH") + "/external/CMakeLists.txt"
    pico_import_source = os.environ("PICO_SDK_PATH") + "/external/pico_sdk_import.cmake"


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