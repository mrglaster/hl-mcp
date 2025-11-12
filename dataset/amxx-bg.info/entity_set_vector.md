# entity_set_vector
#### Syntax
```
native entity_set_vector(iIndex, iKey, const Float:vNewVector[3]);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to write to```
vNewVector | ```Array to copy to the entity```
#### Description
```
Sets a vector type value in an entities entvar struct.
```

#### Note
```
For a list of valid vector type entries, see the EV_VEC_* constants in
engine_const.inc
```

#### Return
```
1 if value was sucessfully set, 0 if an invalid entry
was specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

