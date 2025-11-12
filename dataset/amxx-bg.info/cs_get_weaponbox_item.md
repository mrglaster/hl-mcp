# cs_get_weaponbox_item
#### Syntax
```
native cs_get_weaponbox_item(weaponboxIndex);
```

#### Usage
weaponboxIndex | ```Weaponbox entity index```
---|---
#### Description
```
Returns the weapon entity index that was packed into a weaponbox.
```

#### Return
```
Weapon entity index on success or 0 if no weapon can be found
```

#### Error
```
If a non-weaponbox entity is provided or the entity is invalid, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).