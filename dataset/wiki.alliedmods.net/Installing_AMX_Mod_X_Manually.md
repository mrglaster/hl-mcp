# Installing AMX Mod X Manually
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#mw-head), [search](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#p-search)
This guide will help you install AMX Mod X without the assistance of an automated tool. 
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Introduction)
  * [2 Directory Structure](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Directory_Structure)
  * [3 Installing Metamod](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Installing_Metamod)
    * [3.1 Directory Structure](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Directory_Structure_2)
    * [3.2 Upload Binaries](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Upload_Binaries)
    * [3.3 Configure](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Configure)
    * [3.4 Installing AMX Mod X](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Installing_AMX_Mod_X)


# Introduction
There are a few ways you can install [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X"). If you have [shell](https://wiki.alliedmods.net/index.php?title=Shell&action=edit&redlink=1 "Shell \(page does not exist\)") or direct access to your server, you can do all pf the operations directly on the server itself. If you only have [FTP](https://wiki.alliedmods.net/FTP "FTP") access, it's best to install [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") on a "[dummy](https://wiki.alliedmods.net/index.php?title=Dummy&action=edit&redlink=1 "Dummy \(page does not exist\)")" folder on your hard drive, do all configuration there, and then upload the files to your server. Otherwise, you can upload the files as you're installing and then use [FTP](https://wiki.alliedmods.net/FTP "FTP") to change things along the way. 
Throughout the documentation we'll refer to your "[mod folder](https://wiki.alliedmods.net/Mod_folder "Mod folder")" - this is the folder your mod is stored in, like "cstrike" (for Counter-Strike), or "dod" (for Day of Defeat). If you're installing on a listen server, it will be in \Program Files\Steam\SteamApps\<your steam login>\<Valve game or Half-Life>\<mod folder>. If you're using a dedicated server, it will be HLServer\<mod folder>. On linux this is hlds_l/<mod folder>. If you are using remote/[FTP](https://wiki.alliedmods.net/FTP "FTP") access, you may be restricted to your [mod folder](https://wiki.alliedmods.net/Mod_folder "Mod folder") or hlds_l already, and don't need to find it. For this documentation, <mod folder> will refer to the mod folder mentioned above. For [Linux](https://wiki.alliedmods.net/index.php?title=Linux&action=edit&redlink=1 "Linux \(page does not exist\)") users, binaries will not end in ".dll", they will usually end in "_i386.so" or "_amd64.so" for [AMD64](https://wiki.alliedmods.net/index.php?title=AMD64&action=edit&redlink=1 "AMD64 \(page does not exist\)") machines. 
# Directory Structure
You should familiarize yourself with AMX Mod X's directory structure. The addons folder resides in your [mod folder](https://wiki.alliedmods.net/Mod_folder "Mod folder"). 
```
--addons         - this is where Server addons go
 |--metamod      - this is where Metamod goes. Metamod is necessary to run AMX Mod X
   |--dlls       - this is where Metamod's binaries go
 |--amxmodx      - this is where AMX Mod X goes
   |--dlls       - amxmodx_mm.dll should go here
   |--modules    - Where modules are stored (_amxx.dll or _amxx_i386.so etc)
   |--plugins    - Where plugins are stored (.amx or .amxx)
   |--scripting  - Where example source code and the compiler/assembler are stored
     |--include  - Where include files for source code is stored
     |--compiled - Where the compiler batch file stores .amxx output
   |--doc        - This documentation is kept here
   |--data       - Binary data, for example saved stats, language caches, and GeoIP information
     |--lang     - Dictionary text files for AMX Mod X ML features (multi lingual)
   |--configs    - Configuration files
   |--logs       - AMX Mod X log files

```

# Installing Metamod
Because AMX Mod X is a [Metamod](https://wiki.alliedmods.net/Metamod "Metamod") plugin, you must first install Metamod. If you already have it installed, you may skip this section and jump to [#Installing AMX Mod X](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Manually#Installing_AMX_Mod_X). 
## Directory Structure
  1. In your mod folder, create a folder called "addons".
  2. In <mod folder>\addons, create a folder called "metamod".
  3. In <mod folder>\addons\metamod, create a folder called "dlls".


## Upload Binaries
  1. Go to the [Metamod Website](http://www.metamod.org/) and download Metamod. You will want to get either the Windows [DLL](https://wiki.alliedmods.net/index.php?title=DLL&action=edit&redlink=1 "DLL \(page does not exist\)") or the [Linux SO](https://wiki.alliedmods.net/index.php?title=Linux_SO&action=edit&redlink=1 "Linux SO \(page does not exist\)") (for either 32bit [Linux](https://wiki.alliedmods.net/index.php?title=Linux&action=edit&redlink=1 "Linux \(page does not exist\)") or [Linux](https://wiki.alliedmods.net/index.php?title=Linux&action=edit&redlink=1 "Linux \(page does not exist\)") on [AMD64](https://wiki.alliedmods.net/index.php?title=AMD64&action=edit&redlink=1 "AMD64 \(page does not exist\)")).
  2. Extract the metamod file and upload or copy it to your server. It must be placed in <mod folder>\addons\metamod\dlls.


## Configure
  1. In your mod folder, find the "[liblist.gam](https://wiki.alliedmods.net/Liblist.gam "Liblist.gam")" file. Open the file with a text editor, such as [notepad](https://wiki.alliedmods.net/index.php?title=Notepad&action=edit&redlink=1 "Notepad \(page does not exist\)"). If you're using FTP or a control panel, you will need to download the file first.
  2. For Windows, find this line:      ```
gamedll "dlls\mp.dll"
```
    Replace it with this line: ```
gamedll "addons\metamod\dlls\metamod.dll"
```
For Linux, find this line:      ```
gamedll_linux "dlls/mp_i386.so"
```
    Replace it with this line: (for servers using hldsupdatetool) ```
gamedll_linux "addons/metamod/dlls/metamod_i386.so"
```
    Replace it with this line: (for servers using steamcmd) ```
gamedll_linux "addons/metamod/dlls/metamod.so"
```
    _(Note: AMD64 is no longer supported for various reasons, please use 32bit)_
  3. Save liblist.gam (and upload it over the old one if your server is remote).
  4. Edit the file <mod folder>\addons\metamod\plugins.ini. If it does not exist, create it. This file is your list of Metamod plugins.
  5. For Windows, add ```
win32 addons/amxmodx/dlls/amxmodx_mm.dll
```

For Linux add: 
```
linux addons/amxmodx/dlls/amxmodx_mm_i386.so
```

  6. Save (and upload) plugins.ini.


## Installing AMX Mod X
  1. Go to www.amxmodx.org and click "Downloads". Download the amxmodx-base package for either Windows or Linux.
  2. Extract the base package to your mod folder. This will place AMX Mod X into <mod folder>\addons\amxmodx. If you're uploading over FTP, you should extract it to a dummy location first (like your desktop).
  3. Go back to the AMX Mod X download site. If there is an addon pack for your mod available, and you want to use it, download the addon package corresponding to your mod. As of this writing, addon packs are available for Counter-Strike/Condition-Zero, Team Fortress Classic, Day of Defeat, The Specialists, Natural Selection, and Earth's Special Forces. Make sure you download the pack that corresponds to the server's operating system, either Windows, Linux, or Linux.
  4. Extract the addon pack to the same place as before, it should simply add more files to your AMX Mod X installation.
  5. If you're using FTP, upload the addons folder.
  6. AMX Mod X should now be installed! You can type "meta list" in your [server console](https://wiki.alliedmods.net/Server_console "Server console") to see if it was successful.
  7. You can now move on to [Configuring AMX Mod X](https://wiki.alliedmods.net/Configuring_AMX_Mod_X "Configuring AMX Mod X"). If you encountered problems, see [Troubleshooting AMX Mod X](https://wiki.alliedmods.net/Troubleshooting_AMX_Mod_X "Troubleshooting AMX Mod X").


