# cs_set_weapon_burst
#### Syntax
```
native cs_set_weapon_burst(index, burstmode = 1);
```

#### Usage
index | ```Weapon entity index```
---|---
burstmode | ```If nonzero the weapon will be put into burstmode, otherwise the burst mode will be removed```
#### Description
```
Sets the weapon's burst mode.
```

#### Note
```
Only the Glock and Famas can be set to burst fire mode as they are the
only guns in the game that provide such a mode.
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will result in undefined behavior if used on non-weapon
entities.
```

#### Return
```
1 if burst mode set successfully, 0 if entity is not
an applicable weapon
```

#### Error
```
If an invalid entity index or a client index is
provided, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).