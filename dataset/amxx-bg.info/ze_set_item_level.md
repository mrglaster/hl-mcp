# ze_set_item_level
#### Syntax
```
native ze_set_item_level(iItemid, iLevel);
```

#### Usage
iItemid | ```Item id.```
---|---
iLevel | ```Level must player have to buy this item.```
#### Description
```
Description:      Set this item for specific level.
```

#### Return
```
true          | If level set successfully.
false         | If level < 0 (Failed).
ZE_WRONG_ITEM | If this itemid is invalid.
```

#### Note
```
Use this under ze_register_item() native in plugin_init() forward.
To use this native level plugin must be installed.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed