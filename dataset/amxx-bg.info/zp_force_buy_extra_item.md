# zp_force_buy_extra_item
#### Syntax
```
native zp_force_buy_extra_item(id, itemid, ignorecost = 0)
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


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed