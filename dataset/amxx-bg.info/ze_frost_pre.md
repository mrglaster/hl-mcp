# ze_frost_pre
#### Syntax
```
forward ze_frost_pre(id);
```

#### Description
```
Description: Called before zombie (or human) get frozen by frost nade.
```

#### Return
```
ZE_STOP     | Block the freeze action, zombie will not get frozen.
ZE_CONTINUE | Continue the freeze, zombie will be frozen.
```

#### Note
```
You can use this to stop the freeze action at specific conditions.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed