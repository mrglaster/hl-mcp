# entity_set_origin
#### Syntax
```
native entity_set_origin(iIndex, const Float:fNewOrigin[3]);
```

#### Usage
iIndex | ```Entity index```
---|---
fNewOrigin | ```New origin```
#### Description
```
Sets the origin of an entity.
```

#### Note
```
This native uses engine functions to set the origin, keeping it
properly updated with the game. Directly writing to EV_VEC_origin is an
error and will cause problems.
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


  
  

