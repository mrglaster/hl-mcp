# ze_get_item_cost
#### Syntax
```
native ze_get_item_cost(iItemid);
```

#### Usage
iItemid | ```The item id from ze_register_item() or ze_get_item_id().```
---|---
#### Description
```
Description:         Get item cost (Integer) by it's id.
```

#### Return
```
Item cost     | If item id is valid.
ZE_WRONG_ITEM | If item id is invalid.
```

#### Note
```
ZE_WRONG_ITEM is defined as -1
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed