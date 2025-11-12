# zp_register_extra_item
#### Syntax
```
native zp_register_extra_item(const name[], cost, teams)
```

#### Usage
name | ```Caption to display on the menu.```
---|---
cost | ```Ammo packs to be deducted on purchase.```
teams | ```Bitsum of teams it should be available for.```
#### Description
```
Registers a custom item which will be added to the extra items menu of ZP.

Note: The returned extra item ID can be later used to catch item
purchase events for the zp_extra_item_selected() forward.

Note: ZP_TEAM_NEMESIS and ZP_TEAM_SURVIVOR can be used to make
an item available to Nemesis and Survivors respectively.
```

#### Return
```
An internal extra item ID, or -1 on failure.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed