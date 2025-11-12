# cs_get_user_weapon_entity
#### Syntax
```
native cs_get_user_weapon_entity(playerIndex);
```

#### Usage
playerIndex | ```Player index```
---|---
#### Description
```
Returns active weapon entity.
```

#### Return
```
Weapon entity index on success or 0 if there is no active weapon
```

#### Error
```
If the client index is not within the range of 1 to
maxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).