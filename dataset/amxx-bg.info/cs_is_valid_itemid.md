# cs_is_valid_itemid
#### Syntax
```
stock bool:cs_is_valid_itemid(id, bool:weapon_only = false)
```

#### Usage
id | ```Item id (CSI_* constants)```
---|---
weapon_only | ```If true, only the real weapon ids will be checked, including shield as well```
#### Description
```
Checks whether an item id is not out of bounds.
```

#### Return
```
True if item id is valid, false otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).