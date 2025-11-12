# rg_weapon_kickback
#### Syntax
```
native rg_weapon_kickback(const entity, Float:up_base, Float:lateral_base, Float:up_modifier, Float:lateral_modifier, Float:up_max, Float:lateral_max, direction_change);
```

#### Usage
entity | ```Weapon to reload (> MaxClients) OR player index to reload his current active weapon (>= 1 & <= MaxClients).```
---|---
up_base | ```Minimum vertical punchangle```
lateral_base | ```Minimum horizontal punchangle```
up_modifier | ```Vertical punchangle units to multiply to m_iShotsFired member```
lateral_modifier | ```Horizontal punchangle units to multiply to m_iShotsFired member```
up_max | ```Maximum vertical punchangle```
lateral_max | ```Maximum horizontal punchangle```
direction_change | ```Probability to change punchangle orientation (positive or negative). 0 = 100% (1/1), 1 = 50% (1/2), 2 = 33.3% (1/3), ...```
#### Description
```
Emits a "recoil" effect on weapon's player using the CBasePlayerWeapon::KickBack function.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.