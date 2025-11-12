# cs_get_weapon_silen
#### Syntax
```
native cs_get_weapon_silen(index);
```

#### Usage
index | ```Weapon entity index```
---|---
#### Description
```
Returns if the weapon is in silenced mode.
```

#### Note
```
Only the USP and M4A1 can return 1 as they are the only guns in the
game that have a silenced fire mode.
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will return incorrect values for non-weapon entities.
```

#### Return
```
1 if the weapon is in silenced mode, 0 otherwise
```

#### Error
```
If an invalid entity index or a client index is provided,
an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).