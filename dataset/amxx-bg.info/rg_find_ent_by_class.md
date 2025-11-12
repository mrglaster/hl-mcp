# rg_find_ent_by_class
#### Syntax
```
native rg_find_ent_by_class(start_index, const classname[], const bool:useHashTable = false);
```

#### Usage
start_index | ```Entity index to start searching from. -1 to start from the first entity```
---|---
classname | ```Classname to search for```
useHashTable | ```Use this only for known game entities```
#### Description
```
Finds an entity in the world using Counter-Strike's custom FindEntityByString wrapper.
```

#### Note
```
: Do not use this if you use a custom classname
```

#### Return
```
Entity index > 0 if found, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.