# zp_fw_items_select_pre
#### Syntax
```
forward zp_fw_items_select_pre(id, itemid, ignorecost)
```

#### Usage
id | ```Player index.```
---|---
itemid | ```Internal item ID.```
ignorecost | ```Whether item cost should be ignored.```
#### Description
```
Called when determining whether an item should be available to a player.

Possible return values are:
 - ZP_ITEM_AVAILABLE (show in menu, allow selection)
 - ZP_ITEM_NOT_AVAILABLE (show in menu, don't allow selection)
 - ZP_ITEM_DONT_SHOW (don't show in menu, don't allow selection)
```


This code is a part of zp50_items.inc. To use this code you should include zp50_items.inc as ```#include <zp50_items>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.