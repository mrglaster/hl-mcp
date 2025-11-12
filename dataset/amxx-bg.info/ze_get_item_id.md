# ze_get_item_id
#### Syntax
```
native ze_get_item_id(const szItemName[]);
```

#### Usage
szItemName[] | ```Item name that used in ze_register_item().```
---|---
#### Description
```
Description:         Get item id by it's name.
```

#### Return
```
Item index    | If item name is valid.
ZE_WRONG_ITEM | If this item name invalid.
```

#### Note
```
ZE_WRONG_ITEM is defined as -1
Item name used in ze_register_item() native,
is called the real item name.
this native deal with real name not name in ze_extraitems.ini
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed