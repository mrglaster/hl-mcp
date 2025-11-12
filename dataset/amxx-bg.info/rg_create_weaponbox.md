# rg_create_weaponbox
#### Syntax
```
native rg_create_weaponbox(const pItem, const pPlayerOwner, const modelName[], Float:origin[3], Float:angles[3], Float:velocity[3], Float:lifeTime, bool:packAmmo);
```

#### Usage
pItem | ```Weapon entity index to attach```
---|---
pPlayerOwner | ```Player index to remove pItem entity (0 = no weapon owner)```
modelName | ```Model name ("models/w_*.mdl")```
origin | ```Weaponbox origin position```
angles | ```Weaponbox angles```
velocity | ```Weaponbox initial velocity vector```
lifeTime | ```Time to stay in world (< 0.0 = use mp_item_staytime cvar value)```
packAmmo | ```Set if ammo should be removed from weapon owner```
#### Description
```
Spawn a weaponbox entity with its properties
```

#### Return
```
Weaponbox ent index on success, AMX_NULLENT (-1) otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.