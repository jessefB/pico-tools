# Getting started

This will take you step by step on how to program the Pico. This has been tested on macOS Big Sur and Windows 10, and should work on Linux distros as well.

## Get the tools
1. Clone the `pico-sdk` repository
   - Download the zip [pico-sdk](https://github.com/raspberrypi/pico-sdk)
   - Unzip the downloaded SDK into a direcory. It doesn't matter where.
   - Add an enviorment variable called `PICO_SDK_PATH` and give it the value of the direcory you unzipped the SDK into
1. Get the `gcc-arm` compiler
   - Download the [GCC](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads) compiler
   - Run the installer, making sure to say "Add path to enviornment variable" at the end
1. Install [CMake](https://cmake.org/download/)
   - Download the installer (not the zip!)
   - Run the installer, making sure to say "Add CMake to path for all users"
1. Get Python 3
   - If you are programming the Pico, you should already have python installed. Just sayin.
   -  If not, look up a tutorial.

## Setup pico-tools

Clone this repository, and move `pico-tools.py` and `config.json` into a direcory in your path. From there, search "change python script into executable" to make it a true command line tool.