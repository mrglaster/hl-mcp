# rg_add_ammo_registry
#### Syntax
```
native rg_add_ammo_registry(const szAmmoname[]);
```

#### Usage
szAmmoname | ```Ammo name to create.```
---|---
#### Description
```
Generates an ammo slot in game's logic
```

#### Note
```
To see a visual effect, WeaponList message should be sent using the custom ammo name,
where ammo icon HUD will be the one listed in "sprites/weapon_<name>.txt" file.
```

#### Note
```
Maximum ammo index is 31, after that every ammo instantiation will start from 1 overriding existing ones.
```

#### Return
```
New ammo index. If name already exists, will return the matched index from memory.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.