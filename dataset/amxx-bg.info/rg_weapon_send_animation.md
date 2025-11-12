# rg_weapon_send_animation
#### Syntax
```
native rg_weapon_send_animation(const entity, iAnim, skiplocal = 0);
```

#### Usage
entity | ```Weapon to send animation on owner (> MaxClients) OR player index to send animation (>= 1 & <= MaxClients).```
---|---
iAnim | ```Weapon view model animation to play (use HLMV to see anim index)```
skiplocal | ```If 0, weapon animation will be forced to play on client ignoring active client prediction.```
#### Description
```
Sends a weapon animation using the CBasePlayerWeapon::SendWeaponAnim function.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.