# rg_find_ent_by_owner
#### Syntax
```
native bool:rg_find_ent_by_owner(&start_index, const classname[], owner);
```

#### Usage
start_index | ```Entity index to start searching from. AMX_NULLENT (-1) to start from the first entity```
---|---
classname | ```Classname to search for```
#### Description
```
Finds an entity in the world using Counter-Strike's custom FindEntityByString wrapper, matching by owner.
```

#### Return
```
true if found, false otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.