# find_ent_by_owner
#### Syntax
```
native find_ent_by_owner(iIndex, const szClass[], iOwner, iJghgType = 0);
```

#### Usage
iIndex | ```Entity index to start from```
---|---
szClass | ```String to match```
iOwner | ```Owner entity index to match```
iJghgType | ```Entity field to match string against:     0 - Classname     1 - Target     2 - Targetname```
#### Description
```
Searches entities in the world, starting at a specified index, matching by
owner and a configurable entity field.
```

#### Return
```
Entity index if an entity was found, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

