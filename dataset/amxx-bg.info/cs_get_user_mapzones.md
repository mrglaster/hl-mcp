# cs_get_user_mapzones
#### Syntax
```
native cs_get_user_mapzones(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the map zones the client is inside of as a bitflag value.
```

#### Note
```
If the user does not have the ability to plant (cs_get_user_plant()
returns 0) then the bitflag will not contain CS_MAPZONE_BOMBTARGET.
```

#### Nore
```
For a list of possible zone flags see the CS_MAPZONE_* constants.
```

#### Return
```
Bitflag value of map zones
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).