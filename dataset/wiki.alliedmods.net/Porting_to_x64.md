# Porting to x64
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Porting_to_x64#mw-head), [search](https://wiki.alliedmods.net/Porting_to_x64#p-search)
## Contents
  * [1 Overview](https://wiki.alliedmods.net/Porting_to_x64#Overview)
  * [2 I'm having an issue!](https://wiki.alliedmods.net/Porting_to_x64#I.27m_having_an_issue.21)
    * [2.1 Linux Calling Convention Quirks](https://wiki.alliedmods.net/Porting_to_x64#Linux_Calling_Convention_Quirks)
    * [2.2 MSVC Calling Convention Quirks](https://wiki.alliedmods.net/Porting_to_x64#MSVC_Calling_Convention_Quirks)
  * [3 Porting Plugins](https://wiki.alliedmods.net/Porting_to_x64#Porting_Plugins)
    * [3.1 Gamedata](https://wiki.alliedmods.net/Porting_to_x64#Gamedata)
      * [3.1.1 Gamedata key names](https://wiki.alliedmods.net/Porting_to_x64#Gamedata_key_names)
    * [3.2 Address Natives](https://wiki.alliedmods.net/Porting_to_x64#Address_Natives)
    * [3.3 DHooks](https://wiki.alliedmods.net/Porting_to_x64#DHooks)
    * [3.4 SDKCalls](https://wiki.alliedmods.net/Porting_to_x64#SDKCalls)
  * [4 Recompiling Extensions](https://wiki.alliedmods.net/Porting_to_x64#Recompiling_Extensions)


## Overview
Many plugins are already compatible with the x64 architecture, but many that manipulate game memory (such as with hooks or patches) will require extensive revisions to run under the new 64-bit servers. Overall, if your plugin: 
  * Uses the address natives or the Address type,
  * Uses dhooks
  * Uses sdkcalls or sdktools (_not sdkhooks_)


...you will need to update your plugin for 64 bits. 
Extensions may be good to go with just a recompile for 64-bits, but some may need more extensives changes. 
## I'm having an issue!
In general, **prototypes need to be exactly correct** (including class statics like copy/destruct/constructors) as there are now significantly more quirks that will cause ABIs to be laid out differently. 
Here are some things to check for that may be tripping you up: 
  * The type you thought was an _int_ was actually a _size_t_!
  * The type you put down as an int or pointer was actually a _float_!
  * Handling pointers as _int_ s when they should be _void*_ or _size_t_
  * **The calling convention has changed.** Make sure to account for this in detours and patches. Make sure your prototypes are exactly correct!
  * **In patches:** Did you forget the 64-bit opcode prefix when assembling your patch? EAX and RAX are accessed using different opcode prefixes!


### Linux Calling Convention Quirks
Linux uses the System-V x64 ABI. There are many great sources of documentation all over the internet: [OSDev Wiki](https://wiki.osdev.org/System_V_ABI) [Wikipedia](https://en.wikipedia.org/wiki/X86_calling_conventions#x86-64_calling_conventions)
  * All calling conventions are now an up to 8-register fastcall depending on the types (!!)
  * RDI can be a thisptr, first argument, or stack return pointer depending on the context
  * **Integer arguments and float arguments are passed in different registers!** (generic for ints, SIMD registers for floats)
  * Varargs are now more complex to call when floats are included in the vararg


The exact value of return types with C++ shenanigans (destructors, etc) still needs to be figured out by someone. However, in general. 
  * Return types bigger than 64 bits but smaller than 128 bits will be returned in RAX and RDX


### MSVC Calling Convention Quirks
Microsoft has some excellent official documentation [in their MSVC docs](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention?view=msvc-170). 
  * All calling conventions are now a four-register fastcall
  * RCX is always the this pointers in member function call.
  * **Integer arguments and float arguments are passed in different registers!** (generic for ints, SIMD registers for floats)
  * If the type doesn't have a size of 8, 16, 32 or 64 bits or has special copy operator, or copy constructor, or destructor it will be passed as pointer to a memory space that is sizeof(type).
  * Float arguments passed to varargs need to be put in both the generic and SIMD register for the appropiate argument index. Varargs are still fastcalls... somehow...
  * **setjmp has new behavior** and destroys objects as if the scope has been exited. (if you _are_ using setjmp, good luck)
  * The stack is always freed by the caller, never the callee


If the return type is passed in memory, the pointer to that memory will be passed as the first argument to the function. 
  * In RDX if member function (because RCX is always this pointer)
  * In RCX for everything else


  

## Porting Plugins
### Gamedata
All bytes signatures will need to be updated, mangled names stay mostly as-is. Vtable offsets won't change. 
#### Gamedata key names
Arch/OS  | Linux  | Windows   
---|---|---  
x86  | linux  | windows   
x64  | linux64  | windows64   
### Address Natives
New address natives that support 64-bits are still under development 
### DHooks
DHooks received partial support for 64-bits, only windows is supported. It will need heavy revisions to work under linux 64 bits, starting with better SourceHook support (see: hookmangen) 
### SDKCalls
SDKCalls will need to be updated to learn how to accept a thisptr. However, all non-raw calls (eg, those to entities or gamerules that does not require a thisptr) should be fine as long as none of the arguments are 64-bits (including 64-bit ints!) 
## Recompiling Extensions
Take a look at/copy the sample extension AMBuilder and AMBuildScript available on the sourcemod repository. 
Beyond that, as long as the code isn't architecture-specific, most extensions should compile fine with 64-bit support with slight adjustments at most. If you are using detours, you may need to [make further adjustments to build the new safetyhook dependency](https://github.com/alliedmodders/sourcemod/blob/96727a7610a2690b20670264edb737a42f9da110/AMBuildScript#L583-L591). 
