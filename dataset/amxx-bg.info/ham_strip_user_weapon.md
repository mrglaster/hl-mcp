# ham_strip_user_weapon
#### Syntax
```
stock ham_strip_user_weapon(id, iCswId, iSlot = 0, bool:bSwitchIfActive = true)
```

#### Usage
id: | ```Player id```
---|---
iCswId: | ```Weapon CSW_* index```
iSlot: | ```Inventory slot (Leave 0 if not sure)```
bSwitchIfActive: | ```Switch weapon if currently deployed```
#### Description
```
ConnorMcLeod
http://forums.alliedmods.net/showpost.php?p=1109747&postcount=42

Strips a player's weapon based on weapon index.
```

#### Return
```
: 1 on success, otherwise 0

Ex:  ham_strip_user_weapon(id, CSW_M4A1);    // Strips m4a1 if user has one.
     ham_strip_user_weapon(id, CSW_HEGRENADE, _, false);     // Strips HE grenade if user has one
                                                      // without switching weapons.
```


This code is a part of stripweapons.inc. To use this code you should include stripweapons.inc as ```#include <stripweapons>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.