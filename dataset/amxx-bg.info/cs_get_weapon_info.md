# cs_get_weapon_info
#### Syntax
```
native any:cs_get_weapon_info(weapon_id, CsWeaponInfo:type);
```

#### Usage
weapon_id | ```Weapon id, see CSW_* constants```
---|---
type | ```Info type, see CS_WEAPONINFO_* constants```
#### Description
```
Returns some information about a weapon.
```

#### Return
```
Weapon information value
```

#### Error
```
If weapon_id and type are out of bound, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).