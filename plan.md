# Plan
This is a document for me, the creator. Don't pay attention to this... or do. Your choice. Don't say I didn't warn you though...

The absolute end goal for this is to have a full pico development platform that is cross platform and preferably IDE independant (but integratable into VS Code)

## Things to do
1. C++ auto-compile/upload
1. General purpose library
1. System installer
1. VS Codes extension to run scripts?
1. Stop full sdk from compiling for every project


## Automate SDK development
I'm thinking like arduino tools. Include one library for basic IO stuff, one line command to compile and upload, etc.

Needs to be cross platform. 03/03/12 update: Comment the code, possibly rewrite it, make it really clean. Maybe add a .json config file for all the system different parts?

### Thoughts:
* .uf2 files, .o, compilation tools should be in a `.~~` folder. Something like that to hide unnecessary complications
* Library for IO, cores, analog stuff, clock, etc.


## Modularize Tools
I'd like this system to be just super robust, all-in-one for coding the pico. Should be able to handle micropython uploading (possibly even putting on the runtime enviorment... maybe?), as well as C++ compilation and uploading


## VS Code Intellisense?
Adding the include path to VS Code works, except the included files are seperatly stored, and their includes acutally come from the CMakeLists.txt files, which causes more intellisense errors.

* General purpose library should have abstraction, easier functions, includes IO (`pico-io`?)


## Installer
1. Install gcc-arm compiler
1. Create pico direcory
1. Install pico-sdk, python enviorments, and CMakeLists.txt template file
1. Add gcc-arm to path, add PICO_SDK_PATH variable
1. Install auto-compile/upload tools
1. Add to path auto-compile/upload tools location (maybe just an alias?)


`pico -new projectName` - This creates `.pico` folder with build tools

`pico -make` - Builds the project, results in a single `out.uf2` output file

`pico -build` - Builds the project and looks for target to add to. Uses prompts to guide the user to upload

`pico -py [micro/circuit]` - Puts the micropython or circuit python runtime enviorments on the pico