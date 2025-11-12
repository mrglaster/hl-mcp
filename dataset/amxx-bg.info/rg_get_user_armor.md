# rg_get_user_armor
#### Syntax
```
native rg_get_user_armor(const index, &ArmorType:armortype = ARMOR_NONE);
```

#### Usage
index | ```Client index```
---|---
armortype | ```Variable to store armor type in```
#### Description
```
Returns the client's armor value and retrieves the type of armor.
```

#### Return
```
Amount of armor, 0 if the client has no armor
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.