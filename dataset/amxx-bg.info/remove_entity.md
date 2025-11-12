# remove_entity
#### Syntax
```
native remove_entity(iIndex);
```

#### Usage
iIndex | ```Entity index```
---|---
#### Description
```
Removes an entity from the world.
```

#### Return
```
1 if entity was sucessfully removed, 0 if an invalid entity
was provided
```

#### Error
```
If an entity index in the range of 0 to MaxClients is
provided, an error will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

