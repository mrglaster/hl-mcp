# rg_remove_items_by_slot
#### Syntax
```
native rg_remove_items_by_slot(const index, const InventorySlotType:slot, const bool:removeAmmo = true);
```

#### Usage
index | ```Client index```
---|---
slot | ```The slot that will be emptied```
removeAmmo | ```Remove ammunition```
#### Description
```
Remove all the player's stuff in a specific slot.
```

#### Return
```
1 - successful removal of all items in the slot or the slot is empty
0 - if at least one item failed to remove
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.