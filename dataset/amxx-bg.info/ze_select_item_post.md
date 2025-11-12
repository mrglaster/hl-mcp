# ze_select_item_post
#### Syntax
```
forward ze_select_item_post(id, iItemid, bIgnoreCost);
```

#### Usage
id | ```Client index.```
---|---
iItemid | ```Index of item he try to buy.```
bIgnoreCost | ```true will ignore the cost, false will not ignore cost.```
#### Description
```
Description:         Called after player choose the item,
                     called only if ze_select_item_pre() returned ZE_ITEM_AVAILABLE.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed