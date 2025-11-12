# attach_view
#### Syntax
```
native attach_view(iIndex, iTargetIndex);
```

#### Usage
iIndex | ```Client index```
---|---
iTargetIndex | ```Index of entity to attach to```
#### Description
```
Attaches a clients viewport to an entity.
```

#### Note
```
To reset the clients viewport, call this function with the client index
as the target entity.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

