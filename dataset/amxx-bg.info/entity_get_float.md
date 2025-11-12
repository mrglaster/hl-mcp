# entity_get_float
#### Syntax
```
native Float:entity_get_float(iIndex, iKey);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
#### Description
```
Returns a float type value from an entities entvar struct.
```

#### Note
```
For a list of valid float type entries, see the EV_FL_* constants in
engine_const.inc
```

#### Return
```
Value of specified entry, or 0 if an invalid entry was
specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

