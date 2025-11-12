# entity_set_byte
#### Syntax
```
native entity_set_byte(iIndex, iKey, iVal);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to write to```
iVal | ```Value to set```
#### Description
```
Sets a bytearray type value in an entities entvar struct.
```

#### Note
```
For a list of valid bytearray type entries, see the EV_BYTE_* constants
in engine_const.inc
```

#### Note
```
The value is automatically clamped to [0,255].
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


  
  

