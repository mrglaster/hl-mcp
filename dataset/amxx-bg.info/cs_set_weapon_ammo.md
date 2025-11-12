# cs_set_weapon_ammo
#### Syntax
```
native cs_set_weapon_ammo(index, newammo);
```

#### Usage
index | ```Weapon entity index```
---|---
newammo | ```New ammo amount```
#### Description
```
Sets the amount of ammo in weapon's clip.
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will result in undefined behavior if used on non-weapon
entities.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index or a client index is provided,
an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).