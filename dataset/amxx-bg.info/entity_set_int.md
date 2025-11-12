# entity_set_int
#### Syntax
```
native entity_set_int(iIndex, iKey, iVal);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to write to```
iVal | ```Value to set```
#### Description
```
Sets an integer type value in an entities entvar struct.
```

#### Note
```
For a list of valid integer type entries, see the EV_INT_* constants in
engine_const.inc
```

#### Return
```
1 if value was sucessfully set, 0 if an invalid entry was
specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

