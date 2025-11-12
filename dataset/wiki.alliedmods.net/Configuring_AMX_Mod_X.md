# Configuring amx mod x
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#mw-head), [search](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#p-search)
**Warning:** This template (and by extension, language format) should not be used, any pages using it should be switched to [Template:Languages](https://wiki.alliedmods.net/Template:Languages "Template:Languages")  
---  
**View this page in:** English [Russian](https://wiki.alliedmods.net/index.php?title=Ru:Configuring_amx_mod_x&action=edit&redlink=1 "Ru:Configuring amx mod x \(page does not exist\)") [简体中文(Simplified Chinese)](https://wiki.alliedmods.net/index.php?title=Zh_cn:Configuring_amx_mod_x&action=edit&redlink=1 "Zh cn:Configuring amx mod x \(page does not exist\)") |   
  

## Contents
  * [1 Admins](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Admins)
  * [2 Plugins](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Plugins)
    * [2.1 Installing](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Installing)
    * [2.2 Removing](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Removing)
    * [2.3 Default Plugins](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Default_Plugins)
  * [3 Modules](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Modules)
    * [3.1 Installing](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Installing_2)
    * [3.2 Removing](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Removing_2)
    * [3.3 Default Modules](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Default_Modules)
  * [4 CVARs](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#CVARs)
  * [5 SQL](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#SQL)
  * [6 Maps](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Maps)
    * [6.1 Map Cycle](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Map_Cycle)
    * [6.2 Map Config Files](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Map_Config_Files)
    * [6.3 Map Specific Plugins](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Map_Specific_Plugins)
  * [7 Menus](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Menus)
    * [7.1 Client Commands](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Client_Commands)
    * [7.2 Commands](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Commands)
    * [7.3 Configs](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Configs)
    * [7.4 CVARs](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#CVARs_2)
    * [7.5 Speech](https://wiki.alliedmods.net/Configuring_AMX_Mod_X#Speech)


# Admins
See the section on [Adding Admins](https://wiki.alliedmods.net/Adding_Admins_\(AMX_Mod_X\) "Adding Admins \(AMX Mod X\)") for more information. 
# Plugins
## Installing
Often, plugins will have their own directions if they need special installation requirements. However, this will instruct you on the basics of adding a plugin. 
  1. Follow any directions the plugin author has given you. If the plugin requires extra steps or special files, make sure you have them in the proper place and order.
  2. If you are given a .sma source file instead of a .amxx, you must compile the plugin yourself. For more information, see [Compiling Plugins (AMX Mod X)](https://wiki.alliedmods.net/Compiling_Plugins_\(AMX_Mod_X\) "Compiling Plugins \(AMX Mod X\)").
  3. Place the plugin's .amxx file in the addons/amxmodx/plugins folder.
  4. Add the plugin's name to addons\amxmodx\configs\plugins.ini. Example: ```
myplugin.amxx
```

  5. Change map or restart the server. If the plugin has any load errors, see [Troubleshooting AMX Mod X](https://wiki.alliedmods.net/Troubleshooting_AMX_Mod_X#Plugins "Troubleshooting AMX Mod X").


## Removing
  1. Remove the entry from addons\amxmodx\configs\plugins.ini by deleting it or prepending a semi-colon to comment it out.
  2. Delete any associated files.


## Default Plugins      Plugin  | Purpose   
---|---  
admin.amxx  | Administration Base   
admin_sql.amxx  | Administration Base for SQL. Use only one base.   
admincmd.amxx  | Basic administration commands (such as kick/slap).   
adminhelp.amxx  | Help for admin commands.   
adminslots.amxx  | Slot reservation.   
multilingual.amxx  | Multi-Lingual client configuration.   
menufront.amxx  | Front-end for admin menus.   
cmdmenu.amxx  | Command menu for settings.   
plmenu.amxx  | Player menu commands (kick, ban, etc).   
telemenu.amxx  | Teleport Menu (fun module required).   
mapsmenu.amxx  | Maps menu (vote, changeleve, etc).   
adminchat.amxx  | Console-based chat commands.   
antiflood.amxx  | Prevents clients from flooding the say chat.   
scrollmsg.amxx  | Displays a scrolling message.   
imessage.amxx  | Displays a centered, timed information message.   
adminvote.amxx  | Voting commands.   
nextmap.amxx  | Displays next map in the mapcycle.   
mapchooser.amxx  | Allows players to vote for the next map.   
timeleft.amxx  | Displays time left on the current map.   
pausecfg.amxx  | Allows pausing/unpausing of plugins.   
statscfg.amxx  | Configuration of statistical plugins.   
# Modules
Modules add additional functionality for plugins to use. 
## Installing
  1. Figure out what operating system your server is: Windows, Linux, or Linux using AMD64 (64bit).
  2. If the module is 3rd party, download the module corresponding to your OS. It will end in .dll for Windows, _i386.so for Linux, or _amd64.so for AMD64.
  3. Place the file in addons/amxmodx/modules/ and follow any additional instructions.
  4. If the module is already in addons/amxmodx/configs/modules.ini, remove the ';' next to its name to enable it.
  5. Otherwise, add the module's name to modules.ini. [AMX Mod X](https://wiki.alliedmods.net/AMX_Mod_X "AMX Mod X") supports generic notation, for example: ```
mysql_amxx
```
... will automatically detect the correct module to use.
  6. To see if the module is working, you can type `amxx modules` in your [server console](https://wiki.alliedmods.net/Server_console "Server console").


## Removing
  1. Remove the entry from addons\amxmodx\configs\modules.ini by deleting it or prepending a semi-colon to comment it out.
  2. Delete any associated files if you don't need them.


## Default Modules      Module  | Purpose   
---|---  
fun_amxx  | General functions for changing game values.   
engine_amxx  | More advanced functions for getting and setting values in the HL engine.   
fakemeta_amxx  | Expert/advanced functions for manipulating, hooking, and calling functions in the HL engine.   
*sql_amxx  | SQL/Database scripting functions.   
geoip_amxx  | Functions for finding countries by IP address.   
array_amxx  | Functions for somewhat-dynamic arrays.   
sockets_amxx  | Functions for socket (TCP/UDP) control and manipulation.   
regex_amxx  | Functions for regular expression support.   
  

# CVARs
The base [CVARs](https://wiki.alliedmods.net/index.php?title=CVAR&action=edit&redlink=1 "CVAR \(page does not exist\)") AMX Mod X defines are located in amxmodx/configs/amxx.cfg. You can edit these the same way you edit the server.cfg file:       CVAR  | Default Setting  | Purpose   
---|---|---  
amx_default_access  | "z"  | Sets the default access level for non-admin players.   
amx_password_field  | "_pw"  | Name of the setinfo key which a user should store their password in.   
amx_mode  | 1  | Changes the mode of logging into a server:  
0 - Disable logging, players won't be checked and no access will be given.  
1 - Normal mode which obeys flags set in accounts.  
2 - Kick all players not on the users list.   
amx_show_activity  | 2  | Sets the mode of admin activity on the server:  
0 - Disabled  
1 - Show action anonymously  
2 - Show action with the admin's name   
amx_scrollmsg  | "Welcome to %hostname% -- This server is using AMX Mod X" 600  | Sets the parameters (message and frequency) for a scrolling message.   
amx_imessage  | "Welcome to %hostname" "000255100"   
"This server is using AMX Mod X\nVisit <http://www.amxmodx.org>" "00010025"  | Adds a center-typed colored message. The last parameter is in RRRGGGBBB format (red, green, blue).   
amx_freq_imessage  | 180  | Frequency, in seconds, of the colored center messages.   
amx_flood_time  | 0.75  | Chat flood prevention. Sets how fast a player can chat (in seconds).   
amx_reservation  | 0  | Sets the amount of reserved slots.   
amx_time_display  | "ab 1200" "ab 600" "ab 300" "ab 180" "ab 60" "bcde 11"  | Sets flags for remaining time display:  
a - Display white text on bottom  
b - Use voice  
c - Don't add "remaining" in voice  
d - Don't add "hours/minutes/seconds" in voice  
e - Show/speak if current time is less than set in parameter   
amx_time_voice  | 1  | Sets whether to announce "say thetime" and "say timeleft" with voice.   
amx_vote_delay  | 10  | Sets the minimum delay in seconds between two voting sessions.   
amx_vote_time  | 10  | Sets how long a voting sessions lasts for.   
amx_vote_answers  | 1  | Displays who votes for which options, publically.   
amx_voteban_ratio  | 0.40  | Ratio for a ban vote to be successful.   
amx_votekick_ratio  | 0.40  | Ratio for a kick vote to be successful.   
amx_votemap_ratio  | 0.40  | Ratio for a map vote to be successful.   
amx_vote_ratio  | 0.40  | Ratio for a general vote to be successful.   
amx_extendmap_max  | 90  | Maximum time a mapvote can be extended.   
amx_extendmap_step  | 15  | Amount of time a map extensions adds.   
amx_client_languages  | 1  | Enables or disables the ability for clients to choose their own language.   
amx_debug  | 1  | Sets the debug mode for plugins:  
0 - No debugging (warning messages for plugin errors)  
1 - Plugins with "debug" option in plugins.ini are put into debug mode.  
2 - All plugins are put into debug mode (full backtraces for errors).  
Note that debug mode greatly decreases JIT performance.   
amx_mldebug  | 0  | Logs multi-lingual translation problems.   
  

# SQL
Make sure you have mysql_amxx enabled in AMX Mod X's amxmodx/configs/modules.ini file. 
Then, open amxmodx/configs/sql.cfg and edit the cvars accordingly:       CVAR  | Default Setting  | Purpose   
---|---|---  
amx_sql_host  | "127.0.0.1"  | IP address of SQL server.   
amx_sql_user  | "root"  | Username to connect to the SQL server.   
amx_sql_pass  | ""  | Password to connect to the SQL server.   
amx_sql_db  | "amx"  | Database to use on the SQL server.   
amx_sql_table  | "admins"  | The table to use for the admin_sql plugin.   
amx_sql_type  | "mysql"  | The database type to connect to.   
  * Note: amx_sql_type as of AMXX 1.75


# Maps
## Map Cycle
If you use the mapsmenu plugin, you can either use "maps.ini" or "mapcycle.txt" to manage map rotations. 
Delete "maps.ini" to use mapcycle.txt, otherwise, simply add a list of map names to maps.ini like so: 
```
; Maps configuration file
; File location: $moddir/addons/amxmodx/configs/maps.ini
; To use with Maps Menu plugin

; Add in your mod's maps here
; Delete this file to use mapcycle.txt

as_oilrig
cs_747
cs_assault
cs_backalley
cs_estate
cs_havana
cs_italy
cs_militia
cs_office
cs_siege
de_airstrip
de_aztec
de_cbble
de_chateau
de_dust
de_dust2
de_inferno
de_nuke
de_piranesi
de_prodigy
de_storm
de_survivor
de_torn
de_train
de_vertigo

```

  * Note: This is the default maps.ini for the CS package 1.76d


## Map Config Files
For each map, you can also add a configuration file that will execute when the map loads. This is useful to set certain settings for 3rd party maps, say, removing the freeze time on fy_iceworld. 
To do this, simply create a folder in amxmodx/configs called "maps" and place a .cfg file named after the map with the settings in it, for example, you might have amxmodx/configs/maps/fy_iceworld.cfg: 
```
mp_startmoney 16000
mp_freezetime 0
mp_timelimit 20
sv_downloadurl "http://YourFastDownload1.com/cstrike"  //for different Download URL other then default 

```

Be sure to include the following line into your server.cfg. This ensures that you go back (or fall back on) to your default server settings. It is suggested that anything you place in custom config files are also put in your server.cfg or amxx.cfg (at default settings) for best use of this feature. 
```
mapchangecfgfile server.cfg

```

As of [AMX Mod X 1.8.0](https://wiki.alliedmods.net/AMX_Mod_X_1.8.0_Changes "AMX Mod X 1.8.0 Changes"), you are now able to create config files for map prefixes. To do this, create a file called prefix_<prefix>.cfg, where <prefix> would mean de, cs, awp, surf, ect. All prefix config files go in the same location as per map, the amxmodx/configs/map/ directory. 
```
configs/maps/prefix_de.cfg  - Would run on any de_* map.
configs/maps/prefix_cs.cfg  - Would run on any cs_* map.

```

Configuration files are map prefix first (prefix_de.cfg) and map configuration second (de_dust2.cfg). 
For Counter-Strike, you can restrict certain weapons using these config files. It requires the restmenu.amxx plugin to be enabled on your server (usually is by default). You can find more information on how to do this here. 
<http://forums.alliedmods.net/showthread.php?t=6516>
## Map Specific Plugins
Each map can have a specific plugins.ini file for which it will load on map change. This plugins file will be loaded in addition to the standard plugins.ini file. 
The file is to be located at _amxmodx/configs/maps/plugins-mapname.ini_ For example, for de_dust you would create the file **amxmodx/configs/maps/plugins-de_dust.ini**
In addition, a plugin can be tagged as "_disabled_ " which will prevent this plugin from being loaded. You accomplish this the same way you tag a plugin as debug mode, by entering the word _disabled_ after the plugin name in the file, which will prevent it from being loaded for that map. 
For example, if you wanted the map de_dust to disable the plugin _ham.amxx_ and enable the plugin _pickle.amxx_ you would put this in _amxmodx/configs/maps/plugins-de_dust.ini_ : 
```
ham.amxx disabled
pickle.amxx

```

**Note:** This feature was added in [AMX Mod X 1.76](https://wiki.alliedmods.net/AMX_Mod_X_1.76_Changes "AMX Mod X 1.76 Changes")
As of [AMX Mod X 1.8.0](https://wiki.alliedmods.net/AMX_Mod_X_1.8.0_Changes "AMX Mod X 1.8.0 Changes"), you are now able to create plugin.ini files for map prefixes. To do this, create a file called plugins-<prefix>.ini, where <prefix> would mean de, cs, awp, surf, ect. All prefix config files go in the same location as per map, the amxmodx/configs/map/ directory. 
```
configs/maps/plugins-de.ini - Would enable/disable any plugins for all de_* maps.

```

Plugin based configuration files are loaded by map first (plugins-de_nuke.ini) and prefix second (plugins-de.ini). 
# Menus
## Client Commands      File:  | addons\amxmodx\configs\clcmds.ini   
---|---  
Format:  | "Name" "Command" "Flags" "Access Level"   
Options:  | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.  
Flags are one of the following:  
```
 a - execute from server console.  

 b - execute from admin console.  

 c - execute on selected player.  

 d - display menu again once done

```
  
Example:  | "Slay player" "amx_slay #%userid%" "bd" "u"   
## Commands      File:  | addons\amxmodx\configs\cmds.ini   
---|---  
Format:  | "Name" "Command" "Flags" "Access Level"   
Options:  | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.  
Flags are one of the following:  
```
 a - execute from server console.  

 b - execute from admin console.  

 c - execute on selected player.  

 d - display menu again once done

```
  
Example:  | "Pause" "amx_pause" "bd" "u"   
## Configs      File:  | addons\amxmodx\configs\configs.ini   
---|---  
Format:  | "Name" "Command" "Flags" "Access Level"   
Options:  | Name is the name that will appear on the menu.  
Command is the format for the console command. Flags are one of the following:  
```
 a - execute from server console.  

 b - execute from admin console.  

 d - display menu again once done

```
  
Example:  | "PUBLIC Settings" "servercfgfile server.cfg;exec server.cfg" "a" "u"   
## CVARs      File:  | addons\amxmodx\configs\cvars.ini   
---|---  
Format:  | "CVAR" "Values" ... "Access Level"   
Options:  | CVAR - the CVAR's name  
Values - list of space delimited, quotation enclosed values   
Example:  | "mp_autoteambalance" "0" "1" "@" "u"   
## Speech      File:  | addons\amxmodx\configs\speech.ini   
---|---  
Format:  | "Name" "Command" "Flags" "Access Level"   
Options:  | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.  
Flags are one of the following:  
```
 a - execute from server console  

 b - execute from admin console  

 c - execute on selected player  

 d - display menu again once done

```
  
Example:  | "Hello!" "spk \'vox/hello\'" "cd" "u"   
