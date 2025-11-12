# ze_get_item_name
#### Syntax
```
native ze_get_item_name(iItemid, const szName[], iLen);
```

#### Usage
iItemid | ```Item id to check.```
---|---
szName[] | ```String to copy the string name to.```
iLen | ```The string szName[] max length.```
#### Description
```
Description:     Return the item name by it's id.
```

#### Return
```
true          | If item name copied successfully to szName[] string.
ZE_WRONG_ITEM | If this itemid is invalid.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed