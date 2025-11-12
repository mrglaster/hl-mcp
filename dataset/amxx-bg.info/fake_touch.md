# fake_touch
#### Syntax
```
native fake_touch(entTouched, entToucher);
```

#### Usage
entTouched | ```Index of entity being touched```
---|---
entToucher | ```Index of entity touching```
#### Description
```
Forces an entity to touch another entity.
```

#### Note
```
This calls the game touch function even when the entities do not
intersect. It doesn't change their origins and/or bounding boxes.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid entity index is provided or, if the index
is a client index, the client is not connected, an error
will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

