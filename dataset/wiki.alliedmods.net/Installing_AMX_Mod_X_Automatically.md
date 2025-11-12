# Installing AMX Mod X Automatically
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#mw-head), [search](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#p-search)
This guide will help you install [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") using the automated installer. The automated installer can install to a local server (listen or dedicated) and even servers over FTP. 
## Contents
  * [1 Downloading](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Downloading)
  * [2 Running](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Running)
    * [2.1 Choosing an Install Method](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Choosing_an_Install_Method)
      * [2.1.1 FTP Installations](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#FTP_Installations)
      * [2.1.2 Local Installations](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Local_Installations)
    * [2.2 Upgrading](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Upgrading)
    * [2.3 Addons](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Addons)
  * [3 Finalizing](https://wiki.alliedmods.net/Installing_AMX_Mod_X_Automatically#Finalizing)


# Downloading
  1. The automated installer is downloadable from [AMX Mod X Downloads](http://www.amxmodx.org/downloads.php), under "AMX Mod X Full with Installer".
  2. Run the executable. It will unpack itself and a few tools (such as [AMX Mod X Studio](https://wiki.alliedmods.net/index.php?title=AMX_Mod_X_Studio&action=edit&redlink=1 "AMX Mod X Studio \(page does not exist\)")).


# Running
  * Go to Start, Programs, AMX Mod X, and click on the "AMX Mod X" item. The installer will launch as seen below:

    [File:Installer Setup.jpg](https://wiki.alliedmods.net/index.php?title=Special:Upload&wpDestFile=Installer_Setup.jpg "File:Installer Setup.jpg")
  * Click "Next" to continue.


## Choosing an Install Method
[![Installer Types.jpg](https://wiki.alliedmods.net/images/Installer_Types.jpg)](https://wiki.alliedmods.net/File:Installer_Types.jpg)
You have an option of five different installation types. These are: 
  * Steam Dedicated Server - a server started from your Steam Dedicated Server menu
  * Steam Listen Server - a [listen server](https://wiki.alliedmods.net/Listen_server "Listen server") whereby your client is the server
  * Standalone Server - a local server not started from the steam menu (for example: C:\HLServer)
  * Select mod directory - manual installation selection
  * FTP - your server must be accessed through FTP


  
  
  

### FTP Installations
If you use [FTP](https://wiki.alliedmods.net/FTP "FTP"), you will be presented with a dialog to enter your [FTP](https://wiki.alliedmods.net/FTP "FTP") information. If successful, you will then have to choose your mod folder. In the example on the right, "cstrike" would be selected for "Counter-Strike". Also, make sure to select the correct operating system and verify the addon name. 
[![Installer Passbox.jpg](https://wiki.alliedmods.net/images/Installer_Passbox.jpg)](https://wiki.alliedmods.net/File:Installer_Passbox.jpg)
[File:Installer Checkpath.jpg](https://wiki.alliedmods.net/File:Installer_Checkpath.jpg "File:Installer Checkpath.jpg")   

### Local Installations
[![Installer Modbox.jpg](https://wiki.alliedmods.net/images/Installer_Modbox.jpg)](https://wiki.alliedmods.net/File:Installer_Modbox.jpg)
If you install to a local computer, you will simply get a list of the detected mods. Select which one you want to install to.   

## Upgrading
If an AMX Mod X installation was already detected, you will be asked if you want to upgrade. If you upgrade, only binaries will be updated (your configuration will be preserved). 
[![Installer Detected.jpg](https://wiki.alliedmods.net/images/Installer_Detected.jpg)](https://wiki.alliedmods.net/File:Installer_Detected.jpg)
  

## Addons
After the installation, if your mod has a supported addon package, you will be asked if you want it installed. It is recommended that you choose yes. 
[![Installer Addon.jpg](https://wiki.alliedmods.net/images/Installer_Addon.jpg)](https://wiki.alliedmods.net/File:Installer_Addon.jpg)
  

# Finalizing
After the installation is done, check to make sure AMX Mod X is working by restarted your server and typing "meta list" in the [server console](https://wiki.alliedmods.net/Server_console "Server console"). If it doesn't work, look to [Troubleshooting AMX Mod X](https://wiki.alliedmods.net/Troubleshooting_AMX_Mod_X "Troubleshooting AMX Mod X"). Otherwise, move on to [Configuring AMX Mod X](https://wiki.alliedmods.net/Configuring_AMX_Mod_X "Configuring AMX Mod X"). 
