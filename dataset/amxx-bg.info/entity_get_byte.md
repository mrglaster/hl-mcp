# entity_get_byte
#### Syntax
```
native entity_get_byte(iIndex, iKey);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
#### Description
```
Returns a bytearray type value from an entities entvar struct.
```

#### Note
```
For a list of valid bytearray type entries, see the EV_BYTE_* constants
in engine_const.inc
```

#### Return
```
Value of specified entry, 0 if an invalid entry was
specified
```

#### Error
```
If an invalid entity index is provided, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

