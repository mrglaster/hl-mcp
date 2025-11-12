# cs_get_c4_defusing
#### Syntax
```
native bool:cs_get_c4_defusing(c4index);
```

#### Usage
c4index | ```C4 entity```
---|---
#### Description
```
Returns if the bomb is being defused.
```

#### Return
```
1 if the bomb is being defused, 0 otherwise
```

#### Error
```
If the provided entity index is not a bomb, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).