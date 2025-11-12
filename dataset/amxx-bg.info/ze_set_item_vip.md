# ze_set_item_vip
#### Syntax
```
native ze_set_item_vip(iItemid, szFlag[]);
```

#### Usage
iItemid | ```Item id.```
---|---
szFlag | ```Flag to set item to: a, b, c ... etc.```
#### Description
```
Description:      Set this item for VIPs on specific flag.
```

#### Return
```
true          | If set successfully for VIPs.
ZE_WRONG_ITEM | If this itemid is invalid.
```

#### Note
```
Use this under ze_register_item() native in plugin_init() forward.
To use this native VIP plugin must be installed.
Make sure to use only one flag.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed