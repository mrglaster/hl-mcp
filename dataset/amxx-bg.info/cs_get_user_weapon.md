# cs_get_user_weapon
#### Syntax
```
native cs_get_user_weapon(playerIndex, &clip = 0, &ammo = 0);
```

#### Usage
playerIndex | ```Player index```
---|---
clip | ```Optional variable to store clip ammo to```
ammo | ```Optional variable to store backpack ammo to```
#### Description
```
Returns weapon index of the active weapon.
```

#### Note
```
More reliable than get_user_weapon.
```

#### Return
```
Weapon index on success or 0 if there is no active weapon
```

#### Error
```
If the client index is not within the range of 1 to
maxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).