# GetSequenceInfo
#### Syntax
```
native bool:GetSequenceInfo(const entity, &piFlags, &Float:pflFrameRate, &Float:pflGroundSpeed);
```

#### Usage
entity | ```Entity index```
---|---
piFlags | ```Sequence flags (1 = sequence loops)```
pflFrameRate | ```Sequence framerate```
pflGroundSpeed | ```Sequence ground speed```
#### Description
```
Gets sequence information based on entity's model current sequence index
```

#### Return
```
True on success, false otherwise
```

#### Error
```
If the index is not within the range of 1 to maxEntities or
the entity is not valid, an error will be thrown.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.