# get_user_menu
#### Syntax
```
native get_user_menu(index, &id, &keys);
```

#### Usage
index | ```Client index```
---|---
id | ```Variable to store menu id to```
keys | ```Variable to store menu keys to```
#### Description
```
Returns if the client is watching a menu.
```

#### Note
```
If there is no menu, the id is 0. If the id is negative, then the client
views a VGUI menu. Otherwise, the id is an id acquired from the
register_menuid() function.
```

#### Return
```
1 if client views a menu, 0 otherwise
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

