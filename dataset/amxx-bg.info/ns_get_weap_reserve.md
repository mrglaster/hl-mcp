# ns_get_weap_reserve
#### Syntax
```
native ns_get_weap_reserve(id,weapon);
```

#### Usage
id | ```The player id to check ammo count on.```
---|---
weapon | ```The weapon type to check ammo count for.```
#### Description
```
Gets the player's weapon reserve (backpack ammo) for the specified
type of weapon.
```

#### Note
```
Use player index, not weapon index!
```

#### Return
```
The ammunition count in the player's reserve.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).