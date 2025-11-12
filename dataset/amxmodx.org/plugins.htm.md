. Plugins
  

Content:
  * [Installing Plugins](http://127.0.0.1:8000/content/plugins.htm#install)
  * [Removing Plugins](http://127.0.0.1:8000/content/plugins.htm#remove)
  * [Default Plugins](http://127.0.0.1:8000/content/plugins.htm#default)
  * [Troubleshooting](http://127.0.0.1:8000/content/plugins.htm#help)
  * [Porting AMX Mod Plugins](http://127.0.0.1:8000/content/plugins.htm#port)
  * [Compiling Plugins](http://127.0.0.1:8000/content/plugins.htm#compile)

  
**Installing Plugins**
  1. Follow any directions the plugin author has given you. If the plugin requires extra steps or special files, make sure you have them in the proper place and order.
  2. If you are given a .sma source file, you must compile it. [Click here](http://127.0.0.1:8000/content/plugins.htm#compile) to find out how to compile plugins.
  3. Place the plugin's .amxx file in the addons\amxmodx\plugins folder.
  4. Add the plugin's name to addons\configs\plugins.ini. Example:```
myplugin.amxx
```

  5. Restart the server or change maps. If the plugin has any load errors, see below.

  
**Removing Plugins**
  * Remove the entry from addons\amxmodx\configs\plugins.ini by deleting it or prepending a semi-colon to comment it out.
  * Delete any associated files.

  
**Default Plugins** Plugin Name | Purpose  
---|---  
admin.amxx | Administration Base  
admin_sql.amxx | Administration Base for SQL. Use only one base.  
admincmd.amxx | Basic administration commands (such as kick/slap).  
adminhelp.amxx | Help for admin commands.  
adminslots.amxx | Slot reservation.  
multilingual.amxx | Multi-Lingual client configuration.  
menufront.amxx | Front-end for admin menus.  
cmdmenu.amxx | Command menu for settings.  
plmenu.amxx | Player menu commands (kick, ban, etc).  
telemenu.amxx | Teleport Menu (fun module required).  
mapsmenu.amxx | Maps menu (vote, changeleve, etc).  
adminchat.amxx | Console-based chat commands.  
antiflood.amxx | Prevents clients from flooding the say chat.  
scrollmsg.amxx | Displays a scrolling message.  
imessage.amxx | Displays a centered, timed information message.  
adminvote.amxx | Voting commands.  
nextmap.amxx | Displays next map in the mapcycle.  
mapchooser.amxx | Allows players to vote for the next map.  
timeleft.amxx | Displays time left on the current map.  
pausecfg.amxx | Allows pausing/unpausing of plugins.  
statscfg.amxx | Configuration of statistical plugins.  
  
**Troubleshooting**  
  
**Q: What does "function not found" mean?**  
  
A: Your plugin requires a module which you have not enabled. Make sure you followed the plugin author's instructions. If there were none supplied, you can use these methods to find the module you need to enable: Look at the plugin's source code (.sma file). There will be lines like this:  
```
  #include <amxmodx>
  #include <amxmisc>
  #include <engine>
  #include <fakemeta>

```
These last two lines mean "Engine module" and "Fakemeta module".  
Also, some modern plugins will have sections like this:  
```
  public plugin_modules()
  {
  	require_module("engine")
	require_module("fakemeta")
  }

```
These each correspond to one module that must be enabled.  
  
Lastly, you can see if the function is in the scripting database at <http://www.amxmodx.org/funcwiki.php>  
If all of these options fail, search the forums or contact the plugin developer.  
  
**Q: What does "module required for plugin" mean?**  
A: This means you do not have the specified module enabled. As the error says, you should open addons\amxmodx\configs\modules.ini and enable it.  
  
**Q: What does "Run time error ... debug not enabled" mean?**  
A: This means an internal error occured in the plugin. To enable debug mode, you can do one of two things: 
  1. Change the "amx_debug" cvar in amxx.cfg to one of the following values:  
0 - No debugging  
1 - See option 2 below  
2 - All plugins in debug mode  

  2. Change the entry in addons\amxmodx\configs\plugins.ini to have debug enabled. For example, change something 

like:  
```
myplugin.amxx
```
to:  
```
myplugin.amxx debug
```
You should the contact the plugin author with the debug output when the error occurs again.  
  
**Q: I am a plugin developer. How can I use the debugging system?**  
A: See the [scripting section](http://127.0.0.1:8000/scripting/debug.htm) for more information on this.   
  
**Porting AMX Mod Plugins**   
In order to port AMX Mod plugins to AMX Mod X, you should first try simply recompiling them. Many function names have changed so you can't run them directly. If the compilation is successful, but the plugin doesn't work, read on.  
  
If the re-compilation or plugin did not work, you must assess the source code.  

  * Is the plugin from AMX Mod 0.9.9+? It may use new or unportable natives, such as _T() or other crap.
  * Does the plugin use unported modules? There are some modules so outdated, closed source, or poorly made that they were not ported, and never will be. These modules are:
    * UDP
    * MThread
    * D2Tools
    * Misc
    * Tazmod
    * CMath
    * pvPrivateData
  * Luckily, these modules are rarely used because of the reasons listed above.
  * Are you using AMX Mod X 0.20? The functionality for MySQL and some other idiosyncracies (such as set_task) changed significantly, which could render some plugins unportable without editing the source code.
  * Does the plugin use VexD forwards? The handling, nature, and/or names of some forwards changed from AMX Mod to AMX Mod X 0.16, and again to 0.20. Make sure that they are being used correctly.
  * Is the author still around? See if they are willing to help you.

If you do complete a successful port, you should have the author's permission before distributing it. If you do distribute it, you must use the GNU General Public License as the plugins are linked to AMX Mod X.   
  
**Compiling Plugins**   
  
_Windows:_  
  
Place the .sma source file in addons\amxmodx\scripting.  
Method 1: Quick 
  1. Drag the .sma file onto "compile.exe".
  2. Look in the compiled folder for the output .amxx file.

Method 2: Compile All (Quick) 
  1. Double click compile.exe to compile all plugins into the compiled folder.

Method 3: Command Line 
  1. Go to Start, Run, type "cmd", click Ok.
  2. Use cd to change to the directory, I.e.: ```
  cd c:\hlserver\cstrike\addons\amxmodx\scripting

```

  3. Use amxxsc to compile the plugin: ```
  amxxsc.exe myplugin.sma

```

  4. The output will be in the same folder.

_Linux_   
  
Copy or move the .sma file into addons/amxmodx/scripting.  
Then change the directory to the scripting folder with:  
```
  cd addons/amxmodx/scripting

```
  
Method 1: Compile all 
  1. Run the script compile.sh by either: ```
  sh compile.sh

```
Or: ```
  chmod +x compile.sh
  ./compile.sh

```


Method 2: Compile single 
  1. ```
  ./amxxsc myplugin.sma

```
The output will be in the same folder.


