# call_think
#### Syntax
```
native call_think(entity);
```

#### Usage
entity | ```Entity index```
---|---
#### Description
```
Calls the DispatchThink() game DLL function on an entity, triggering it to
think if applicable.
```

#### Note
```
DispatchThink() checks the entity for the FL_DORMANT flag - if it is
set, the entity will not proceed to think. It will first call the
class-specific think function and eventually CBaseEntity::Think(), thus
triggering other think hooks and forwards.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

