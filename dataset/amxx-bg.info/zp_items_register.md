# zp_items_register
#### Syntax
```
native zp_items_register(const name[], cost)
```

#### Usage
name | ```Caption to display on the menu.```
---|---
cost | ```Cost to display on the menu.```
#### Description
```
Registers a custom item which will be added to the extra items menu of ZP.

Note: The returned item ID can be later used to catch item
selection events for the zp_item_select_() forwards.
```

#### Return
```
An internal item ID, or ZP_INVALID_ITEM on failure.
```


This code is a part of zp50_items.inc. To use this code you should include zp50_items.inc as ```#include <zp50_items>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.