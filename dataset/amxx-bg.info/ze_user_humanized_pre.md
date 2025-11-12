# ze_user_humanized_pre
#### Syntax
```
forward ze_user_humanized_pre(id);
```

#### Usage
id | ```Client index.```
---|---
#### Description
```
Description: Called when user humanized, it called whenever
             ze_set_user_human(id) native used.
             It's called also at every new round when all players humanized.
```

#### Return
```
ZE_STOP     | Prevent humanization event.
ZE_CONTINUE | Continue humanization event.
```

#### Note
```
ze_user_humanized never called,
When this forward return value 1 or above.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed