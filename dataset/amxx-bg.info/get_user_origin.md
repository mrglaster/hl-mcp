# get_user_origin
#### Syntax
```
native get_user_origin(index, origin[3], mode = 0);
```

#### Usage
index | ```Client index```
---|---
origin | ```Array to store origin in```
mode | ```What type of origin to retrieve:   Origin_Client - current position   Origin_Eyes - position of eyes (and weapon)   Origin_AimEndClient - aim end position from client position   Origin_AimEndEyes - aim end position from eyes (hit point for weapon)   Origin_CS_LastBullet - position of last bullet hit (only for Counter-Strike)```
#### Description
```
Retrieves an origin related to the client.
```

#### Note
```
For a list of possible modes see the Origin_* constants in amxconst.inc.
```

#### Return
```
1 on success, 0 if client is not connected
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

