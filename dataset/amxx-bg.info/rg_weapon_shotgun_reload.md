# rg_weapon_shotgun_reload
#### Syntax
```
native rg_weapon_shotgun_reload(const entity, iAnim, iStartAnim, Float:fDelay, Float:fStartDelay, const pszReloadSound1[] = "", const pszReloadSound2[] = "");
```

#### Usage
entity | ```Weapon to reload (> MaxClients) OR player index to reload his current active weapon (>= 1 & <= MaxClients).```
---|---
iAnim | ```Weapon view model "insert" animation to play (use HLMV to see anim index)```
iStartAnim | ```Weapon view model "start reload" animation to play (use HLMV to see anim index)```
fDelay | ```Delay between each buckshot inserted```
fStartDelay | ```Delay before buckshots insertion starts```
pszReloadSound1 | ```Sound to play on every insertion```
pszReloadSound2 | ```Another sound to play on every insertion```
#### Description
```
Forces shotgun reload thinking on a weapon or a player's active weapon using the CBasePlayerWeapon::DefaultShotgunReload function.
```

#### Note
```
This is used inside weapon's Reload function and is often called every frame player is pressing IN_RELOAD button.
```

#### Return
```
1 while weapon not in delay and with ammo remaining to load, 0 otherwise.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.