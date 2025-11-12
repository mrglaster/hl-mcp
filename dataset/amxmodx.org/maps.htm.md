. Configuration: Maps
If you use the mapsmenu plugin, you can either use "maps.ini" or "mapcycle.txt" to manage map rotations.  
  
Delete "maps.ini" to use mapcycle.txt, otherwise, simply add a list of map names to maps.ini like so:  
  
```
de_dust
cs_assault
de_aztec

```
  
Et cetera. For each map, you can also add a configuration file that will execute when the map loads. This is useful to set certain settings for 3rd party maps, say, removing the freeze time on fy_iceworld.  
  
To do this, simply create a folder in addons\amxmodx\configs called "maps" and place a .cfg file named after the map with the settings in it, for example, you might have addons\amxmodx\configs\maps\fy_iceworld.cfg:  
  
```
mp_startmoney 16000
mp_freezetime 0
mp_timelimit 20

```

