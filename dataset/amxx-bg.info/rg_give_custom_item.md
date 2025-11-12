# rg_give_custom_item
#### Syntax
```
native rg_give_custom_item(const index, const pszName[], GiveType:type = GT_APPEND, const uid = 0);
```

#### Usage
index | ```Client index```
---|---
pszName | ```Item classname```
type | ```Look at the enums with name GiveType```
uid | ```Sets a unique index for the entity```
#### Description
```
Gives the player an custom item, this means that don't handled API things.
```

#### Example
```
rg_give_custom_item(id, "weapon_c4"); doesn't sets the member m_bHasC4 to true, as the rg_give_item does.
```

#### Return
```
Index of entity if successfull, -1 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.