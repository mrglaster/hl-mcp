# xmod_is_melee_wpn
#### Syntax
```
native xmod_is_melee_wpn(wpnindex);
```

#### Usage
wpnindex | ```Weapon id```
---|---
#### Description
```
Returns if the weapon is considered a melee weapon.
```

#### Note
```
For a list of default CS weapon ids see the CSW_* constants in
amxconst.inc, this function also works on custom weapons.
```

#### Note
```
For the default CS weapons this obviously returns true only for
CSW_KNIFE.
```

#### Return
```
1 if weapon is a melee weapon, 0
```

#### Error
```
If an invalid weapon id is provided an error will be thrown.
```


This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).