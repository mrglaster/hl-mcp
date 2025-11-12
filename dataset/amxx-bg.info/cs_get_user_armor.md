# cs_get_user_armor
#### Syntax
```
native cs_get_user_armor(index, &CsArmorType:armortype = CS_ARMOR_NONE);
```

#### Usage
index | ```Client index```
---|---
armortype | ```Variable to store armor type in```
#### Description
```
Returns the client's armor value and retrieves the type of armor.
```

#### Note
```
For a list of possible armor types see the CsArmorType enum.
```

#### Return
```
Amount of armor, 0 if client has no armor
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).