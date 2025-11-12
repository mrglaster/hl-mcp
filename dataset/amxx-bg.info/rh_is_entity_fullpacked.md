# rh_is_entity_fullpacked
#### Syntax
```
native bool:rh_is_entity_fullpacked(const host, const entity, const frame = -1);
```

#### Usage
host | ```Host index for whom we are checking the entity. (Host cannot be a fake client)```
---|---
entity | ```Entity index to find in the table of entities for the given frame.```
frame | ```Frame index where to look. Default is -1, which checks the previous frame.```
#### Description
```
Checks if a specific entity is present in the host's outgoing entity table for a given frame,
indicating it has passed the visibility check (AddToFullPack) and is ready for client transmission.
```

#### Note
```
To check in the current frame, this native should be called at the end of the server frame.
```

#### Return
```
Returns true if the entity is present in the host's outgoing entity table and
ready to be sent to all clients in the given frame, otherwise false.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.