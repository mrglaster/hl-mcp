# entity_set_size
#### Syntax
```
native entity_set_size(index, const Float:mins[3], const Float:maxs[3]);
```

#### Usage
index | ```Entity index```
---|---
mins | ```Vector containing the minimum point relative to the origin```
maxs | ```Vector containing the maximum point relative to the origin```
#### Description
```
Sets the size of the entity bounding box, as described by the minimum and
maximum vectors relative to the origin.
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


  
  

