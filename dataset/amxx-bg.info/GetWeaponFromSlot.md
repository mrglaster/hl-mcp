# GetWeaponFromSlot
#### Syntax
```
stock GetWeaponFromSlot( id , iSlot , &iEntity )
```

#### Usage
id: | ```Player id```
---|---
iSlot: | ```Inventory slot you want to get the weaponid from```
&iEntity: | ```Weapon entity id```
#### Description
```
bugsy
http://forums.alliedmods.net/showpost.php?p=1575989&postcount=2

Gets a weapon entity id based on inventory slot.
```

#### Return
```
:             Weapon CSW_* index on success, otherwise 0

Ex: GetWeaponFromSlot(id, 3, iEntity);   // Should return CSW_KNIFE if player has one.
                                  // Knife is always in 3th slot (if not changed with plugin or something);
```


This code is a part of stripweapons.inc. To use this code you should include stripweapons.inc as ```#include <stripweapons>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.