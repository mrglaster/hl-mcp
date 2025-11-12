# zp_extra_item_selected
#### Syntax
```
forward zp_extra_item_selected(id, itemid)
```

#### Usage
id | ```Player index of purchaser.```
---|---
itemid | ```Internal extra item ID.```
#### Description
```
Called when a player buys an extra item from the ZP menu.

Note: You can now return ZP_PLUGIN_HANDLED in your plugin to block
the purchase and the player will be automatically refunded.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed