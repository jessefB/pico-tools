#!/usr/bin/env python3
import new, make, upload
import argparse

## Put all tools in one file. That will simplify stuff a lot. I think. Ask bro. macbeth

# First things first - get the argument parser up and running
parser_message = "May the force be with you and the odds ever in your favor. I have spoken."
parser = argparse.ArgumentParser(prog="pico", usage="%(prog)s [options]", epilog=parser_message)
parser.add_argument("--make", "-m",help="Make the project and return a .uf2 file", action="store_true")
parser.add_argument("--build", "-b", help="Make the project and upload it to the target", action="store_true")
parser.add_argument("--new", "-n", metavar="projectName", help="Create build tools for new project", type=str)

args = parser.parse_args()

if (args.make):
    make.make(False)
elif (args.build):
    make.make(True)
    upload.upload()
elif (args.new != None):
    new.new(args.new)

else:
    parser.print_help();