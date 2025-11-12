. Introduction: Features
Content:
  * [Features](http://127.0.0.1:8000/content/features.htm#features)
  * [Features for Developers](http://127.0.0.1:8000/content/features.htm#developers)


a) Features
  * Administration system
  * Scripting/plugin system
  * Module expansion system
  * Basic admin commands, such as: 
    * Banning, kicking
    * Slap/slay
    * Chat
    * Reserve slot control
    * Flood protection
    * Weapon restriction
    * Statistics (in the style of StatsMe)
  * Dynamic menu system


b) Features for Developers
AMX Mod X has an integrated development API that can connect modules to Metamod and AMX Mod X. This easy, contained environment provides debugging, memory leak tracking, and rapid toolkit development.  
With over 600 native functions and an easily expandable and interfaceable M/SDK, AMX Mod X is perfect for creating quick server solutions without having to muck around with the annoying details of making a Metamod plugin or an archaic AMX Mod module.  
  
Plugins have the following advantages: 
  * Registering client/console commands
  * Hooking almost all GameDLL and HL Engine functions
  * Calling almost all GameDLL and HL Engine functions
  * Catching and modifying events
  * Easily extracting information from entities and global settings
  * Creating/modifying CVARs
  * Interfacing to PostgreSQL, MySQL, or MS-SQL
  * Using TCP and UDP socket functions
  * Regular Expressions
  * New debugging system with stack trace support
  * Creation of in-game menus
  * Easy to use multi-lingual system
  * Architecture independent format (.amxx)
  * Game-specific natives for CS/CZ, DoD, TFC, TS, and NS
  * ... and more!

Modules have the following advantages: 
  * Contained environment for tracking memory allocations
  * M/SDK that eliminates the need for .def files or outside explicit includes such as "modules.h"
  * Interface that is both forwards and backwards compatible, using a "request function by name" system.
  * Functions to interface with the AMX Mod X core, for general tasks such as getting internal player information and manipulating plugin data.
  * Modules use a router interface from Metamod called "FakeMeta", therefore they are contained from Metamod but compatible with it.


