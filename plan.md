# Plan

## Get pico sdk working

## Automate SDK development
I'm thinking like arduino tools. Include one library for basic IO stuff, one line command to compile and upload, etc.

### Thoughts:
* .uf2 files, .o, compilation tools should be in a `.~~` folder. Something like that
* Library for IO, cores, analog stuff
* General purpose library should have abstraction, easier functions, includes IO (`pico-io`?)