# entity_set_string
#### Syntax
```
native entity_set_string(iIndex, iKey, const szNewVal[]);
```

#### Usage
iIndex | ```Entity index```
---|---
iKey | ```Entry to retrieve from```
szNewVal | ```String to copy to the entity```
#### Description
```
Sets a string type value in an entities entvar struct.
```

#### Note
```
For a list of valid string type entries, see the EV_SZ_* constants in
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


  
  

