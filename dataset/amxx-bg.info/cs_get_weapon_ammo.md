# cs_get_weapon_ammo
#### Syntax
```
native cs_get_weapon_ammo(index);
```

#### Usage
index | ```Weapon entity index```
---|---
#### Description
```
Returns the amount of ammo in weapon's magazine.
```

#### Note
```
This native does not verify that the provided entity is a weapon
entity. It will return incorrect values for non-weapon entities.
```

#### Return
```
Amount of ammo in magazine
```

#### Error
```
If an invalid entity index or a client index is provided,
an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).