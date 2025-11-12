# ns_get_hive_ability
#### Syntax
```
native ns_get_hive_ability(idPlayer, ability=0);
```

#### Usage
idPlayer | ```The player index to look up.```
---|---
ability | ```The ability number to check, set to 0 to get number of active hives.```
#### Description
```
Returns 1 if a player has the hive ability number.
If ability is 0, it will return the number of active hives.
```

#### Return
```
If ability is != 0, returns 1 or 0 depending on if the client has the ability.
If ability is 0, returns the number of active hives.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).