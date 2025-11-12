# ze_is_zombie_frozen
#### Syntax
```
native ze_is_zombie_frozen(id);
```

#### Usage
id | ```Client index.```
---|---
#### Description
```
Description: Check if this zombie in pre-release time or not.
             Pre-Release time is said to be freeze time for zombies.
```

#### Return
```
true  | If this zombie in freeze time.
false | If this zombie not in freeze time.
-1    | If player not connected or this player is Human.
```

#### Note
```
This native is working in Escape Mode.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed