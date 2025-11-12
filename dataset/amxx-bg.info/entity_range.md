# entity_range
#### Syntax
```
native Float:entity_range(ida, idb);
```

#### Usage
ida | ```Entity index 1```
---|---
idb | ```Entity index 2```
#### Description
```
Returns the distance between two entities.
```

#### Return
```
Distance between the entities
```

#### Error
```
If an invalid entity index is provided or, if either index is a
client index, that client is not connected, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

