# cs_set_no_knives
#### Syntax
```
native cs_set_no_knives(noknives = 0);
```

#### Usage
noknives | ```If nonzero enable "no knives" mode, disable otherwise```
---|---
#### Description
```
Enables or disables the "no knives" mode.
```

#### Note
```
"No knives" mode means that the CStrike module will prevent the game
from creating (and thus attaching) "weapon_knife" entities. This means
that clients will spawn without knives, but knives can still be put
into the client inventories directly.
```

#### Return
```
This function has no return value.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).