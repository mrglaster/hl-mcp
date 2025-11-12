# cs_get_weapon_id
#### Syntax
```
native cs_get_weapon_id(index);
```

#### Usage
index | ```Weapon entity index```
---|---
#### Description
```
Returns the weapon id of an entity.
```

#### Note
```
For a list of possible weapon ids see the CSW_* constants in
amxconst.inc
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will return incorrect values for non-weapon entities.
```

#### Return
```
Weapon id
```

#### Error
```
If an invalid entity index or a client index is provided,
an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).