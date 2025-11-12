# Upgrading AMX Mod X
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#mw-head), [search](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#p-search)
This document contains information on upgrading AMX Mod X versions. Almost all versions follow the same pattern, although notes on specific versions can be found here as well. If you're upgrading from a very old verison, you will need to stage your upgrade. For example, you must read the upgrade notes for each version in between. 
## Contents
  * [1 All Versions](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#All_Versions)
  * [2 Upgrading to AMX Mod X 1.8.0](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#Upgrading_to_AMX_Mod_X_1.8.0)
  * [3 Upgrading to AMX Mod X 1.76d](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#Upgrading_to_AMX_Mod_X_1.76d)
    * [3.1 From 1.76c](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.76c)
    * [3.2 From 1.76b](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.76b)
    * [3.3 From 1.76a](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.76a)
    * [3.4 From 1.76](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.76)
    * [3.5 From 1.75](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.75)
    * [3.6 From 1.71](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.71)
    * [3.7 From 1.70](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.70)
    * [3.8 From 1.50, 1.55, 1.60](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.50.2C_1.55.2C_1.60)
    * [3.9 From 1.01, 1.00, or 0.20-RC4+](https://wiki.alliedmods.net/Upgrading_AMX_Mod_X#From_1.01.2C_1.00.2C_or_0.20-RC4.2B)


# All Versions
For general upgrades, you should make sure you: 
  * Read the changelog!
  * Replace all binaries. 
    * dlls, modules / *.dll/*.so - This includes amxmodx_mm and all modules.
    * plugins/*.amxx - Any default plugins AMX Mod X comes with.
    * data/GeoIP.dat - If you use GeoIP, make sure you update the database.
  * Replace language files. 
    * data/lang/*.txt - Important to make sure plugins are using the right language phrases.
  * Read the upgrade notes to see any other custom changes needed.
  * If you do scripting locally... 
    * Replace all base include and source files (.inc, .sma).
    * Replace the compiler and its binaries (amxxpc, amxxpc32, amxxpc64).


# Upgrading to AMX Mod X 1.8.0
There are no extra upgrade instructions -- AMX Mod X 1.8.0 should be fully backward compatible with old installations. If you wish to use new configuration features, it is recommended that you merge configuration files on a case-by-case basis. 
# Upgrading to AMX Mod X 1.76d
Instructions for upgrading to AMX Mod X 1.76 from older versions are below. 
## From 1.76c
  * Follow general upgrade instructions. This was a binary-only update.
  * **Backwards Compatibility Warning:** Certain non-GPL plugins will no longer load under AMX Mod X. The "hall of shame" list currently includes: _(note - heuristics updated 3/10)_
    * `czgungame.amxx` by "Live"
  * Changed files:

```
[ALL PACKAGES]
configs/
	core.ini
plugins/
	(all recompiled)

[BASE]
dlls/
	amxmodx_mm
modules/
	fakemeta_amxx
scripting/
	amxmod_compat/
		vexdum.sma
	include/
		amxmod_compat/
			maths.inc
			VexdUM.inc
		amxconst.inc
		amxmisc.inc
		amxmodx.inc
		csx.inc
		dbi.inc
		dodfun.inc
		dodx.inc
		engine.inc
		engine_stocks.inc
		fakemeta.inc
		fakemeta_const.inc
		fakemeta_stocks.inc
		float.inc
		fun.inc
		geoip.inc
		message_const.inc
		message_stocks.inc
		messages.inc
		ns.inc
		ns2amx.inc
		nvault.inc
		sockets.inc
		sqlx.inc
		string.inc
		tfcconst.inc
		tfcx.inc
		tsfun.inc
		tsx.inc
		vector.inc
	amxxpc32.so/dll
	amxxpc64.so/dll
	admin.sma
	adminchat.sma
	admincmd.sma
	pausecfg.sma

[COUNTER-STRIKE]
scripting/
	miscstats.sma
	statsx.sma

[NATURAL SELECTION]
modules/
	ns_amxx
scripting/
	idlekicker.sma

```

## From 1.76b
  * Follow general upgrade instructions. This update was a binary-only update.
  * **Backwards Compatibility Warning:** CSX no longer ranks bots by default. Set csstats_rankbots to 1 to revert this change.
  * Changed files:

```
AMX Mod X Base:
dlls/
	amxmodx_mm
	nvault_amxx
plugins/
	(all recompiled)
scripting/
	admin.sma
	mapschooser.sma
	mapsmenu.sma
	menufront.sma
	pausecfg.sma
	telemenu.sma

	includes/
		amxmodx.inc
		amxconst.inc
		geoip.inc
		sqlx.inc

		amxmod_compat/
			xtrafun.inc

Counter-Strike:
modules/
	csx_amxx
plugins/
	(all recompiled)
scripting/
	restmenu.sma
	statsx.sma


Day of Defeat:
plugins/
	(all recompiled)
scripting/
	stats.sma

	
Natural Selection:
plugins/
	(all recompiled)
scripting/
	nscommands.sma

```

## From 1.76a
  * Follow general upgrade instructions. This update was a binary-only update, except for a language change to statsx.txt.


## From 1.76
  * Follow general upgrade instructions. This update was a binary-only update, except for "common.txt."


## From 1.75
  * Follow general upgrade instructions.
  * You may want to recompile your plugins for new implementations of replace_all() and other stocks, however, 1.76 is a binary only upgrade from 1.75.


## From 1.71
  * Follow general upgrade instructions.
  * Make the following configuration changes: 
    * Recommended: Open configs/sql.cfg. Add the new cvar: 
      * `amx_sql_type "mysql"`
      * _Note: Other option is "sqlite"_
    * Optional: Open configs/modules.ini. 
      * If you are using MySQL or SQLite, or any custom modules, write them down.
      * Replace your old modules.ini with 1.75's stock version.
      * Re-add your custom or SQL modules back in.
  * Optional: Recompile 3rd party plugins. 
    * If you wish to take advantage of some automatic module loading features, plugins will need to be recompiled with the 1.75 compiler. However, all old plugins will work as is.


## From 1.70
  * Follow general upgrade instructions.
  * Make the following configuration changes: 
    * Open configs/core.ini. 
      * Replace the contents with the core.ini from AMX Mod X 1.75.
      * _Note: Make sure to note any custom changes!_
  * Continue by following instructions for 1.71.


## From 1.50, 1.55, 1.60
  * Follow general upgrade instructions.
  * Make sure you have [Metamod](https://wiki.alliedmods.net/Metamod "Metamod") version 1.19 or higher installed.
  * Continue by following instructions for 1.70.


## From 1.01, 1.00, or 0.20-RC4+
  * Follow general upgrade instructions.
  * Recommended: replace all of your scripting tools with the latest versions of includes and the compiler. Then, recompile all of your custom or 3rd party plugins with AMX Mod X 1.75.
  * Continue by following instructions for 1.50/1.55/1.60.


