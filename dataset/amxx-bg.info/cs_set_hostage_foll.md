# cs_set_hostage_foll
#### Syntax
```
native cs_set_hostage_foll(index, followedindex = 0);
```

#### Usage
index | ```Hostage entity index```
---|---
followedindex | ```New entity to follow```
#### Description
```
Sets hostage to follow an entity.
```

#### Note
```
Hostages can theoretically follow any entity in the game, so the
followedindex does not have to be a client index.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the provided entity index is not a hostage, an
error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).