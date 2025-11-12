# ns_set_speedchange
#### Syntax
```
native ns_set_speedchange(id, speedchange=0);
```

#### Usage
id | ```The player id to change.```
---|---
speedchange | ```The speed to modify the player speed by.  Set to 0 to revert to default speed.```
#### Description
```
Set this to modify the player's speed by a certain amount.
```

#### Note
```
The speed does not revert on death, teamswitch, gestation, etc.
```

#### Return
```
This function has no return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).