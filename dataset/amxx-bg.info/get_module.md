# get_module
#### Syntax
```
native get_module(id, name[], nameLen, author[], authorLen, version[], versionLen, &status);
```

#### Usage
id | ```Module id```
---|---
name | ```Buffer to copy module name to```
nameLen | ```Maximum name buffer size```
author | ```Buffer to copy module author to```
authorLen | ```Maximum author buffer size```
version | ```Buffer to copy module version to```
versionLen | ```Maximum version buffer size```
status | ```Variable to store module status to```
#### Description
```
Retrieves info about a module by module index.
```

#### Note
```
For a list of possible status flags, see module_* constants in
amxconst.inc
```

#### Return
```
Module id on success, -1 on invalid module
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

