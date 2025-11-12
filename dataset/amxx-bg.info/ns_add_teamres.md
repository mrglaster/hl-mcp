# ns_add_teamres
#### Syntax
```
native Float:ns_add_teamres(Team,Float:value);
```

#### Usage
Team | ```1 for teama, 2 for teamb. (eg: in MvA maps, 1 is marines, 2 is aliens.  In mvm, 1 is marine1, 2 is marine2)```
---|---
value | ```The amount to set the resources to add to the pool```
#### Description
```
Adds to the team's resources in the resource pool.
```

#### Note
```
If this is used on an alien team, the resources will be
distributed between all of the players who need resources.
```

#### Return
```
The new amount of resources in the resource pool.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).