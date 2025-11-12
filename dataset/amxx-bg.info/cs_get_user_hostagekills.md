# cs_get_user_hostagekills
#### Syntax
```
native cs_get_user_hostagekills(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the amount of hostages that the client has killed.
```

#### Note
```
This is the value that the internal Counter-Strike hostage punisher
uses to determine if a client should be kicked, depending on the
value of the mp_hostagepenalty value.
```

#### Return
```
Amount of hostages killed
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).