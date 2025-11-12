# get_user_ammo
#### Syntax
```
native get_user_ammo(index, weapon, &clip, &ammo);
```

#### Usage
index | ```Client index```
---|---
weapon | ```Weapon index```
clip | ```Variable to store clip ammo to```
ammo | ```Variable to store backpack ammo to```
#### Description
```
Retrieves ammo in the clip and backpack of the specified weapon.
```

#### Return
```
1 on success or 0 if the client is not connected
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients or the weapon index is invalid, an error will
be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

