# cm_set_user_prefix_status
#### Syntax
```
native cm_set_user_prefix_status(id, bool:status, bool:update = true)
```

#### Usage
id | ```Player's index.```
---|---
status | ```True to enable or false to disable.```
update | ```Whether to automatically update the player's data.```
#### Description
```
Enables/Disables the client's prefix.
```

#### Note
```
It is recommended to leave the "update" parameter to "true" because starting from version 4.1
custom data can be set to players who don't have a prefix or their prefix is disabled.
```

#### Return
```
This function has no return value.
```


This code is a part of chatmanager.inc. To use this code you should include chatmanager.inc as ```#include <chatmanager>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.