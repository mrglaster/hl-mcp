# ns_set_player_skin
#### Syntax
```
native ns_set_player_skin(id, skin=-1);
```

#### Usage
id | ```The player id to change.```
---|---
skin | ```The skin number to change to.```
#### Description
```
Sets a player skin.  Omit the second parameter to return to default
```

#### Note
```
The skin does not revert on death, teamswitch, gestation, etc.
```

#### Return
```
This function has no return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).