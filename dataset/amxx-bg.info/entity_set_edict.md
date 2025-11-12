# entity_set_edict
#### Syntax
```
native entity_set_edict(iIndex, iKey, iNewIndex);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to write to```
iNewIndex | ```Entity index to set```
#### Description
```
Sets an edict type value in an entities entvar struct.
```

#### Note
```
For a list of valid edict type entries, see the EV_ENT_* constants in
engine_const.inc
```

#### Note
```
This native will crash the server if an invalid entity index is
provided in iNewIndex.
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


  
  

