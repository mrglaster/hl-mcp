# zp_items_get_real_name
#### Syntax
```
native zp_items_get_real_name(itemid, real_name[], len)
```

#### Usage
classid | ```A valid item ID.```
---|---
name | ```The buffer to store the string in.```
len | ```Character size of the output buffer.```
#### Description
```
Returns an item's real name (used when registering the item).
```

#### Return
```
True on success, false otherwise.
```


This code is a part of zp50_items.inc. To use this code you should include zp50_items.inc as ```#include <zp50_items>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.