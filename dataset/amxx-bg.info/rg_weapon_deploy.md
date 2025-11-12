# rg_weapon_deploy
#### Syntax
```
native rg_weapon_deploy(const entity, const szViewModel[], const szWeaponModel[], iAnim, const szAnimExt[], skiplocal = 0);
```

#### Usage
entity | ```Weapon to deploy. Must be attached to a player.```
---|---
szViewModel | ```Weapon view model name ("models/v_*.mdl")```
szWeaponModel | ```Weapon world model bame ("models/p_*.mdl")```
iAnim | ```Weapon view model animation to play (often "deploy", use HLMV to see anim index)```
szAnimExt | ```Player anim extension name to assign. Examples: "carbine", "shotgun", "knife", etc. Use HLMV on a player model to see animext names.```
skiplocal | ```If 0, weapon animation will be forced to play on client ignoring active client prediction.```
#### Description
```
Deploys a weapon attached to a player using the CBasePlayerWeapon::DefaultDeploy function.
```

#### Return
```
1 on successful weapon deploy, 0 otherwise.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.