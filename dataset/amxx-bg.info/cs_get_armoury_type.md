# cs_get_armoury_type
#### Syntax
```
native cs_get_armoury_type(index, &count = 1);
```

#### Usage
index | ```Armoury entity index```
---|---
count | ```Optional variable to store in the number of times that an item can be retrieved from the same entity before being hidden```
#### Description
```
Returns the armoury entity's weapon id.
```

#### Note
```
Not all weapon ids are supported by Counter-Strike, an armoury entity
can not be a pistol, a knife or a bomb for exmaple. The full list is:
   CSW_SCOUT, CSW_HEGRENADE, CSW_XM1014, CSW_MAC10, CSW_AUG,
   CSW_SMOKEGRENADE, CSW_AWP, CSW_MP5NAVY, CSW_M249, CSW_M3, CSW_M4A1,
   CSW_TMP, CSW_G3SG1, CSW_VEST, CSW_VESTHELM, CSW_FLASHBANG,
   CSW_SG552, CSW_AK47, CSW_P90
```

#### Return
```
Weapon id
```

#### Error
```
If a non-armoury entity is provided, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).