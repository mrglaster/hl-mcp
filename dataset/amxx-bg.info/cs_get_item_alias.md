# cs_get_item_alias
#### Syntax
```
native bool:cs_get_item_alias(itemid, name[], name_maxlen, altname[] = "", altname_maxlen = 0);
```

#### Usage
itemid | ```Item id (CSI_* constants)```
---|---
name | ```Buffer to store alias name to```
name_maxlen | ```Maximum buffer size```
altname | ```Optional buffer to store if available alternative alias name to```
altname_maxlen | ```Maximum buffer size```
#### Description
```
Returns the alias name associated with an item index.
```

#### Return
```
True if alias is found, false otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).