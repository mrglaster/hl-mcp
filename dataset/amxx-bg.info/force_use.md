# force_use
#### Syntax
```
native force_use(entUsed, entUser);
```

#### Usage
entUsed | ```Index of entity being used```
---|---
entUser | ```Index of entity using```
#### Description
```
Forces an entity (such as a player) to use another entity (such as a button).
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index is provided or, if either index
is a client index, that client is not connected, an error
will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

