# agroups_get_user_group
#### Syntax
```
native agroups_get_user_group(id, group[] = "", len = 0)
```

#### Usage
id | ```Player's index.```
---|---
group | ```Buffer to store the group name in.```
len | ```Buffer length.```
#### Description
```
Get's the user group.
```

#### Return
```
-2 if the player is not connected, -1 if the player is not in a group, group's index otherwise.
```


This code is a part of agroups.inc. To use this code you should include agroups.inc as ```#include <agroups>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 