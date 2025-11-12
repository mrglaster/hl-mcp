. Installation: Manual
Content:
  * [Introduction](http://127.0.0.1:8000/content/manual.htm#introduction)
  * [Directory structure](http://127.0.0.1:8000/content/manual.htm#dirstruct)
  * [Metamod](http://127.0.0.1:8000/content/manual.htm#metamod)
  * [AMX Mod X](http://127.0.0.1:8000/content/manual.htm#amxx)
  * [Configuration](http://127.0.0.1:8000/content/manual.htm#config)


a) Introduction
There are a few ways you can install AMX Mod X. If you have shell or direct access to your server, you can do all operations directly on the server itself. If you only have FTP access, it's best to install AMX Mod X on a "dummy" folder on your hard drive, do all configuration there, and then upload the files to your server. Otherwise, you can upload the files as you're installing and then use FTP to change things along the way.  
Throughout the documentation we'll refer to your "mod folder" - this is the folder your mod is stored in, like "cstrike", or "dod", for example. If you're installing on a listen server, it will be somewhere in \Program Files\Steam\SteamApps\<your steam login>\<Valve game or Half-Life>\<mod folder>. If you're using a dedicated server, it will be HLServer\<mod folder>. On linux this is hlds_l/<mod folder>. If you are using remote/FTP access, you may be restricted to your mod folder or hlds_l already, and don't need to find it. For this documentation, <mod folder> will refer to the mod folder mentioned above. For Linux users, binaries will not end in ".dll", they will usually end in "_i386.so" or "_amd64.so" for AMD64 machines. 
b) Directory structure
You should familiarize yourself with the directory structure for AMX Mod X now.  
addons\ - this is where Server addons go  
metamod\ - this is where Metamod goes. Metamod is necessary to run AMX Mod X  
dlls\ - this is where Metamod's binaries go  
amxmodx\ - this is where AMX Mod X goes  
dlls\ - amxmodx_mm.dll should go here  
modules\ - Where modules are stored (_amxx.dll or _amxx_i386.so etc)  
plugins\ - Where plugins are stored (.amx or .amxx)  
scripting\ - Where example source code and the compiler/assembler are stored  
include\ - Where include files for source code is stored  
compiled\ - Where the compiler batch file stores .amxx output  
doc\ - This documentation is kept here  
data\ - Binary data, for example saved stats, language caches, and GeoIP information  
lang\ - Dictionary text files for AMX Mod X ML features (multi lingual)  
configs\ - Configuration files  
logs\ - AMX Mod X log files 
c) Metamod
  1. If you already have metamod installed, you may skip to step e.  
In your mod folder, create a folder called "addons".  
In <mod folder>\addons, create a folder called "metamod".  
In <mod folder>\addons\metamod, create a folder called "dlls". 
  2. Go to [www.metamod.org](http://www.metamod.org/) and download the appropriate version of Metamod (either Windows, Linux, or Linux AMD64).
  3. Extract the metamod binary into <mod folder>\addons\metamod\dlls.
  4. Edit the file <mod folder>\liblist.gam with a text-editor like Notepad.  
For windows, find the gamedll line. It will look like this:  
```
gamedll "dlls\mp.dll"
```
Replace it with: ```
gamedll "addons\metamod\dlls\metamod.dll"
```
For Linux, find the gamedll line. It will look like this: ```
gamedll_linux "dlls/mp_i386.so"
```
Replace it with: ```
gamedll_linux "addons/metamod/dlls/metamod_i386.so"
```
*NOTE: use metamod_amd64.so for AMD64 servers. 
  5. Edit the file <mod folder>\addons\metamod\plugins.ini. If it does not exist, create it.
  6. If you are upgrading from AMX or AMX Mod X 0.1x, skip to step h.
  7. Add a line to <mod folder>\addons\metamod\plugins.ini like so: Windows: ```
win32 addons\amxmodx\dlls\amxmodx_mm.dll
```
Linux: ```
linux addons/amxmodx/dlls/amxmodx_mm_i386.so
```
Linux AMD64: ```
linux addons/amxmodx/dlls/amxmodx_mm_amd64.so
```

  8. If you're using AMX, change "amx\amx_" to "amxmodx\amxmodx_".  
If you're using AMX Mod X 0.1x, change "amxx\amxx_" to "amxmodx\amxmodx_". 


d) AMX Mod X
  1. Go to [www.amxmodx.org](http://www.amxmodx.org/) and click "Downloads". Download the amxmodx-base package for either Windows, Linux, or AMD64.
  2. Extract the base package to your mod folder. This will place AMX Mod X into <mod folder>\addons\amxmodx.
  3. Go back to the AMX Mod X download site. If there is one available, and you want to use it, download the addon package corresponding to your mod.  
As of this writing, addon packs are available for Counter-Strike/Condition-Zero, Team Fortress Classic, Day of Defeat, The Specialists, and Natural Selection.  
Make sure you download the pack that corresponds to the server's operating system, either Windows, Linux, or AMD64. 
  4. Extract the addons pack into your mod folder. This will merge the addon pack into your installation in <mod folder>\addons\amxmodx.
  5. AMX Mod X should now be installed! You can load your server now to try it out (type "meta list" to see it loaded).


e) Configuration
Now that AMX Mod X is installed, move on to the [Configuration Section](http://127.0.0.1:8000/configuration/).
