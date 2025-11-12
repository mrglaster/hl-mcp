# cs_set_user_nvg
#### Syntax
```
native cs_set_user_nvg(index, nvgoggles = 1);
```

#### Usage
index | ```Client index```
---|---
nvgoogles | ```If nonzero the NVG will be added to the client's inventory, otherwise they will be removed from it```
#### Description
```
Sets the client's night vision goggles.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).