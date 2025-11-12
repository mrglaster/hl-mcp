# cs_set_user_armor
#### Syntax
```
native cs_set_user_armor(index, armorvalue, CsArmorType:armortype);
```

#### Usage
index | ```Client index```
---|---
armorvalue | ```Amount of armor to set```
armortype | ```CS armor type```
#### Description
```
Sets the client's armor value the type of armor.
```

#### Note
```
For a list of possible armor types see the CsArmorType enum.
```

#### Note
```
Sends the appropriate message to update the client's HUD.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).