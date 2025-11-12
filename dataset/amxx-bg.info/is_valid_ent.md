# is_valid_ent
#### Syntax
```
native is_valid_ent(iIndex);
```

#### Usage
iIndex | ```Entity index```
---|---
#### Description
```
Returns if an entity index is valid (as required by other engine natives).
```

#### Note
```
Engine considers an entity index valid if it is in the range between 1
and the maximum number of entities possible. The index also has to
point to an existing entity or, if it is a client index, the client has
to be connected.
```

#### Return
```
1 if entity is valid, 0 otherwise
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

