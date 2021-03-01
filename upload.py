#!/usr/bin/env python
import os
import time

def upload():
    waitTime = 10    # Wait for x seconds looking for the drive
    project_directory = "./"
    uf2_file = ""
    pico_location = "/Volumes/RPI-RP2"

    for fname in os.listdir(project_directory):
        if fname.endswith('.uf2'):
            uf2_file = fname
            print("UF2 file found: " + uf2_file)
    
    for fname in os.listdir(project_directory + "/.pico"):
        if fname.endswith('.uf2'):
            uf2_file = ".pico/" + fname
            print("UF2 file found: " + uf2_file)

    if uf2_file == "":
        print("Unable to find UF2 file for target loading. I have spoken.")
        quit()

    # Prompt to connect the drive
    print("Unplug Pico, hold BOOTSEL button, and reconnect")
    print("Searching...")


    time_end = time.time() + waitTime

    while time_end > time.time():
        if os.path.isdir(pico_location):
            break
    else:
        print("Unable to locate drive '" + pico_location + "'.")
        quit()

    time.sleep(2)

    os.system("cp " + project_directory + "/" + uf2_file + " " + pico_location)

    print("Success. Go watch WandaVision now.")