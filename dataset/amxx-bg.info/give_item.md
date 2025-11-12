# give_item
#### Syntax
```
native give_item(index, const item[]);
```

#### Usage
index | ```Client index```
---|---
item | ```Classname of the item to give. Should start with either "weapon_", "ammo_", "item_" or "tf_weapon_"```
#### Description
```
Gives an item to a player.
```

#### Return
```
Item entity index. If an invalid item name is
given or the item failed to create, it will return 0.
If the item was removed, it will return -1
```

#### Error
```
If player is not connected or not within the range
of 1 to MaxClients or item creation fails.
```


This code is a part of fun.inc. To use this code you should include fun.inc as ```#include <fun>```


  
  

