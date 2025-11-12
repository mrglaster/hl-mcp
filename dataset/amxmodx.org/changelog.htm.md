. Changelog
Versions:
  * AMX Mod X:
  * [1.60 (September 18, 2005)](http://127.0.0.1:8000/content/changelog.htm#1.60)
  * [1.55 (August 24, 2005)](http://127.0.0.1:8000/content/changelog.htm#1.55)
  * [1.50 (August 1, 2005)](http://127.0.0.1:8000/content/changelog.htm#1.50)
  * [1.01 (March 09, 2005)](http://127.0.0.1:8000/content/changelog.htm#1.01)
  * [1.00 (November 14, 2004)](http://127.0.0.1:8000/content/changelog.htm#1.00)
  * [0.20-RC7 (October 29, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.7)
  * [0.20-RC6 (September 20, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.6)
  * [0.20-RC5 (September 12, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.5)
  * [0.20-TP4 (September 2, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.4)
  * [0.20-TP3 (August 24, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.3)
  * [0.20-TP2 (August 22, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.20.2)
  * [0.16 (March 26, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.16)
  * [0.15 (March 15, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.15)
  * [0.10 (March 08, 2004)](http://127.0.0.1:8000/content/changelog.htm#0.1)
  * AMX Mod:
  * [0.9.7](http://127.0.0.1:8000/content/changelog.htm#0.9.7)
  * [0.9.6](http://127.0.0.1:8000/content/changelog.htm#0.9.6)
  * [0.9.5](http://127.0.0.1:8000/content/changelog.htm#0.9.5)
  * [0.9.4](http://127.0.0.1:8000/content/changelog.htm#0.9.4)
  * [0.9.3](http://127.0.0.1:8000/content/changelog.htm#0.9.3)
  * [0.9.2](http://127.0.0.1:8000/content/changelog.htm#0.9.2)
  * [0.8.4](http://127.0.0.1:8000/content/changelog.htm#0.8.4)
  * [0.7.3](http://127.0.0.1:8000/content/changelog.htm#0.7.3)
  * [0.7](http://127.0.0.1:8000/content/changelog.htm#0.7)
  * [0.6.1](http://127.0.0.1:8000/content/changelog.htm#0.6.1)
  * [0.6](http://127.0.0.1:8000/content/changelog.htm#0.6)
  * [0.5](http://127.0.0.1:8000/content/changelog.htm#0.5)
  * [0.4](http://127.0.0.1:8000/content/changelog.htm#0.4)

**AMX Mod X 1.60 (September 18, 2005 - Codename "Rusty Mushroom")**
  * Plugins can now query/retrieve client-side cvars (for example, to enforce CVAR rules).
  * Plugins can now use modules and natives without them being loaded. For example, plmenu will use the cstrike module only if it's available, and no recompile is necessary.
  * Plugins can now handle their own errors and look at their own debug traces.
  * Rewrote the debugger from scratch and, in some cases, greatly improved error message output.
  * Numerous other warnings and compiler bugs were removed and/or fixed in this release.
  * Fixed many bugs in AMXx Studio (bringing it to version 1.2).
  * Faluco has reformatted every single original, OLOcode AMX Mod X source code file to be readable! This was a herculean task and we thank him for his time.
  * Made some final improvements to Linux optimization flags.
  * Added is_string_num() (thanks azrael!)
  * Added abs() (requested by Brad Jones)
  * Language files can now have comments with ; or //
  * amx_addadmin in admin.sma will now also add to the SQL database if available (thanks Lazarus Long!)
  * Improved parameters to amx_addadmin so more admin types can be added (thanks Lazarus Long!)
  * Fixed nvault_open() crashing after nvault_close was called on the same file (atambo).
  * Fixed Linux compiler not being able to run from any directory (Lazarus Long).
  * Fixed get_distance_f not being in amxmodx.inc (Greenberet).
  * Fixed trim() function not removing whitespace properly (karlos).
  * Fixed many bugs in the compiler preprocessor and macro preprocessor.
  * Fixed bug in compiler where array indexes were improperly tag-checked.
  * Fixed various array bugs in register_native default style (Lord of Destruction).
  * Fixed dod_get_map_info breaking after a mapchange (FireStorm)..
  * Fixed/rewrote find_ent_by_model in Engine.
  * Fixed MySQL crashing on null fields (And One).
  * Fixed listen servers not getting admin access (jtp10181).
  * Fixed crash bugs in MySQL when querying and caching field names (Striker).
  * Fixed more memory deallocation mismatches with plugins (Zenith77).
  * Fixed get_user_gravity not returning a Float (vittu).
  * Fixed MySQL module not conforming to DBI, causing memory leaks and crashes.
  * Fixed build process and various minor errors in SQLite module (thanks Lazarus Long!)
  * Fixed AMXXRelease releasing no config files on Linux (Gonzo).
  * Fixed permissions problems with AMXXRelease on Linux (hondaman, Arnold).
  * Fixed/reverted functionality of stopping plugins for amx_pausecfg.
  * Fixed plmenu (Player Menu) not swapping or displaying teams correctly after Steam update (KWo)
  * Fixed name clashes in TSFun and TSX modules (Twilight Suzuka).

**AMX Mod X 1.55 (August 24, 2005)**
  * Changed the JIT to prevent possible crashing on pingboost/threading situations on linux (reported by hullu).
  * Compiled with gcc-3.4 instead of 2.95 - binaries should be smaller and faster (thanks hullu). AMX Mod X and the S/MDK will no longer compiler on gcc-2.95
  * Added human readable error messages to many core natives.
  * Added Czech language translation (thanks Fatty).
  * Replaced AMXX Edit with newer AMXX Studio.
  * Replaced ESF module with new ESF plugin from Corona-Bytes.
  * Fixed bug where set_task would run one extra time on "repeat" mode.
  * Fixed bug where plugins could not be unpaused.
  * Fixed bug where bots could not deal damage with Fun module.
  * Fixed linux compiler crashing on load.
  * Fixed crash bug in register_native.
  * Fixed alloc/dealloc mismatches in register_native.
  * Fixed three newmenu functions not being implemented (patched by Freecode).
  * Fixed a bug where CS team switching did not work with plmenu (Steam update consequence).
  * Fixed callfunc_push_str copying zero characters (reported by Lord of Destruction, Twilight Suzuka).
  * Fixed documentation errors about MF_AmxExec* (Twilight Suzuka).

**AMX Mod X 1.50 (August 1, 2005 - Codename "Schnappi Kitten")**
  * Updated Small to version 3.0. Note: ITB CompuPhase has changed the name of Small to "Pawn". This includes an improved and more powerful compiler. You can now return arrays, simulate "structs", and the optimizer has been improved.
  * Large reduce in CPU usage for non-Metamod-p users. AMX Mod X now requires Metamod 1.18 or Metamod-p. Note: this is because we have removed the internal mini-Metamod that was added in 0.20.
  * Added new system for automating multi-page menus.
  * Added module for ESF (Earth's Special Forces), thanks to Lynx.
  * Rewrote installer from scratch, now a much more improved interface that actually works.
  * Added an official "AMX Mod X Editor", AMXX-Edit. To be expanded as AMX Mod X Studio in the future.
  * Rewrote MySQL module (again) - now can be used by other modules.
  * Added new plugin debugging system from Small 3.0. Old plugins need to be recompiled to be debugged.
  * Added "register_native", plugins can now create natives that other plugins can use. This was first conceptualized by dJeyL and added on request of T(+)rget.
  * Changed the plugin file format to be a tad more flexible. Old plugins will still work.
  * Added a module for dealing with binary vaults (nVault).
  * Added another The Specialists module (TSFUN).
  * Deprecated AMX Mod module support, which was incompatible with Small 3.0.
  * Require_module is deprecated. Module detection is now done automatically when you compile plugins.
  * Fixed a serious memory leak in set_task (reported by fysh).
  * Fixed a serious memory leak in entity_set_model (reported by EKS).
  * Fixed deallocation errors in engine and core (reported by theqizmo, OneEyed, and fysh).
  * Added module API changes that require a sync of the SDK. This was to make sure modules had the right Small 3.0 headers. Modules compiled with the old SDK will refuse to load.
  * Added inter-module communication to complement AMX Mod X's inter-plugin communication.
  * Deprecated read_dir, added much faster open_dir natives.
  * Fixed a bug where language settings were mishandled (thanks faluco).
  * Fixed a good deal of language translation-related errors (thanks faluco).
  * Added Spanish, Brazilian translations (thanks faluco, AlucarD_fOx).
  * Fixed bug where repeated tasks actually repeated one less than their given amount (reported by EKS).
  * Fixed bug where bad language translation files could corrupt build_pathname (reported by Kamikaze).
  * Fixed is_user_hltv (thanks Wallslide).
  * Fixed mishandling of user input strings (potential security bug). Reported and diagnosed by Stan Bubrouski.
  * Fixed log_to_file so it logs to the right file (reported by karlos).
  * Fixed bug in the JIT where a lone default case would crash (reported by twistedeuphoria).
  * Fixed bug where client_print to console would not insert newlines (reported by azrael).
  * Added dir_exists (requested by twistedeuphoria).
  * Fixed memory leaks on plugin unload.
  * Deprecated most fget/fput natives (they have been removed), due to improper implementation.
  * Fixed problems with weapon ids in DoDX
  * Fixed problem with setting and retrieving strings with set_pev/pev
  * Updated Regex library from PCRE 4.5 to 6.1.
  * Updated GeoIP database to July 2005
  * Updated Natural-Selection module for latest NS release.
  * Fixed bugs and added new natives to DoDFun.
  * Fixed various bugs in the documentation.
  * Fixed potential problems in register_message, reduced memory usage a bit.
  * Added in_viewcone and can_see, at the request of v3x.
  * Fixed bug in MySQL module where a port could not be added to the connect string (reported by azrael).
  * Added trace_forward at the request of, and by, twistedeuphoria.
  * Added get_distance_f to core at the request of twistedeuphoria.

**AMX Mod X 1.01 (March 09, 2005)**
  * Updated NS module for Natural Selection 3.0.
  * Added new package to maintain unsupported SQL/DBI modules.
  * Added a module for SQL Lite.
  * Added a tool for viewing stats (CS addon).
  * Added optimizations for when using Metamod-p (evilspy).
  * Added mkdir native.
  * Added cs_set/get_user_armor.
  * Added callfunc_begin_i and get_func_id.
  * Added more client menu functionality to menufront.
  * Added a new MySQL module for version 4.1.
  * Updated get_stats to work with authids.
  * Updated and cleaned the funcwiki. (thanks, Avalanche).
  * Fixed logging bug in SDK.
  * Fixed bugs with bots disconnecting.
  * Fixed bugs with uninitialized players disconnecting.
  * Fixed parse bug in strbreak.
  * Fixed typos in config files.
  * Fixed installer when using Condition-Zero.
  * Fixed custom weapons in xmod stuff.
  * Fixed grenade problem in CSX.
  * Fixed mistakes in documentation (breaddawson).
  * Fixed compiling error in adminslots (Firestorm).
  * Fixed a hitzones problem with Fun.
  * Snyced language files.

**AMX Mod X 1.00 (November 14, 2004 - Codename "Kaiserpinguin")**
  * Added an installer.
  * Completed documentation.
  * Added fakemeta_stocks include file.
  * Added PM OnoTo's XS Library.
  * Added natives to array_amxx to check lists for values.
  * Admin.sma will now immediately exec amxx.cfg to make plugin_cfg more useful.
  * Synced language files and added Dutch (thanks Devilion).
  * Increased write-file buffer.
  * Fixed a bug that caused the JIT to crash with a kernel option in 2.6.x.
  * Fixed many Counter-Strike native offsets in Cstrike module.
  * Fixed a crash bug in hooking MESSAGE_BEGIN in Fakemeta_amxx
  * Fixed a bug where admin_sql would not reset admins on fallback to users.ini.
  * Fixed range checking in set_user_hitzones.
  * Fixed read_data() float return method.
  * Fixed version and file info in some modules and core.

**AMX Mod X 0.20-RC7 (October 29, 2004)**
  * Improved plugin error output and debugging greatly.
  * Run time errors of type 10 (AMX_ERR_NATIVE) now display the native's name for clarity.
  * If debug is not enabled and an RTE occurs, instructions on enabling debug mode are printed.
  * Rewrote error reporting for all modules to use new debug trace API.
  * Added get_user_msgname().
  * Added custommenuitems.cfg to standard cfg files.
  * Added ability for plugins to dynamically add items to amxmodmenu.
  * Fixed compiler generating very long file paths for debug information.
  * Fixed error causing amx_client_languages to reverse effects.
  * Fixed error causing floats passed in forwards to mess up everything.
  * Fixed menu mistakes in StatsX.
  * Fixed vote map menu.
  * Fixed missing weapon status in restmenu.
  * Fixed serious bug in forwards that use floats.
  * Fixed bug where message_begin could not send MSG_PAS_R and MSG_PVS_R (Damaged Soul).
  * Fixed crash bug in get_msg_origin (Damaged Soul).
  * Fixed bugs in entity_set_byte and entity_set_edict.
  * Fixed a small bug in mapchooser mapcycle reader (Damaged Soul).
  * Fixed a bug in CSX where get_weaponname was overridden incorrectly.
  * Fixed some bugs in pev() natives in fakemeta module.
  * Fixed client_built forward in NS module.
  * Fixed last hit being ignored in StatsX (JC Denton).
  * Fixed miscstats playing sounds to connecting players.
  * Renamed cs_get_weapon_type to cs_get_weapon_id. 

**AMX Mod X 0.20-RC6 (September 20, 2004)**
  * Added AMD64 support for Cstrike module.
  * Added TraceResult and TraceLine manipulation to fakemeta_amxx.
  * Added new API calls for module SDK.
  * Added new debug trace system to JIT and C core.
  * Added universal error handling API to Core (modules not yet implemented).
  * Removed extraneous packages from DoD, TFC, and TS packages.
  * Fixed a bug in get_user_astats for CSSTATS.
  * Fixed remaining bugs in remove_task().
  * Fixed bug where reloadadmins would not reset flasg (mrhunt).
  * Fixed bug where amxxsc failed on -o <file>.
  * Fixed logging typo in core.ini.
  * Fixed wrong kills and deaths in CSSTATS.
  * Fixed string formatting in mapsmenu, admincmd.
  * Fixed restmenu run time error.
  * Fixed adminslots not calculating slots immediately.
  * Fixed crash bug in amx_modules.
  * Fixed parsing bug in string trim routine.
  * Fixed bug where language files were not closed.
  * Compiler is now set to debug level 2 and compaction is disabled. 

**AMX Mod X 0.20-RC5 (September 12, 2004)**
  * Fixed a bug related to the JIT headers that was causing stats modules to crash.
  * Removed MMGR from default builds.
  * Removed MMGR from default SDK options.
  * Added optimizations to format() routines.
  * Added amx_debug to control plugin run levels.
  * Added ability for plugins to tell Core which modules are needed (requested by mahnsawce).
  * Added new SDK module functions MNF_GetPlayerEdict, MNF_GetPlayerFlags.
  * Added better support for Natural-Selection 3 Beta 5 (mahnsawce, CheesyPeteza, et al).
  * Fixed a bug where %c would not be recognized.
  * Fixed a bug where SQL connections were not disconnected on mapchange (UgLyPuNk).
  * Fixed a bug where MySQL connections could not have a specified port (Mugwump).
  * Fixed a bug where float computations were incorrect on AMD64 (UgLyPuNk).
  * Fixed a bug where entity validation routines in Engine/Fakemeta were incorrect (JJKiller).
  * Fixed a bug where the fakemeta engine could bootstrap a module twice.
  * Fixed a crash bug relating to forward re-registration (fsfod).
  * Fixed a compile bugs in some modules that prevented AMD64 compatibility (UgLyPuNk).
  * Fixed a memory leak related to Engine not unregistering forwards (mahnsawce).
  * Fixed bugs in find_ent* natives which choked on 0 indices (Pimp Daddy).
  * Fixed CVector assertions (fsfod).
  * Fixed get_keyvalue not being a valid native in Engine (Vortox).
  * Fixed include files so formatting Sql or Res variables won't give a tag mismatch (Pimp Daddy).
  * Fixed many include files.
  * Fixed "amx_client_languages" cvar.
  * The command "amxx plugins" will now report plugin load errors that occurred (requested by mahnsawce).
  * The command "amxx version" will now report whether your Core build is normal, ASM, or JIT.
  * Admin_sql now reverts to users.ini on failure (requested by QwertyAccess).
  * SQL configuration CVARs are now enabled by default (Gonzo).
  * Changed is_jit_enabled(): now reports 1 for JIT, 0 for safe, -1 for ASM.
  * Added module load simulator to default linux packages.
  * Module names listed in modules.ini can now be loaded independently of their extension (for example _i386 will search for _amd64 on AMD64, et cetera) (requested by UgLyPuNk).

**AMX Mod X 0.20-TP4 (September 2, 2004)**
  * Changed amxx_mm.* to amxmodx_mm.*
  * Changed "amxx" to "amxmodx" for addons folder.
  * Switched from 2.6.0 compiler to 2.5.1 (2.6.0 is much too buggy).
  * Enabled the JIT on Linux (sorry - Makefile bug showed we hadn't been doing this).
  * Rewrote task system to use Forward API.
  * Added CVAR to multilingual plugin to disable client side options - "amx_client_languages".
  * Fixed a bug in forward API where parameters would be garbage.
  * Fixed crash bugs in Forward API.
  * Fixed many string format crash bugs in amxmodx core.
  * Fixed other string formatting issues such as %% and % being parsed improperly. (reported by Gonzo)
  * Fixed a memory leak on loading amxx plugins.
  * Fixed a bug in the Module SDK header file where structs could be misaligned. (reported by fsfod)
  * Fixed many crash bugs in the MySQL module. (reported by Gonzo)
  * Fixed memory leaks in both Engine and MySQL.
  * Fixed bugs in Engine that caused crashes in DoD and prevented optimization.
  * Fixed message capturing in Engine so it can work with multiple plugins. (reported by fsfod)
  * Fixed plmenu and get_user_team bugs in DoD package and TFC package.
  * Fixed top15 display problems in DoD package.
  * Fixed bug where amx_say would use the ML system.
  * Fixed bug where remove_task() could cause a server crash on shutdown. (reported by Pimp_Daddy)
  * Fixed bug where client_command was not a blockable forward.
  * Fixed bug where radians were not converted properly. (malex)
  * Fixed buffer overflow security holes in string formatting routine (legacy code from AMX Mod)
  * Removed pvPrivateData functions from Engine and placed into Fakemeta_amxx.
  * Added NewDLL HLAPI functions to FakeMeta. (reported by mahnsawce)
  * Greatly improved error reporting for both MySQL and Engine.

**AMX Mod X 0.20-TP3 (August 24, 2004)**
  * Changed .amxx plugin format - changed compression from LZO to GZ  
-Note on the above - old .amxx files will not work, recompile with the new compiler.  
-The compression will be 30-80% better, but that's not the reason for the switch (which was licensing issues)
  * Fixed include files to be more backwards compatible
  * Fixed bad compiling options in both AMD64 and Linux compiles (stdc++ dependencies)
  * -This also fixes a crash bug in the cstrike package and load errors
  * Fixed a very ubiquitous crash bug in MySQL
  * Fixed a crash bug in Core when resolving certain strings
  * Increased compiler line buffer 

**AMX Mod X 0.20-TP2 (August 22, 2004 - Codename "Tiger")**
  * Packages
    * AMX Mod X is now packaged as mod independent. You can download mod packages which enhance
    * Strike (this
    * Zero), Day of Defeat, Natural Selection, The Specialists, and Team Fortress Classic.
    * If you would like to be the maintainer of a mod package, please contact the AMX Mod X Team. Mod
    * The custom dir has been removed. Use the configs folder. get_customdir() will use configs.
    * A "data" folder has been added for binary files. "data/lang" holds language translations.
  * Modules
    * Modules are no longer loaded through Metamod. AMXx acts as a Metamod wrapper for all HL engine
    * The above functionality is called FakeMeta. AMXx in fact treats its own engine calls as an internal Fakemeta plugin.
    * Modules have a new, more complete, Application Programming Interface (API). It is an SDK which allows developers
    * AMXx now loads modules in three formats: amxx, amx, and amx&mm. The configuration file "modules.ini"
    * Listenservers have been finicky with Steam ever since an update which broke AMX 0.9.6j+ API
    * Modules no longer use a specific struct of function pointers. A function request system makes modules,
  * Core
    * The Just In Time Compiler (JIT) is now enabled by default. It translates AMX plugins to native
    * AMX Mod X is fully 64bit compatible. Plugins now end in ".amxx" to reflect a new, 64bit compatible
    * For debuggers/developers, there is now a Memory Test build which will log all memory usage to peroidic
    * There is also a special optimization build for newer processors (not default in packages).
    * Many, many portions of the AMX Mod X core were rewritten from the ground up. This includes various
  * Multi-Lingual
    * AMX Mod X now features an API for multi-lingual development. An intuitive system lets you add language
    * Language definitions are retrieved as multi-layered formatted strings in a system that crosses between
    * The AMX Mod X Plugins have been translated into over 10 languages! Hats off to the translators.
  * MySQL Module
    * SQL support has been heavily changed. The MySQL module was completely rewritten from scratch. Known
    * There is now a universal Database Interface (DBI) which allows for more advanced scripting using
    * such as per-query results, resource handles, and better error
    * The new interface can break backwards compatibility. Old plugins may or may not work, and it's best to
    * There is now a module for PostgreSQL support and Microsoft SQL Server support (Windows only).
  * Engine Module
    * The Engine module was completely rewritten from scratch for a more organized code base.
    * Many natives were merged in from NS2AMX when it was split to form n2_amxx.
    * Engine has been optimized to no longer strain servers like it's original VexD base.
  * CSStats Module
    * Known CSStats issues have been fixed in AMXx's rewrite of CSStatus "CSStats2".
  * NS_amxx Module
    * Mahnsawce has continued his excellent Natural Selection work to port his NS module to AMX Mod X.
  * DoD Modules
    * AMX Mod X comes with DoDX for Day of Defeat Statistics and DoDFun for Day of Defeat scripting.
  * TFCx Module
    * AMX Mod X comes with a Team Fortress Classic statistical package.
  * GeoIP Module
    * The GeoIP module has been ported to AMX Mod X, written from scratch and updated.
  * Array Module
    * A module for advanced array manipulation is now included.
  * Sockets Module
    * A module for network socket manipulation is now included (kenterfie).
  * Fakemeta Module
    * Almost all metamod functionality has been captured into a module for use in Small.
    * Fakemeta module can call, hook, supercede, or block almost every Half-Life engine and DLL function.
    * It also has simplified natives for accessing player private data and edict properties.
    * Fakemeta features the same optimizations as Engine. It won't lag from being idle.
  * Plugins
    * The Admin and Admin_mysql plugins have been merged into one plugin, with a preprocessor directive
    * The Stats plugin has been replaced with XAD's StatsX.
    * Admin_mysql is now admin_sql.
    * All base plugins that detect Counter-Strike will now work on Condition-Zero automatically.
    * Per-map configuration files can be stored as .cfg files on configs/maps, which will be auto-executed on
    * up (admin base).
    * Anti-Flood now more intelligently flood protects (internal increment and decrement counters).
    * The new multi-lingual plugin allows clients to set their own languages for real-time translation.
    * Plugins are now compressed into a new plugin format called ABL - the new extension to reflect this is
    * Normal .amx plugins will not work on the AMD64 version of AMX Mod X - you need to use .amxx
    * A new compiler - amxxsc.exe - is being used. It's a hybrid Small/AMXx compiler.
    * A new batch compiler has been made - compiler.exe for windows.
    * You can now write plugins in AMX Assembly (sasm.exe).
  * Configuration
    * mysql.cfg is now sql.cfg
    * amx_mysql_ CVARs are now named amx_sql_ instead.
    * Slot reservation is no longer default
    * Counter-Strike specific modules, plugins, and settings are no longer default.
    * modules.ini and plugins.ini are now a tad more descriptive.
    * amx_client_languages allows you to select whether clients can use the multilingual system.
  * The list of new natives was removed because it was too long.
  * Core
    * No longer crashes on bad modules
    * Fixed license (GPL now reports properly).
    * Better Condition-Zero support.
    * read_data(0) returns the msgid in events.
    * Removed amx_version cvar.
    * New internal function forwarding system.
    * New Module API fixes old idiosyncracies.
    * Removed many warnings in gcc.
    * New floating point module from ITB Compuphase.
    * Rewrote many portions of the core from scratch.
    * Upgraded to latest abstract machine and added AMD64 compatibility.
  * Cstrike
    * Fixed rare crash bug in all natives (being used before players are initialized).
  * Engine
    * Rewritten from scratch.
    * Fixed memory leaks
    * Fixed message natives.
    * Imported many natives from NS2AMXx.
    * Fixed crash bugs.
  * Fun
    * Now uses the correct, original set_user_hitzones functionality.
  * MySQL
    * Rewritten from scratch, contains a new codebase and operation style.
    * Fixed crash bugs.
  * Plugins
    * Fixed typos in various includes.
    * Added second parameter to amx_help.
    * Changed amx_mode to 1 by default.
    * Fixed access level bugs.
    * Added multi-lingual settings.
  * Core
    * Fixed a possible crash bug where Cmd_Args would return NULL.
    * Fixed type "Dettach" to "Detach".
    * Fixed crash bug on invalid plugin path.
    * Added memory allocation failure checks.
    * Fixed file handles staying open on error.
    * Fixed get_module.
    * Added amxmodx_modules cvar.
    * get_user_weapons sets the third parameter to 0 before counting.
    * cs_set_user_team now updates models/scoreboards right away.
    * cs_set_user_vip changes to the VIP model/updates scoreboard right away.
    * Fixed cs_set_hostage_foll
    * Fixed engclient_cmd.
    * Added md5() functionality.
    * Added some string manipulation.
    * Fixed memory leaks.
  * Fun
    * Added TFC support for give_item.
  * Plugins
    * Fixed a small bug in make_deathmsg.
    * Fixed localinfo for users.ini
    * Fixed if NO_STEAM is defined for adminslots.sma
    * March 15, 2004
    * We are using the old SC 2.1 small compiler.
    * March 08, 2004
    * game stats theme
    * Selection
    * Strike 1.6 maps to maps.ini
    * Strike module and added functions:

**AMX Mod X 0.16 (March 26, 2004 - Codename "Rockzilla")**
  * amx.cfg is now amxx.cfg, in configs dir
  * New folder - custom, for custom configs from 3rd party plugins
  * Fixed conditional event bug in core.
  * Fixed engine get/set_offset_float
  * Fixed engine to have get/set_speak
  * Added jghg2 into engine (with jghg2.inc)
  * Fixed give_item for all mods
  * Fixed amx_plugins command
  * Fixed access levels being random
  * Fixed include files
  * Fixed cstrike having long native lengths
  * Fixed maxspeeds
  * Fixed call_think in engine
  * Added cstrike natives cs_get_weapon_ammo, cs_set_weapon_ammo
  * Cstrike now animates with cs_set_weapon_silen
  * localinfos are back (addons/amxx/core.ini too)
  * Plugins now use localinfo with get_basedir and get_configsdir
  * amx_version / amxmodx_version cvar fixed
  * get_modulesnum native fixed
  * reading from files with weird line breaks should work now
  * NOTE! Plugin writers should store their files in get_configsdir()

**AMX Mod X 0.15 (March 15, 2004 - Codename "Bugzilla")**
  * Fixed event related bugs such as incorrect timing and crashes.
  * Removed all std:: code and lstdc++ requirement.
  * Moved messaging functions back into core from ENGINE
  * Many documentation fixes
  * Added xtrafun support backwards support.
  * TEMPORARY - We are using the old SC 2.1 small compiler.
  * Removed .amx from logging plugin names.
  * Hardcoded directory names into core.
  * get_module also returns status.
  * Fixed logging crashes.
  * Removed get_user_wonid.
  * cs_set_user_vip and cs_get_user_vip fixed.
  * cs_set_user_deaths now updates scoreboard.
  * Fixed ENGINE memory leaks.
  * Fixed register_message argument functions.
  * Fixed controller and blending values.
  * Reduced set_view lag.
  * It is now possible to shoot and break func_breakables.
  * Removed fun cvars and engine cvars and amx_version cvar.
  * Removed FUN debug messages.
  * Added set_user_hitzones and get_user_hitzones.
  * Removed set_hitzones. 

**AMX Mod X 0.10 (March 08, 2004 - Codename "Xerocks")**
  * Imported the initial AMX Mod code base.
  * updated to new Small Abstract Machine and Small Compiler
  * added welcome message for Steam (replaces the default motd)
  * kicking/banning reason is displayed on target player
  * changed amx_ban, amx_banid and amx_banip command
  * mysql table is automatic created
  * mapchange obeys mp_chattime
  * updated in-game stats theme
  * fixed say @... and say_team @... under Natural-Selection
  * only admins can view amx_who
  * added Counter-Strike 1.6 maps to maps.ini
  * added native functions:
    * log_amx( ... )
    * is_module_loaded( ... )
    * get_module( ... )
    * get_modulesnum( ... )
    * is_plugin_loaded( ... )
    * callfunc_begin( ... )
    * callfunc_push_...( ... )
    * callfunc_end( ... )
  * added commands:
    * amx_reloadadmins
    * amx_plugins
    * amx_modules
  * moved some native functions to new Counter-Strike module and added functions:
    * cs_get_hostage_follow( ... )
    * cs_set_hostage_follow( ... )
    * cs_get_hostage_id( ... )
    * cs_get_user_backpackammo( ... )
    * cs_set_user_backpackammo( ... )
    * cs_get_user_defusekit( ... )
    * cs_set_user_defusekit( ... )
    * cs_get_user_inside_buyzone( ... )
    * cs_get_user_model( ... )
    * cs_set_user_model( ... )
    * cs_reset_user_model( ... )
    * cs_get_user_nvgoggles( ... )
    * cs_set_user_nvgoggles( ... )
    * cs_get_user_plant( ... )
    * cs_set_user_plant( ... )
    * cs_set_user_team( ... )
    * cs_get_user_vip( ... )
    * cs_set_user_vip( ... )
    * cs_get_weapon_burstmode( ... )
    * cs_set_weapon_burstmode( ... )
    * cs_get_weapon_silenced( ... )
    * cs_set_weapon_silenced( ... )
  * moved some native functions to new Engine module and added functions:
    * register_message( ... )
    * get_msg_...( ... )
    * set_msg_...( ... )
    * get_offset_...( ... )
    * set_offset...( ... )
    * precache_generic( ... )
    * entity_get_...( ... )
    * entity_set_...( ... )
    * create_entity( ... )
    * find_entity_...( ... )
    * call_think( ... )
    * is_valid_ent( ... )
    * entity_set_origin( ... )
    * entity_set_model( ... )
    * remove_entity( ... )
    * entity_count( ... )
    * fake_touch( ... )
    * DispatchKeyValue( ... )
    * DispatchSpawn( ... )
    * RadiusDamage( ... )
    * VelocityByAim( ... )
    * PointContents( ... )
    * trace_line( ... )
    * trace_normal( ... )
    * vector_to_angle( ... )
    * vector_length( ... )
    * vector_distance( ... )
    * get_grenade_id( ... )
    * halflife_time( ... )
    * set_lights( ... )
    * set_msg_block( ... )
    * get_msg_block( ... )
    * attach_view( ... )
    * set_view( ... )
    * pfn_touch( ... )
    * server_frame( ... )
    * client_kill( ... )
    * client_PreThink( ... )
    * client_PostThink( ... ) 

**AMX Mod 0.9.7**
  * added support for listenservers, all you need is   
"loopback" "" "abcdefghijkmnopqrstu" "de" entry in users.ini file
  * added read_datanum() native function
  * added CS_DeathMsg event which fixes last damage issue
  * added amx_csay command; you can now specify if you want to show  
names with hud messages (to set in plugin sources)
  * added forward client_authorized() called when a client get valid steam id
  * added formating to MOTD window for top15, statsme and rank
  * made adminslots, admin, admin_mysql using client_authorized()
  * removed support for amx_real_res_slots (for HLSW)
  * rebuilded adminslots, fixed hide slots issue; now there is only one  
cvar - amx_reservation (see plugin comments for more details)
  * modules used by AMX don't have to be put in the
  * made that stats in rank are not saved if get_score returns cellmin
  * made read_data() to return values in a requested format  
(should help in debugging since all values can be returned as string)
  * made that on a module error a server exits with a proper message
  * improved commands handling, now high number of commands/AMX plugins  
shouldn't affect a server overload
  * fixed force_unmodified() for files different from "wav" and "mdl"
  * fixed crashes caused by missing plugins with left entries in plugins.ini 
  * fixed that register_cvar() didn't set an initial string for a cvar
  * fixed weapon restriction plugin (now can block buy commands in CS 1.6)
  * removed get_user_wonid() native function
  * for custom rank's points calculation (by default: kills - deaths) you  
must set "csstats_score" localinfo (f.e. to "addons/amx/csstats.amx")

**AMX Mod 0.9.6**
  * fixed entry in "amxmisc.inc" file about a command access
  * fixed admin access when an account was set for an IP
  * fixed cancel vote report in admin vote plugin
  * fixed say /hp and killer displaying in stats plugin
  * brought back old compiler and initializing local variables by default
  * improved compile plugins script for linux
  * fixed parsing names containing '<' and '>' chars with parse_loguser(...) 

**AMX Mod 0.9.5**
  * fixed reserved slots, also not used are hidden now
  * fixed boundary checks
  * fixed pause( ... ) and unpause( ... ) which crash on unknown plugin name
  * fixed pause plugins plugin
  * added stock functions to "amxmisc.inc" and new constants to "amxconst.inc"
    * get_basedir( ... )
    * build_path( ... )
    * show_activity( ... )
    * get_logfile( ... )
  * admin command "amx_plugin" is changed to "amx_pausecfg"
  * added "amx_banid", "amx_banip" and changed "amx_ban"
  * fixed admin logging when name is changed
  * by default compiler doesn't initialize local variables to zero  
(option can be turned on with -z flag)
  * general rewrite/tweak for all default plugins
  * server commands "amx cmds" and "amx cvars" give now more detailed info
  * admin must now have all flags of command to gain an access to it
  * added amx_logdir localinfo which specifies logging directory for  
log_to_file(...) (default plugins has been updated to obey that setting)
  * added "amx_basedir" localinfo by which plugins know a path  
to configuration files (resolves problem with running the same AMX on  
different ports with different settings, accounts and plugins)
  * modified admin, admin_mysql and slots reservation  
plugins to work also on CS 1.6 (you have to edit source first)
  * extended functionality of file_size(...) native
  * added native functions to support public variables (introduced them  
with stats and stats configuration plugins)
    * xvar_exists( ... )
    * get_xvar_id( ... )
    * get_xvar_num( ... )
    * get_xvar_float( ... )
    * set_xvar_num( ... )
    * set_xvar_float( ... )
    * isalpha(...)
    * isdigit(...)
    * isalnum(...)
    * isspace(...)
  * added Miscellaneous Stats plugin for Counter-Strike which constains
    * multikill announcement
    * bomb events
    * killing streak
    * enemy remaining
    * round counter
    * italy bonus kill
    * knife kill
    * headshot kill
    * greanade kill
    * last man
    * double kill
    * player name
  * added some stats to Stats plugin
    * most damage
    * most kills
    * team score
    * rank info

**AMX Mod 0.9.4**
  * fixed that stats are not shown if you survive a round
  * fixed get_user_money(...) under linux in fun module
  * fixed issue with amx_nextmap when mp_chattime was set to 0
  * plugin nextmap chooser uses now maps.ini as configuration file
  * admin_mysql.amx is now a seperate plugin (disable admin.amx)
  * name admin.cfg is changed to amx.cfg
  * admin accounts are moved to users.ini (there is no amx_admin command)
  * logd and udp modules are no more in default package
  * moved changelog.txt to readme.txt
  * replaced adminmenu.amx (amx_menu cmd) with several menus (amxmodmenu cmd)
  * changed nextmap plugin to obey mapcycle (you can still use the old style)
  * in register_menuid(...) you can specify if a menu from outside plugin  
can be grabed by a menu command (fixes serveral problems with voting)
  * added weaponstats2, latency and time logging to stats logging plugin
  * added amx_cancelvote command (removes all tasks with 99889988 id)
  * added "say @ ..." commands to adminchat plugin (CM like)
  * changed amx_ppause command to main amx_plugin (with several options)
  * added two new flags for set_task(...)
  * added cvar csstats_maxsize (by default set to 3500) which  
resets stats when number of entries is reached
  * combined console and menu version of restrict weapons plugin
  * fixed bug in fun module with give_item(...) (thx EJ)
  * added amx_statscfg and amx_statscfgmenu (affects menu front end)  
commands to stats configuration plugin
  * moved amx_dpause and amx_addoption to the main commands amx_plugin and  
amx_statscfg (plugins which use one of these commands have to be edited)
  * added native functions:
    * format_time(...)
    * parse_time(...)
    * get_systime(...)
    * task_exists(...)
    * power(...)
    * sqroot(...)
    * time(...)
    * date(...)
    * tickcount(...)
    * vaultdata_exists(...)
    * get_vaultdata(...)
    * set_vaultdata(...)
    * remove_vaultdata(...)

**AMX Mod 0.9.3**
  * fixed imessage plugin which spamed the server with  
hudmessages when amx_freq_imessage was set to 0
  * fixed pausing first plugin when "amx pause" was called from server console
  * fixed format-string bug in log_message native function which could  
be used to gain a remote shell for people who have access to rcon
  * added get last bullet hit to get_user_origin(...) (added by Mike Cao)
  * added format_args(...) native which formats arguments  
of function to one string
  * cvar csstats_rank sets mode of ranking: 0 by nick, 1 by authid and 2 by ip
  * improved Pause Plugins plugin (added amx_ppause and amx_pausemenu cmds.)
  * added Stats Settings plugin for better server managment  
(use amx_statscfg command from that plugin to enable proper stats)
  * made amx_psay command to be HLSW tool compatible
  * added native functions:
    * is_user_hltv( ... )
    * is_linux_server() 
    * is_dedicated_server()
    * read_dir( ... )
    * read_logdata( ... )
    * read_logargc()
    * read_logargv( ... )
    * parse_loguser( ... )
    * register_logevent( ... )
  * added forward function plugin_log() called on log message
  * you can now specify connecting port in mysql module (added by BigDog)
  * fixed stats plugin which could not display all players in top15 list
  * made admin base plugin to check user access on name change
  * added random direction of slaping in user_slap(...) native

**AMX Mod 0.9.2**
  * added inconsistent file checking for sounds and models to AMX
  * improved searching for target in admin commands
  * removed timeleft/nextmap flood exploit (changed order in plugins.ini)
  * fixed bug with gathering information from user at last slot
  * added cvar csstats_reset to reset stats on map change
  * fixed issue with get_user_team(...) in DOD
  * fixed option under flag "f" in get_players(...)
  * fixed option under flag "k" in find_player(...)
  * improved scrolling messaging (no overflows)
  * fixed bug when task was self-removing during execution
  * moved logs to new folder and changed theirs format (edited plugins are:  
admin, adminchat, admincmd, adminslots, adminvote, mapextend)
  * new plugin: information messages (see admin.cfg for more details)
  * fixed issue in mapextend plugin when on server were no players
  * added more cvars settings to admin.cfg from default plugins
  * fixed admin slots plugin and added new option to it
  * fixed timeleft plugin to not hang up during counting down
  * reduced frequency of notifing by fun module
  * added notifing for health, armor and frags changes
  * new native functions:
    * set_cvar_flags(const cvar[], flags)
    * get_cvar_flags(const cvar[])
    * remove_cvar_flags(const cvar[], flags = -1)
  * new natives for strings:
    * strtolower(string[]) - converts string to lower case
    * strtoupper(string[]) - converts string to upper case
  * combined AMX with MetaSmall so there is only AMX Mod
  * Strings, files and floats modules has been moved to AMX Mod code
  * plugin adminvote uses now cvar to set voting session, so other plugins  
can check if it is still in progress or when was the last vote
  * made admin commands to accept also '#userid' as target
  * amx_ban command works now also on LAN servers
  * changed cfg in menu.cfg to perform an action on player by '#userid'
  * amx_nextmap and amx_timeleft now are visible in server status
  * added amx_show_activity cvar to admincmd plugin and adminvote
  * compiled AMX with newest metamod 1.14 (so it works with CS 1.6)
  * removed execution of amx_vote results
  * added to fun module (only for Counter-Strike):
    * get_user_money(...)
    * set_user_money(...)
  * replaced mapextend plugin with more powerful mapchooser plugin  
(configuration for that plugin is in admin.cfg)
  * added to csstats module
    * get_user_wrstats(...)
  * changed name of function get_user_lstats(...) to get_user_rstats(...)
  * added some constants to amxconst.inc file
  * added amx_unban command to admincmd plugin
  * fixed issue in adminmenu when there were diff. access flags set for  
cvars and server commands
  * fixed fun module to reset rendering on client respawn

**AMX Mod 0.8.4**
  * moved 19 natives, like give_item(...), set_user_rendering(...)  
or set_user_godmode(...), to seperate "fun" module
  * added localinfo for metasmall which specifies metasmall.ini  
(+localinfo ms_metasmall metasmall.ini)
  * removed "Fixed" module from default package
  * changed localinfo amx_plugins and localinfo csstats to be  
specified only by filename and not by full path
  * added csstats.amx plugin by which you can rank players in top15
  * fixed issue with lenght protection on replace native in string module
  * fixed issue with get_clcmd(...) when flag was set to 0
  * you can now specify if modules for metasmall have to be loaded  
only once or initialized on every map change
  * moved operations on files to seperate module for metasmall
  * new flags for function get_players(...):
    * "f" - match with part of name.
    * "g" - ignore case sensitivity.
  * added new functions for metasmall engine:
    * build_pathname
    * get_modname
    * print_console
  * in function get_user_time(...) you may now specify playing time
  * function get_playersnum(...) can now also count connecting players
  * new native functions
    * is_user_connecting(...)
    * get_srvcmd(...)
    * console_print(,...)
    * console_cmd(...)
    * register_concmd(...)
    * get_concmd(...)
    * get_srvcmdsnum(...)
    * get_flags(...)
  * added new include file amxmisc.inc
  * made mysql module to not open new connection each time if such  
already exists but return just its id to use with sql natives
  * fixed reset stats on player connection issue in CSStats module
  * fixed get_pluginsnum() function
  * added "amx cmds" command, displaying server commands registered by plugins
  * made registered server commands case insensitive
  * many improvments and some fixes in default scripts:
    * stats : new cmds say /stats and say /statsme
    * adminvote : fixed bug with votes counting and changed keys
    * welcomemsg : added to default package
    * stats_logging : added to default package
    * adminhelp : added to default package
    * timeleft : timeleft and thetime is announced by voice
    * admincmd : added amx_who, amx_slap, amx_pause and amx_leave
    * adminchat : added server commands and improved amx_chat
    * admin : added amx_default_access
    * adminslots : rebuilded plugin
    * ppause : pause and unpause plugins on the fly
    * general clean up

**AMX Mod 0.7.3**
  * made menus to be mod independent
  * added "amx cvars" command, displaying CVars registered by plugins
  * fixed bug in string module with native add(...)
  * changed way of dealing with no MetaSmall (plugins are just unloaded  
from MetaMod with some info) in AMXMod and CSStats modules
  * fixed crash on calling get_clcmd for command with empty description
  * added localinfo amx_plugins where you can specify filename with  
plugins list to load on HLDS command line  
f.e. +localinfo amx_plugins addons/amx/plugins/plugins.ini
  * added localinfo csstats to specify stats data file:  
+localinfo csstats addons/metasmall/csstats.dat
  * fixed server crash when using plugin_end
  * fixed native remove_task (sometimes not removing tasks properly)
  * moved CS stats to a MetaMod plugin & MetaSmall module  
(has to be defined in addons/metamod/plugins.ini AND in  
addons/metasmall/modules.ini, like AMX)
  * plugins adminchat, admincmd and adminvote can accept WONIDs
  * fixed a syntax error in menu.cfg

**AMX Mod 0.7**
  * added MetaSmall 0.1 engine and modules :
    * string
    * fixed
    * float
    * mysql
  * changed AMX to be both a MetaMod plugin and MetaSmall module
  * changes and fixes in plugins :
    * adminslots : now kicks properly
    * adminvote : added amx_vote_delay cvar (min. time between votes)
    * mapextend : fixed divide by zero
    * admincmd : fixed amx_ban command
    * some other fixes :-)
  * added natives :
    * get_user_godmode(index)
    * set_user_noclip(index)
    * get_user_noclip(index)
    * get_user_wonid(index)
    * mysql_connect(host[],user[],pass[],dbname[],error[],maxlength)
  * new flag in function find_player(...):
    * "l" - ignores case sensitivity
  * fixed natives headers in amxmod.inc :
    * get_stats(index,stats[8],bodyhits[8],name[],len)
    * get_statsnum()

**AMX Mod 0.6.1**
  * fixed linux cvar & float issues that broke many things in 0.6
  * removed avlist plugin
  * added menu.cfg file for adminmenu plugin
  * fixed admin_sql plugin when mysql query couldn't be performed

**AMX Mod 0.6**
  * added forward plugin_end(), which is called just before
  * added formatting in functions like format(dest[],len,text[],...)
  * added native log_to_file(file[])
  * added native get_user_deaths(index)
  * added stats natives :
    * get_user_wstats(index,wpnindex,stats[8],bodyhits[8])
    * get_user_stats(index,stats[8],bodyhits[8])
    * get_user_vstats(index,vic,stats[8],body[8],wpnname[]="",len=0)
    * get_user_astats(index,wpn,stats[8],body[8],wpnname[]="",len=0)
    * reset_user_wnstats(index)
    * get_stats(index,stats[8],bodyhits[8])
    * get_statsnum(index,stats[8],bodyhits[8])
  * added mysql support :
    * native sql_query(query[])
    * native sql_newquery(sql,query[])
    * native sql_nextrow(sql)
    * native sql_getfield(sql,fieldnum,dest[],maxlength)
    * native sql_free(sql)
  * native get_user_team(index, team[]="", len=0) now
  * native get_user_attacker(index,...) also returns hit body part
  * changed parameters list in native set_task(...)
  * changed parameters list in native read_file(...)
  * copied values will always be trunked to given length
  * last parameter in native get_user_ip(index,ip,[],len,p=0) sets
  * if there is less arg to set from parse the error is not raised

**AMX Mod 0.5**
  * added native get_user_weapon(index,&clip,&ammo)
  * added native get_user_ammo(index,weapon,&clip,&ammo)
  * added native get_weaponname(weapon_id,weapon[],iLen)
  * added native get_user_listening(iReceiver,iSender)
  * added native set_user_listening(iReceiver,iSender,bListen)
  * added native get_clcmdsnum( flags = 0)
  * added native get_clcmd(index, flag, cmd[], iLen1, info[], iLen2)
  * added native replace(text[],iLen,what[],with[])
  * added native get_maxplayers()
  * added native get_pluginsnum()
  * added native get_plugin(index,filename[], iLen1, name[],iLen2,  
version[],iLen3,author[],iLen4,status[],iLen5)
  * changed native get_user_weapons(index,iwpns[32],&inum)
  * changed native get_user_attacker(index,&weapon)
  * changed native get_user_origin(index,origin[3],mode=0)
  * changed ADMIN flags in amxconst.inc
  * replaced user_glow with set_user_rendering (more options to set)
  * now when bots join to server, natives client_connect and  
client_putinserver are called
  * native show_motd can now display files (send filename as body parameter)
  * fixed bug in checking length of parameter in read_data
  * fixed bug in parse native where arguments weren't 0 terminated
  * added many administrating/managment scripts

**AMX Mod 0.4**
  * added native engclient_print(id,type,message[], ...)
  * added native parse(text[], ... )
  * added native random_float(Float:a,Float:b)
  * added native random_num(a,b)
  * added native remove_quotes(text[])
  * added native file_exists(text[])
  * added native delete_file(text[])
  * added native read_file(file[],line,text[],iLen)
  * added native write_file(file[],text[],line=-1)
  * added native get_user_attacker(index)
  * added native Float:get_user_aiming(index,&id,&body,dist=9999)
  * added native cvar_exists(cvarname[])
  * added native register_plugin(title[],version[],author[])
  * added server command: amx < command > [ parameter ]
  * changed parameters for native function user_glow(...)
  * changed parameters for native function register_cvar(...)
  * changed flags for find_player(...)
  * changed flags for get_players(...)
  * fixed set_cvar_string/float natives
  * removed native check_user_flags(...)
  * more examples of plugins: admin, mirror damage, last man


