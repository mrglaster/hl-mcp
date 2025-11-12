# rg_switch_best_weapon
#### Syntax
```
native rg_switch_best_weapon(const player, const currentWeapon = 0);
```

#### Usage
player | ```Player index.```
---|---
currentWeapon | ```Current player active weapon. 0 = retrieve from m_pActiveItem member```
#### Description
```
Switches player current weapon into the best one on its inventory using the CHalfLifeMultiplay::GetNextBestWeapon function.
```

#### Note
```
Weapon selection is based on weapon's Weight attribute from ItemInfo structure.
```

#### Return
```
1 if weapon was found and switched to, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.