# cs_set_user_plant
#### Syntax
```
native cs_set_user_plant(index, plant = 1, showbombicon = 1);
```

#### Usage
index | ```Client index```
---|---
plant | ```If nonzero the client will be able to plant the bomb, otherwise he will be unable to```
showbombicon | ```If nonzero the green C4 icon will be displayed on the client's hud, otherwise it will be hidden```
#### Description
```
Sets the client's ability to plant the bomb and displays or hides the bomb
HUD icon.
```

#### Note
```
Only with this set can the client plant the bomb within the usual bomb
target areas. If this is not set the user can not plant the bomb, even
when he has one in the inventory. This is only correctly set when the
client touches a bomb and picks it up "manually" (only possible for
Terrorists), so this should be used if the bomb is added to the
inventory through other means.
```

#### Return
```
1 if the client is able to plant the bomb, 0 otherwise
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).