# is_visible
#### Syntax
```
native is_visible(entity, target);
```

#### Usage
entity | ```Entity index```
---|---
target | ```Target entity index```
#### Description
```
Returns if an entity is visible to another entity. Derived from SDK.
```

#### Note
```
If the target entity has the FL_NOTARGET flag set, this native always
returns 0.
```

#### Note
```
This native fires a traceline between the view-offset origins of the
entities. If the traceline is unobstructed it returns true. This is not
a full 3D visibility check.
```

#### Return
```
1 if entity is visible, 0 otherwise
```

#### Error
```
If an invalid entity index is provided or, if the index is a
client index, the client is not connected, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

