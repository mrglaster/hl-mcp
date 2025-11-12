# rg_drop_item
#### Syntax
```
native rg_drop_item(const index, const item_name[]);
```

#### Usage
index | ```Client index```
---|---
item_name | ```Item classname, if no name, the active item classname```
#### Description
```
Forces the player to drop the specified item classname.
```

#### Return
```
Entity index of weaponbox, AMX_NULLENT (-1) otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.