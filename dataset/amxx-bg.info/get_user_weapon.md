# get_user_weapon
#### Syntax
```
native get_user_weapon(index, &clip = 0, &ammo = 0);
```

#### Usage
index | ```Client index```
---|---
clip | ```Optional variable to store clip ammo to```
ammo | ```Optional variable to store backpack ammo to```
#### Description
```
Returns weapon index of the currently carried weapon. Also allows retrieval
of ammo in the clip and backpack.
```

#### Return
```
Weapon index on success or 0 if the client is not connected
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

