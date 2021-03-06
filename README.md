# Overview

This code is designed as a command line tool to completely automate the development of code for the Raspberry Pi Pico running the RP2040 chip.

I was very used to the ease of coding through the Arduino enviornment, so when the Pico came along and I suddenly had to deal with complex CMake files and distributed SDK's, I started to lose interest because of the complexity. However, I wanted to be able to use the Pico in my projects, so I built these tools to make developing for the Pico much easier.

[Software Demo Video](http://youtube.link.goes.here)

# Setup

Read `GET_STARTED.md` for how to get started. It will take you from the ground up

# Development Environment

These tools are written in Python 3.9.1, using VS Code. I used mostly the `os` library to run command line tools, as well as to organize paths to different parts of the SDK.

# Useful Websites

* [Pico SDK](https://github.com/raspberrypi/pico-sdk)
* [Setting up VS Code for programming Pico](https://www.youtube.com/watch?v=mUF9xjDtFfY)

# Future Work

* Build in multi file support
* Simplify the libraries include
* Add an integrated microPython interface
* Add an installer to take care of all the setup processes