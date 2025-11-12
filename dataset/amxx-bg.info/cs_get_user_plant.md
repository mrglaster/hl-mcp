# cs_get_user_plant
#### Syntax
```
native cs_get_user_plant(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if the client has the ability to plant the bomb.
```

#### Note
```
Only with this set can the client plant the bomb within the usual bomb
target areas. If this is not set the user can not plant the bomb, even
when he has one in the inventory.
```

#### Return
```
1 if the client is able to plant the bomb, 0 otherwise
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).