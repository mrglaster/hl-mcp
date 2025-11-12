. Counter-Strike
Sections:
  * [Configuration](http://127.0.0.1:8000/content/cstrike.htm#config)
  * [Plugins](http://127.0.0.1:8000/content/cstrike.htm#plugins)
  * [Modules](http://127.0.0.1:8000/content/cstrike.htm#modules)

**CVAR Config**   
  
To edit these options, open addons\amxmodx\configs\amxx.cfg with your favorite text editor.   
  
CVAR | Default Setting | Purpose  
---|---|---  
csstats_rank | 1 | Sets the rank player mode for CSX. Options:  
0 - By name  
1 - By SteamID  
2 - By IP Address  
csstats_maxsize | 3500 | Maximum size of the CSX stats file.  
amx_statsx_duration | 12.0 | Duration of HUD statistics.  
amx_statsx_freeze | -2.0 | HUD statistics display limit relative to round freeze end. Negative values will clear the HUD before the round freezetime has ended.  
  
**Plugins** Plugin Name | Purpose  
---|---  
restmenu.amxx | Weapon Restriction Menu  
statsx.amxx | Statistics Generation (such as end of death/round stats) - Requires CSX  
miscstats.amxx | Events announcement for Counter-Strike (requires CSX)  
stats_logging.amxx | Weapon stats logging (requires CSX)  
  
**Modules** Module Name | Purpose  
---|---  
cstrike_amxx | Adds scripting functionality to modify aspects of Counter-Strike  
csx_amxx | CSSTATS replacement - statistics generation and other events
