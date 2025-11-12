# cs_set_c4_explode_time
#### Syntax
```
native cs_set_c4_explode_time(index, Float:value);
```

#### Usage
index | ```C4 entity```
---|---
value | ```New explosion time```
#### Description
```
Sets the game time at which the bomb will explode.
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