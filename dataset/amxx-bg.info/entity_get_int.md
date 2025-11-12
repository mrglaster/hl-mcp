# entity_get_int
#### Syntax
```
native entity_get_int(iIndex, iKey);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
#### Description
```
Returns an integer type value from an entities entvar struct.
```

#### Note
```
For a list of valid integer type entries, see the EV_INT_* constants in
engine_const.inc
```

#### Return
```
Value of specified entry
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

