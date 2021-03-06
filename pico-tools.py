import json
import argparse
import os
import shutil
import time
import platform

# First things first - get the argument parser up and running
parser_message = "May the force be with you and the odds ever in your favor. I have spoken."
parser = argparse.ArgumentParser(prog="pico", usage="%(prog)s [options]", epilog=parser_message)
parser.add_argument("--make", "-m",help="Make the project and return a .uf2 file", action="store_true")
parser.add_argument("--build", "-b", help="Make the project and upload it to the target", action="store_true")
parser.add_argument("--upload", "-u", help="Upload .uf2 file to target", action="store_true")
parser.add_argument("--new", "-n", metavar="projectName", help="Create build tools for new project", type=str)

args = parser.parse_args()




# Get the OS
is_windows = (platform.system() == "Windows")

# Get configuration
with open("config.json", 'r') as f:
    config = json.load(f)

project_directory = config["default_project_directory"]
build_directory = os.path.join(project_directory, ".pico")


# Make the project
def make(build):
    # CMake the build directory
    os.system("cmake -G \"Unix Makefiles\" -S " + build_directory + " -B " + build_directory + " .")

    # For some reason, Windows throws errors when not running 'make' for the first time
    # Delete some stuff, and it seems to work... not sure why, but whatevs.
    if is_windows:
        if os.path.isdir(build_directory):
            os.system("rmdir /s /q " + os.path.join(build_directory, "CMakeFiles"))

    # Next run make
    os.system("make -C " + build_directory)

    if not build:
        # Finally, try to move the resulting uf2 file up a directory
        if is_windows:
            os.system("move " + os.path.join(build_directory, "*.uf2 ") + project_directory)
        else:
            os.system("mv " + os.path.join(build_directory, "*.uf2 ") + project_directory)

# Create the needed build systems
def new(projectName):
    # This needs to be figured out for multi file support and libraries
    source_files = "main.cpp"
    libraries = "pico_stdlib"

    # Make sure the OS variable is set
    if os.environ["PICO_SDK_PATH"] == None:
        print("Enviorment variable PICO_SDK_PATH not found. Program aborted")
        quit()

    cmake_list_source = os.path.join(os.environ["PICO_SDK_PATH"], "external\\CMakeLists.txt")
    pico_import_source = os.path.join(os.environ["PICO_SDK_PATH"], "external\\pico_sdk_import.cmake")


    # Build custom CMakeLists.txt
    def build_cmake_list():

        replace_key = {
            '$project' : projectName,
            '$executables' : "../" + source_files,
            '$libraries' : libraries
        }

        # Create the file for writing
        with open(os.path.join(build_directory, "CMakeLists.txt"), 'w') as f:

            # Open the source file for reading
            with open(cmake_list_source, 'r') as src:

                # Copy line by line from the source CMakeLists.txt template
                for line in src:

                    # Replace any keys, like the project name, etc.
                    for key in replace_key:
                        if key in line:
                            line = line.replace(key, replace_key[key])
                    f.write(line)

    
    # Create the '.pico' directory
    print("Attempting project structure build... ", end='')
    try:
        # Ceck to see if the directory exists
        if not os.path.isdir(build_directory):
            os.mkdir(build_directory)
        else:
            print("already exists... ", end='')
    except:
        print("Failed. Program aborted.")
        quit()
    else:
        print("done.")



    # Add build tools (pico_sdk_import.cmake)
    print("Attempting project tools build... ", end='')

    try:
        build_cmake_list()
        shutil.copy(pico_import_source, build_directory)
    except:
        print("Failed. Program aborted.")
        quit()
    else:
        print("done.")

# Find the final '.uf2' file for upload
def getUF2(project_directory):
    # Look for the .uf2 file
    for files in os.listdir(project_directory):
        if files.endswith('.uf2'):
            uf2_file = files
            print("UF2 file found: " + uf2_file)
            break
    
    if uf2_file == None:
        for files in os.listdir(os.path.join(project_directory, ".pico")):
            if files.endswith('.uf2'):
                uf2_file = os.path.join(".pico/", files)
                print("UF2 file found: " + uf2_file)
                break

    if uf2_file == None:
        print("Unable to find UF2 file for target loading. I have spoken.")
        quit()

    return uf2_file

# Upload the '.uf2' file to target
def upload():
    waitTime = config["pico_search_time"]

    # Get the drive location
    if is_windows:
        pico_location = config["windows_pico_location"]
    else:
        pico_location = config["unix_pico_location"]

    # Get the UF2 file location
    uf2_file = getUF2(project_directory)

    # Prompt to connect the drive
    print("Unplug Pico, hold BOOTSEL button, and reconnect")

    # Set up a timer based on 'waitTime'
    time_end = time.time() + waitTime

    # Loop for 'waitTime' seconds or until the drive is found
    while time_end > time.time():
        if os.path.isdir(pico_location):
            break
    else:
        print("\nUnable to locate drive '" + pico_location + "'.")
        quit()

    # Newline after the "Searching...." dots animation
    print("")

    # Make sure the drive is able to mount correctly
    time.sleep(2)

    # Copy the .uf2 file over to the "removable drive"
    if is_windows:
        os.system("copy \"" + os.path.join(project_directory, uf2_file) + "\" " + pico_location)
    else:
        os.system("cp " + os.path.join(project_directory, uf2_file) + " " + pico_location)


    print("Success on upload to target. You can watch the Mandalorian now.")


if (args.make):
    make(False)
elif (args.build):
    make(True)
    upload()
elif (args.new != None):
    new(args.new)
elif (args.upload):
    upload()

else:
    parser.print_help();