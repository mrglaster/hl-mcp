# cs_get_item_id
#### Syntax
```
native any:cs_get_item_id(const name[], &CsWeaponClassType:classid = CS_WEAPONCLASS_NONE);
```

#### Usage
name | ```Alias or classname```
---|---
classid | ```If item is a weapon, variable to store the associated weapon class id in (CS_WEAPONCLASS_* constants)```
#### Description
```
Returns the item id associated with an item name and its aliases.
```

#### Note
```
The item name is case sensitive an can be with or without
weapon_ and item_ prefixes. This can be a command alias as well.
Values examples: ak47, weapon_ak47, kevlar, item_kevlar, vest, bullpup, ...
```

#### Return
```
Item id (CSI_* constants)
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).