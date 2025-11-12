# rg_weapon_reload
#### Syntax
```
native rg_weapon_reload(const entity, iClipSize, iAnim, Float:fDelay);
```

#### Usage
entity | ```Weapon to reload (> MaxClients) OR player index to reload his current active weapon (>= 1 & <= MaxClients).```
---|---
iClipSize | ```Weapon max clip to check. 0 = weapon max clip stored in ItemInfo```
iAnim | ```Weapon view model animation to play (often "reload", use HLMV to see anim index)```
fDelay | ```Player reload duration before clip refill.```
#### Description
```
Reloads a weapon or a player's active weapon using the CBasePlayerWeapon::DefaultReload function.
```

#### Return
```
1 on successful weapon reload, 0 otherwise.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.