# ze_select_item_pre
#### Syntax
```
forward ze_select_item_pre(id, iItemid, bIgnoreCost);
```

#### Usage
id | ```Client index.```
---|---
iItemid | ```Index of item he try to buy.```
bIgnoreCost | ```True has ignore the cost, False will not ignore cost.```
#### Description
```
Description:         Called when player opens the extra-items menu.
                     Or when he choose the item but before he get it.
```

#### Return
```
ZE_ITEM_AVAILABLE   | Shows item in the menu, player can also buy it.
ZE_ITEM_UNAVAILABLE | Show to player but he can't but it.
ZE_ITEM_DONT_SHOW   | Item not appear to that player.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed