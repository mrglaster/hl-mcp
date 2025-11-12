# drop_to_floor
#### Syntax
```
native drop_to_floor(entity);
```

#### Usage
entity | ```Entity index```
---|---
#### Description
```
Uses the DROP_TO_FLOOR() engine function on an entity, which attempts to put
it down on the floor.
```

#### Note
```
This engine function traces 256 units straight downwards from the
entity origin. If the trace hits the floor, the origin is updated to
the end position of the trace, FL_ONGROUND is added to the flags and
EV_ENT_groundentity is updated. When the trace does not hit anything or
the entity would be stuck inside something, the function does nothing
and returns 0.
```

#### Return
```
1 if entity is on the floor, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

