# get_keyvalue
#### Syntax
```
native get_keyvalue(entity, const szKey[], value[], maxLength);
```

#### Usage
entity | ```Entity index```
---|---
szKey | ```Key to retrieve value of```
value | ```Buffer to copy value to```
maxLength | ```Maximum size of buffer```
#### Description
```
Retrieves a value from an entities keyvalues.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If an invalid entity index is provided or, if the index
is a client index, the client is not connected, an error
will be thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

