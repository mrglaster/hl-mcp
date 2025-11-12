# entity_get_string
#### Syntax
```
native entity_get_string(iIndex, iKey, szReturn[], iRetLen);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
szReturn | ```Buffer to copy value to```
iRetLen | ```Maximum size of buffer```
#### Description
```
Retrieves a string type value from an entities entvar struct.
```

#### Note
```
For a list of valid string type entries, see the EV_SZ_* constants in
engine_const.inc
```

#### Return
```
Number of cells written to buffer,  0 if an invalid entry
was specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

