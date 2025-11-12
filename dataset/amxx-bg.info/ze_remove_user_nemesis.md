# ze_remove_user_nemesis
#### Syntax
```
native ze_remove_user_nemesis(id, bool:bZombie = true);
```

#### Usage
id | ```Client index.```
---|---
bZombie | ```Set player Zombie attributes after remove.```
#### Description
```
Description: Remove player Nemesis attributes
```

#### Return
```
true    | If remove successfully.
false   | If player not connected.
```

#### Note
```
Nemesis health never reset, When remove Nemesis attributes.
```

#### Error
```
If player not connected.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed