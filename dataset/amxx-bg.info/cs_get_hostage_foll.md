# cs_get_hostage_foll
#### Syntax
```
native cs_get_hostage_foll(index);
```

#### Usage
index | ```Hostage entity index```
---|---
#### Description
```
Returns index of the entity that a hostage is following.
```

#### Note
```
Hostages can theoretically follow any entity in the game, so the
returned entity index is not necessarily a client index.
```

#### Return
```
Entity index if hostage is following something, 0 otherwise
```

#### Error
```
If the provided entity index is not a hostage, an error will
be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).