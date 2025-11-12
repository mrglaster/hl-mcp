# ze_set_zombie_speed
#### Syntax
```
native ze_set_zombie_speed(id, iSpeed);
```

#### Usage
id | ```Client index.```
---|---
iSpeed | ```Speed to set this zombie to.```
#### Description
```
Description:     Set this zombie speed to custom value.
```

#### Return
```
true  | If set successfully
false | If this player not connected
```

#### Error
```
If player not connected.
```

#### Note
```
This native will set custom speed for this zombie
and will not use value defined in ze_zombie_speed cvar
This is limited by sv_maxspeed cvar.
This will throw error in case of invalid player.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed