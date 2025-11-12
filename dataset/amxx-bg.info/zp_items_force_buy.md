# zp_items_force_buy
#### Syntax
```
native zp_items_force_buy(id, itemid, ignorecost = false)
```

#### Usage
id | ```Player index.```
---|---
itemid | ```A valid extra item ID.```
ignorecost | ```If set, item's cost won't be deduced from player.```
#### Description
```
Forces a player to buy an extra item.
```

#### Return
```
True on success, false otherwise.
```


This code is a part of zp50_items.inc. To use this code you should include zp50_items.inc as ```#include <zp50_items>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.