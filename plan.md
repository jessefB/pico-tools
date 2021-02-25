# Plan
This is a document for me, the creator. Don't pay attention to this... or do. Your choice. Don't say I didn't warn you though...

## Get pico sdk working
I saved some youtube vids under "Watch Later" that goes into setting up vscode 

## Automate SDK development
I'm thinking like arduino tools. Include one library for basic IO stuff, one line command to compile and upload, etc.

### Thoughts:
* .uf2 files, .o, compilation tools should be in a `.~~` folder. Something like that to hide unnecessary complications
* Library for IO, cores, analog stuff, clock, etc.
* General purpose library should have abstraction, easier functions, includes IO (`pico-io`?)

## Modularize Tools
I'd like this system to be just super robust, all-in-one for coding the pico. Should be able to handle micropython uploading (possibly even putting on the runtime enviorment... maybe?), as well as C++ compilation and uploading

## VS Code Intellisense?
It would be nice to maybe have a pico extension or something for color coding, autocomplete, and to get rid of the red squigle lines of death. I've got no clue how involved that is. I could probably just get away with using the C++ and/or Python extensions (respective to their file types)

## Things to do
1. Systems - IDE integration, auto compilation, script transfer, installer
1. General purpose library
1. 