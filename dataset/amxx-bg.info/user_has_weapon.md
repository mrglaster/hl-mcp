# user_has_weapon
#### Syntax
```
native user_has_weapon(index, weapon, setweapon = -1);
```

#### Usage
index | ```Client index```
---|---
weapon | ```Weapon index```
setweapon | ```If zero the weapon bit will be removed from the client's inventory, if 1 it will be set```
#### Description
```
Returns if the client has the specified weapon in their inventory.
```

#### Return
```
1 if the weapon is present, 0 if it is not
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

