# zp_get_zombie_class_info
#### Syntax
```
native zp_get_zombie_class_info(classid, info[], len)
```

#### Usage
classid | ```Internal zombie class ID.```
---|---
info | ```The buffer to store the string in.```
len | ```Character size of the output buffer.```
#### Description
```
Returns a zombie class' description (passed by reference).
```

#### Return
```
True on success, false otherwise.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed