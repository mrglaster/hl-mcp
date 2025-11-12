# rg_set_weapon_info
#### Syntax
```
native rg_set_weapon_info(const {WeaponIdType,_}:weapon_id, WpnInfo:type, any:...);
```

#### Usage
weapon_id | ```Weapon id, see WEAPON_* constants```
---|---
type | ```Info type, see WI_* constants```
#### Description
```
Sets specific weapon info values.
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.