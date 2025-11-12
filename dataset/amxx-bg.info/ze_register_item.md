# ze_register_item
#### Syntax
```
native ze_register_item(const szItemName[], iCost, iLimit);
```

#### Usage
szItemName[] | ```Item name.```
---|---
iCost | ```Item cost.```
iLimit | ```Item limit.```
#### Description
```
Description:         Register extra-item in the items-menu.
```

#### Return
```
Item id in the menu, if successfully registered.
ZE_WRONG_ITEM | If item name was empty or item already registered.
```

#### Error
```
If player not connected.
```

#### Note
```
ZE_WRONG_ITEM is defined as -1
Limit must be >= 0, 0 means unlimited.
Use this native in plugin_init() forward.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed