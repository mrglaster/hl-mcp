# GetBonePosition
#### Syntax
```
native GetBonePosition(const entity, const bone, Float:vecOrigin[3], Float:vecAngles[3] = {0.0, 0.0, 0.0});
```

#### Usage
entity | ```Entity index```
---|---
bone | ```Number of the bone```
vecOrigin | ```Array to store origin in```
vecAngles | ```Array to store angles in```
#### Description
```
Gets the position of the bone
```

#### Return
```
1 on success, 0 otherwise
```

#### Error
```
If the index is not within the range of 1 to maxEntities or
the entity is not valid, an error will be thrown.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.