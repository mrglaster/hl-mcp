# custom_weapon_add
#### Syntax
```
native custom_weapon_add(const wpnname[], melee = 0, const logname[] = "");
```

#### Usage
wpnname | ```Full weapon name```
---|---
melee | ```If nonzero the weapon will be considered a melee weapon```
logname | ```Weapon short name```
#### Description
```
Adds a custom weapon to the stats system.
```

#### Note
```
The weapon name should be the full display name of the gun such as
"Desert Eagle" while the logname should be "weapon_deagle".
```

#### Return
```
Cusom weapon id (>0) on success, 0 if no more custom weapons
can be added
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).