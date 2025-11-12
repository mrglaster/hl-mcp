# ze_set_fire_grenade
#### Syntax
```
native ze_set_fire_grenade(id, bSet);
```

#### Usage
id | ```Client index.```
---|---
bSet | ```Boolean value, true will set fire on zombie. false will stop fire on zombie.```
#### Description
```
Description: Used to set/stop fire on zombie.
```

#### Return
```
true    | If successfully set/stop fire on zombie.
false   | If returned 1 in ze_fire_pre() forward.
        Mean if fire action stopped by the pre forward.
NULLENT | If this zombie not alive.
```

#### Note
```
If zombie fired right now, you can use this to stop the fire
imediatly by using: ze_set_fire_grenade(id, false)
Same you can fire him at anytime.
Always check if user alive or not when using this native.
This will throw error in case of invalid player.
You can also set fire on alive humans.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed