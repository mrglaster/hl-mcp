# rh_get_mapname
#### Syntax
```
native rh_get_mapname(output[], len, MapNameType:type = MNT_SET);
```

#### Usage
output | ```Buffer to copy map name to```
---|---
len | ```Maximum buffer size```
type | ```MNT_SET will return the name of the current map MNT_TRUE will return the original map name independant of the name set with via rh_set_mapname```
#### Description
```
Gets the name of the map.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_engine.inc. To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.