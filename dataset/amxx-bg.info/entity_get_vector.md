# entity_get_vector
#### Syntax
```
native entity_get_vector(iIndex, iKey, Float:vRetVector[3]);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
vRetVector | ```Array to store vector in```
#### Description
```
Retrieves a vector type value from an entities entvar struct.
```

#### Note
```
For a list of valid vector type entries, see the EV_VEC_* constants in
engine_const.inc
```

#### Return
```
1 if value was sucessfully retrieved, 0 if an invalid
entry was specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

