. Natural Selection
Sections:
  * [Configuration](http://127.0.0.1:8000/content/ns.htm#config)
  * [Plugins](http://127.0.0.1:8000/content/ns.htm#plugins)
  * [Modules](http://127.0.0.1:8000/content/ns.htm#modules)

**CVAR Config**   
  
To edit these options, open addons\amxmodx\configs\amxx.cfg with your favorite text editor.   
  
CVAR | Default Setting | Purpose  
---|---|---  
amx_mapnum_ignore | 0 | Sets whether to ignore the minimum and maximum settings for maps in the mapcycle.  
amx_idle_time | 120 | Time players must be idle in order to be kicked  
amx_idle_min_players | 8 | Minimum number of players on the server before kicking starts  
amx_idle_ignore_immunity | 1 | Sets whether to kick idle admins with immunity  
amx_unstuck_frequency  | 4 | Sets the frequency in seconds that a player can say /stuck to free themselves.  
  
**Plugins** Plugin Name | Purpose  
---|---  
idlekicker.amxx | Kicks idle players  
nscommands.amxx | Extra commands for Natural-Selection  
unstuck.amxx | Free stuck players (Engine and NS modules required!)  
  
**Modules** Module Name | Purpose  
---|---  
ns_amxx | Adds many Natural-Selection related functions
