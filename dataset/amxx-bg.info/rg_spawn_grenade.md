# rg_spawn_grenade
#### Syntax
```
native rg_spawn_grenade(WeaponIdType:weaponId, pevOwner, Float:vecSrc[3], Float:vecThrow[3], Float:time, TeamName:iTeam, usEvent = 0);
```

#### Usage
weaponId | ```WEAPON_HEGRENADE, WEAPON_SMOKEGRENADE, WEAPON_FLASHBANG or WEAPON_C4```
---|---
pevOwner | ```Grenade owner```
vecSrc | ```Grenade spawn position```
vecThrow | ```Grenade velocity vector```
time | ```Grenade explosion time```
iTeam | ```Grenade team, see TEAM_* constants```
usEvent | ```Event index related to grenade (returned value of precache_event)```
#### Description
```
Spawn a grenade (HEGrenade, Flashbang, SmokeGrenade, or C4)
```

#### Return
```
Entity index on success, AMX_NULLENT (-1) otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.