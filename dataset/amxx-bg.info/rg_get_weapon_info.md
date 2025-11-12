# rg_get_weapon_info
#### Syntax
```
native any:rg_get_weapon_info(any:...);
```

#### Usage
weapon | ```name or id      Weapon id, see WEAPON_* constants, WeaponIdType or weapon_* name```
---|---
WpnInfo:type | ```Info type, see WI_* constants```
#### Description
```
Returns specific information about the weapon.
```

#### Note
```
weapon_* name can only be used to get WI_ID
```

#### Return
```
Weapon information
```

#### Error
```
If weapon_id or type are out of bounds, an error will be thrown
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.