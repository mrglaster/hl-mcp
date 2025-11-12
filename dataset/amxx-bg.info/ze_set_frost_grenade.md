# ze_set_frost_grenade
#### Syntax
```
native ze_set_frost_grenade(id, bSet);
```

#### Usage
id | ```Client index.```
---|---
bSet | ```Boolean value, true will freeze zombie. false will unfreeze zombie.```
#### Description
```
Description: Used to set/stop freeze on zombie.
```

#### Return
```
true    | If successfully freeze/unfreeze zombie.
false   | If returned 1 in ze_frost_pre() forward.
        Mean if freeze action stopped by the pre forward.
        Or if player already frozen
NULLENT | If this zombie not alive.
```

#### Note
```
If zombie frozen right now, you can use this to unfreeze him
imediatly by using: ze_set_frost_grenade(id, false)
Same you can freeze him at anytime.
Always check if user alive or not when using this native.
This will throw error in case of invalid player.
You can also freeze alive humans.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed