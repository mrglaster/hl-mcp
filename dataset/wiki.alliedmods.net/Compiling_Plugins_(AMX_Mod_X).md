# Compiling Plugins (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/Ru:Compiling_Plugins_\(AMX_Mod_X\) "Ru:Compiling Plugins \(AMX Mod X\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/Zh_cn:Compiling_Plugins_\(AMX_Mod_X\) "Zh cn:Compiling Plugins \(AMX Mod X\)") |   
  
This article describes how to compile [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") plugins from [source code](https://wiki.alliedmods.net/Source_code "Source code") (.sma). 
For all steps, you should place the .sma file addons/amxmodx/scripting. 
## Contents
  * [1 Windows](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Windows)
    * [1.1 Drag and Drop](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Drag_and_Drop)
    * [1.2 Compiling All Plugins](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Compiling_All_Plugins)
    * [1.3 Command Line](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Command_Line)
  * [2 Linux](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Linux)
    * [2.1 Compile All](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Compile_All)
    * [2.2 Compile single](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\)#Compile_single)


# Windows
## Drag and Drop
  1. Drag the .sma file onto "compile.exe".
  2. Look in the compiled folder for the output .amxx file.


## Compiling All Plugins
  1. Double click compile.exe to compile all plugins into the compiled folder.


## Command Line
  1. Go to Start, Run, type "cmd", click Ok.
  2. Use cd to change to the directory, I.e.: ```
cd c:\hlserver\cstrike\addons\amxmodx\scripting
```

  3. Use amxxsc to compile the plugin: ```
amxxpc.exe myplugin.sma
```

  4. The output will be in the same folder.


# Linux
First, change to the scripting folder in your shell with: 
```
cd addons/amxmodx/scripting
```

## Compile All
  1. Run the script compile.sh by either: ```
sh compile.sh
```
or ```
chmod +x compile.sh
```



./compile.sh 
## Compile single
  1. Run amxxpc, like so: ```
./amxxpc myplugin.sma
```

  2. The output will be in the same folder.


