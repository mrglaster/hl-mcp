. Configuration: Menus
There are a number of menu configuration files for the administration in-game menus. Click each of the menus to see how to configure them. 
Menus:
  * [Client Commands](http://127.0.0.1:8000/content/menus.htm#clcmds)
  * [Commands](http://127.0.0.1:8000/content/menus.htm#cmds)
  * [Configs](http://127.0.0.1:8000/content/menus.htm#config)
  * [CVARs](http://127.0.0.1:8000/content/menus.htm#cvar)
  * [Speech](http://127.0.0.1:8000/content/menus.htm#speech)

**Client Commands Menu**  
File: | addons\amxmodx\configs\clcmds.ini  
---|---  
Format: | "Name" "Command" "Flags" "Access Level"  
Options: | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.   
Flags are one of the following:  
a - execute from server console  
b - execute from admin console  
c - execute on selected player  
d - display menu again once done  
Example: | "Slay player" "amx_slay #%userid%" "bd" "u"  
  
**Commands Menu**  
File: | addons\amxmodx\configs\cmds.ini  
---|---  
Format: | "Name" "Command" "Flags" "Access Level"  
Options: | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.   
Flags are one of the following:  
a - execute from server console  
b - execute from admin console  
c - execute on selected player  
d - display menu again once done  
Example: | "Pause" "amx_pause" "bd" "u"  
  
**Server Configs Menu**  
File: | addons\amxmodx\configs\configs.ini  
---|---  
Format: | "Name" "Command" "Flags" "Access Level"  
Options: | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.   
Flags are one of the following:  
a - execute from server console  
b - execute from admin console  
c - execute on selected player  
d - display menu again once done  
Example: | "PUBLIC Settings" "servercfgfile server.cfg;exec server.cfg" "a" "u"  
  
**CVARs Menu**  
File: | addons\amxmodx\configs\cvars.ini  
---|---  
Format: | "CVAR" "Values" ... "Access Level"  
Options: | CVAR - the CVAR's name  
Values - list of space delimited, quotation enclosed values   
Example: | "mp_autoteambalance" "0" "1" "@" "u"  
  
**Speech Menu**  
File: | addons\amxmodx\configs\speech.ini  
---|---  
Format: | "Name" "Command" "Flags" "Access Level"  
Options: | Name is the name that will appear on the menu.  
Command is the format for the console command - you can use %userid% to insert the user's id.   
Flags are one of the following:  
a - execute from server console  
b - execute from admin console  
c - execute on selected player  
d - display menu again once done  
Example: | "Hello!" "spk \'vox/hello\'" "cd" "u"
