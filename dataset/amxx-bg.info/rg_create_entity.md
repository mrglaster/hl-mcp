# rg_create_entity
#### Syntax
```
native rg_create_entity(const classname[], const bool:useHashTable = false);
```

#### Usage
classname | ```Entity classname```
---|---
useHashTable | ```Use this only for known game entities```
#### Description
```
Creates an entity using Counter-Strike's custom CreateNamedEntity wrapper.
```

#### Note
```
: Do not use this if you plan to change custom classname an entity after creation,
  otherwise it will never be release from hash table even if an entity was destroyed,
  and that to lead table to inflate/memory leaks
```

#### Return
```
Index of the created entity or 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.