# grenade_throw
#### Syntax
```
forward grenade_throw(index, greindex, wId);
```

#### Usage
index | ```Client index```
---|---
greindex | ```Grenade entity index```
wId | ```Weapon id```
#### Description
```
Called after a grenade was thrown.
```

#### Note
```
Weapon id is one of CSW_HEGRENADE, CSW_SMOKEGRENADE or CSW_FLASHBANG.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).