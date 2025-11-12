# cs_get_user_driving
#### Syntax
```
native cs_get_user_driving(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if the client is currently driving a vehicle and if so, indicates
the speed.
```

#### Return
```
0 if the client is not driving, 1 if driving a vehicle but
not moving, 2 to 4 if driving positive speeds, 5 if
driving at a negative speed (backing), see TRAIN_* constants
in hlsdk_const.inc
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).