# rg_drop_items_by_slot
#### Syntax
```
native rg_drop_items_by_slot(const index, const InventorySlotType:slot);
```

#### Usage
index | ```Client index```
---|---
slot | ```Specific slot for remove of each item.```
#### Description
```
Drop to floor all the player's stuff by specific slot.
```

#### Return
```
1 - successful drop of all items in the slot or the slot is empty
0 - if at least one item failed to drop
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.