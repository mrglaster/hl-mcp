# cs_get_no_knives
#### Syntax
```
native cs_get_no_knives();
```

#### Description
```
Returns if "no knives" mode is enabled.
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
1 if "no knives" mode is enabled, 0 otherwise
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).