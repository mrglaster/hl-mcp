# cs_set_user_zoom
#### Syntax
```
native cs_set_user_zoom(index, type, mode);
```

#### Usage
index | ```Client index```
---|---
type | ```Zoom type```
mode | ```If zero (blocking) the client will be forced to use the zoom type set and won't be able to change it until it is reset with CS_RESET_ZOOM, otherwise the user can restore back to normal as usual```
#### Description
```
Sets a zoom type on the client.
```

#### Note
```
Zoom types are not tied to their intended weapons, so any zoom type can
be combined with any weapon.
```

#### Note
```
For a list of possible zoom types see the zoom type enum above
(CS_*_ZOOM constants).
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, the client is not connected, or an invalid zoom
type is provided, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).