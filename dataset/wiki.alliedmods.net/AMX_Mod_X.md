# AMX Mod X
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/AMX_Mod_X#mw-head), [search](https://wiki.alliedmods.net/AMX_Mod_X#p-search)
[![Comment](https://wiki.alliedmods.net/images/Info-icon.png)](https://wiki.alliedmods.net/File:Info-icon.png "Comment") |      This project is owned by the Consortium that controls this wiki. Changes to this main page are allowed but patrolled.  
---|---  
## Contents
  * [1 Introduction](https://wiki.alliedmods.net/AMX_Mod_X#Introduction)
  * [2 Feature List](https://wiki.alliedmods.net/AMX_Mod_X#Feature_List)
  * [3 History](https://wiki.alliedmods.net/AMX_Mod_X#History)
  * [4 Milestones](https://wiki.alliedmods.net/AMX_Mod_X#Milestones)
    * [4.1 0.10-alpha](https://wiki.alliedmods.net/AMX_Mod_X#0.10-alpha)
    * [4.2 0.16-beta](https://wiki.alliedmods.net/AMX_Mod_X#0.16-beta)
    * [4.3 1.00](https://wiki.alliedmods.net/AMX_Mod_X#1.00)
    * [4.4 1.50](https://wiki.alliedmods.net/AMX_Mod_X#1.50)
  * [5 Development Team](https://wiki.alliedmods.net/AMX_Mod_X#Development_Team)
    * [5.1 Original](https://wiki.alliedmods.net/AMX_Mod_X#Original)
    * [5.2 Current](https://wiki.alliedmods.net/AMX_Mod_X#Current)
  * [6 Documentation](https://wiki.alliedmods.net/AMX_Mod_X#Documentation)
  * [7 The Future](https://wiki.alliedmods.net/AMX_Mod_X#The_Future)
  * [8 License](https://wiki.alliedmods.net/AMX_Mod_X#License)
  * [9 External Links](https://wiki.alliedmods.net/AMX_Mod_X#External_Links)


## Introduction
AMX Mod X is a [Metamod](https://wiki.alliedmods.net/Metamod "Metamod") plugin for [Half-Life 1](https://wiki.alliedmods.net/Half-Life_1 "Half-Life 1"). It provides comprehensive scripting for the game engine and its mods. Scripts can intercept network messages, log events, commands, client commands, set cvars, modify entities, and more. AMX Mod X also has a system for extending native scripting through [modules](https://wiki.alliedmods.net/index.php?title=AMX_Mod_X_Modules&action=edit&redlink=1 "AMX Mod X Modules \(page does not exist\)"), leading to outside support for things like MySQL and Sockets. The AMX Mod X scripting language is called [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") (formerly "Small"), and is officially maintained by [ITB CompuPhase](http://www.compuphase.com/). 
## Feature List
  * Creating client and server-side commands and variables
  * Default and customizable server administration tools 
    * Kicking/Banning
    * Slot Reservation
    * Text file or MySQL enabled admin system
    * Voting
    * Management Commands (chat, map changing, cvar changing, etc)
    * Flood Protection
    * Weapon Restriction
    * Statistics
  * Scriptability through large function library 
    * Inter-plugin communication
    * Event listening
    * Network message hooking
    * Entity and engine modification
    * Gamedll and engine function call hooking
    * Sockets
    * Mod-specific extra support for: 
      * Counter-Strike, Condition Zero
      * Day of Defeat
      * Natural Selection
      * Team Fortress Classic
      * The Specialists
      * Earth's Special Forces
    * Regular Expressions
    * Menu Creation
    * Debugger
  * Modularity 
    * Comprehensive M/DK for interacting with scripts
    * Easily attach and use Metamod
    * Plug 'n Use - MDK requires almost no modification to compile
    * Written in C/C++ - total flexibility


[File:Example.jpg](https://wiki.alliedmods.net/index.php?title=Special:Upload&wpDestFile=Example.jpg "File:Example.jpg")
## History
The original AMX Mod project started in 2002 authored by [Aleksander "OLO" Naszko](https://wiki.alliedmods.net/OLO "OLO"). While the same scripting language ([Small](https://wiki.alliedmods.net/Small "Small")) was used as its predecessor admin tool, [Admin-Mod](https://wiki.alliedmods.net/Admin-Mod "Admin-Mod"), the style itself is very different, most likely to correct various confusing or inadequate design decisions. For example: 
  * Focus was on modifying the game, rather than only providing admin tools
  * Easier native syntaxes
  * Easier string manipulation
  * Greater flexibility for hooking game events and commands
  * Greater flexibility for manipulating engine/game
  * Module support for developers to extend native language
  * Easier syntax in general (for example, dropping semicolon requirement)


AMX Mod was originally coupled with [dJeyL](https://wiki.alliedmods.net/DJeyL "DJeyL")'s "[MetaSmall](https://wiki.alliedmods.net/index.php?title=MetaSmall&action=edit&redlink=1 "MetaSmall \(page does not exist\)")", although this was eventually dropped and the two combined into one binary. 
Around January of 2004, various high-ranking members of the AMX Mod community decided the project was in an inactive and dead state. Neither OLO nor dJeyL could be contacted, and [Felix "SniperBeamer" Geyer](https://wiki.alliedmods.net/index.php?title=SniperBeamer&action=edit&redlink=1 "SniperBeamer \(page does not exist\)") decided to found a continuation project named AMX Mod X. 
## Milestones
_For a full list of AMX Mod X and AMX Mod changes, see the[AMX Mod X Changelog](https://wiki.alliedmods.net/AMX_Mod_X_Changelog "AMX Mod X Changelog")._
### 0.10-alpha
The first release of AMX Mod X presented the core new features and organization policies of the overall package, native library, and forums. 
### 0.16-beta
This was the first and most widely used version of AMX Mod X considered to be stable. It contained cleaned up code, inter-plugin communication, a rewritten internal events system, and more. 
### 1.00
Jumped from 0.20, AMX Mod X became a truly different product with a new, advanced module API and many code rewrites, as well as the first Metamod plugin with AMD64 support. AMX Mod X also became the project to port [Small](https://wiki.alliedmods.net/Small "Small") to AMD64. It also gained a very powerful subsystem and module for engine hacking called [Fakemeta](https://wiki.alliedmods.net/index.php?title=Fakemeta&action=edit&redlink=1 "Fakemeta \(page does not exist\)"). 
### 1.50
AMX Mod X followed the renaming of [Small](https://wiki.alliedmods.net/Small "Small") to [Pawn](https://wiki.alliedmods.net/Pawn "Pawn") by [CompuPhase](https://wiki.alliedmods.net/index.php?title=CompuPhase&action=edit&redlink=1 "CompuPhase \(page does not exist\)"). It also added dynamic natives and featured a new debugger. 
## Development Team
### Original
The AMX Mod X development team, founded by SniperBeamer, was: 
  * [Felix "SniperBeamer" Geyer](https://wiki.alliedmods.net/index.php?title=SniperBeamer&action=edit&redlink=1 "SniperBeamer \(page does not exist\)") - Manager, Plugins/Documentation Maintainer, Web Dev
  * [Pavol "PM OnoTo" Marko](https://wiki.alliedmods.net/index.php?title=PM_OnoTo&action=edit&redlink=1 "PM OnoTo \(page does not exist\)") - Lead Developer, Core/VM/Compiler Maintainer
  * [David "BAILOPAN" Anderson](https://wiki.alliedmods.net/User:BAILOPAN "User:BAILOPAN") - General Development, Engine Module, Release Technician
  * [Johnny "JGHG" Bergström](https://wiki.alliedmods.net/index.php?title=Johnny_Got_His_Gun&action=edit&redlink=1 "Johnny Got His Gun \(page does not exist\)") - Cstrike module, Fun module
  * [Lukasz "SidLuke" Wlasinski](https://wiki.alliedmods.net/index.php?title=SidLuke&action=edit&redlink=1 "SidLuke \(page does not exist\)") - Stats modules and extra mod support (TFC, DoD, TFC, TS) _note - SidLuke joined Jul 17, 2005_


### Current
After 1.0 (Nov 15, 2004), the AMX Mod X development team informally disbanded. On January 4, 2006, the development team was officially restructured to continue to maintain and improve AMX Mod X. 
  * [David "BAILOPAN" Anderson](https://wiki.alliedmods.net/User:BAILOPAN "User:BAILOPAN") - Manager, Core/VM/Compiler Maintainer, Release Technician
  * [Christian "Basic-Master" Hammacher](https://wiki.alliedmods.net/User:Basic-Master "User:Basic-Master") - AMXX Studio, AMXX Installer, GabenMod
  * [Borja "faluco" Ferrer](https://wiki.alliedmods.net/index.php?title=User:Faluco&action=edit&redlink=1 "User:Faluco \(page does not exist\)") - General Maintenance/Development, Multi-Lingual Maintenance
  * [Scott "Damaged Soul" Ehlert](https://wiki.alliedmods.net/index.php?title=User:Damaged_Soul&action=edit&redlink=1 "User:Damaged Soul \(page does not exist\)") - General Maintenance/Development
  * [Steve "sawce" Dudenhoeffer](https://wiki.alliedmods.net/User:Sawce "User:Sawce") - General Maintenance/Development


## Documentation
For full documentation on AMX Mod X, see [AMX Mod X Documentation](https://wiki.alliedmods.net/AMX_Mod_X_Documentation "AMX Mod X Documentation"). 
## The Future
AMX Mod X is, for the most part, a finished product. The future holds maintenance, optimizing, further expanding the community as possible, and bug fixing. Features will also usually be added on request. 
## License
AMX Mod X is licensed under the [GNU General Public License](https://wiki.alliedmods.net/GNU_General_Public_License "GNU General Public License"), the parent license of [Metamod](https://wiki.alliedmods.net/Metamod "Metamod"). AMX Mod X also requires that plugins be licensed under the GPL. 
## External Links
  * [The AMX Mod X Website](http://www.amxmodx.org/)
  * [The Metamod Website](http://www.metamod.org/)
  * [The Original AMX Mod Website](http://www.amxmod.net/)
  * [AMX Mod X Forums](http://www.amxmodx.org/forums)


