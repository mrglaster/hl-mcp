# ns_get_spawn
#### Syntax
```
native ns_get_spawn(team,number=0,Float:ret[3]);
```

#### Description
```
Gets spawn point for specified team (type).
If:
Team is equal to 0:
Ready room spawns are returned.
Team is greater than 0:
Spawns for the team are returned.

Number is equal to 0:
Total number of spawns is returned.
Number is greater than 0:
The location of the specified spawn is returned.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).