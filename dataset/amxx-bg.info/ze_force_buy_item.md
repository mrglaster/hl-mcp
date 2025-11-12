# ze_force_buy_item
#### Syntax
```
native ze_force_buy_item(id, iItemid, bIgnoreCost);
```

#### Usage
id | ```Client index.```
---|---
iItemid | ```Item id, returned by ze_register_item() or ze_get_item_id().```
bIgnoreCost | ```true will ignore the cost, false will not ignore cost.```
#### Description
```
Description:         Force player to buy specific extra-item.
```

#### Return
```
true  | If successfully bought item.
false | If this player not connected or itemid is invalid.
```

#### Error
```
If player not connected.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed