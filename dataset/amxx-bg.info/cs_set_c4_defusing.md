# cs_set_c4_defusing
#### Syntax
```
native cs_set_c4_defusing(c4index, bool:defusing);
```

#### Usage
c4index | ```C4 entity```
---|---
defusing | ```True if the bomb should be defused, false otherwise```
#### Description
```
Sets if the bomb is being defused.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the provided entity index is not a bomb, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).