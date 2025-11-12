# rg_remove_item
#### Syntax
```
native rg_remove_item(const index, const item_name[], const bool:removeAmmo = false);
```

#### Usage
index | ```Client index```
---|---
item_name | ```Item classname```
removeAmmo | ```Remove ammunition```
#### Description
```
Removes the specified item classname from the player
```

#### Return
```
1 if found and remove, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.