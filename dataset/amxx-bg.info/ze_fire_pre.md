# ze_fire_pre
#### Syntax
```
forward ze_fire_pre(id);
```

#### Description
```
Description:  Called before zombie (or human) get fired by fire nade.
```

#### Return
```
ZE_STOP         | Block the fire action, zombie will not get fired.
ZE_CONTINUE     | Continue the fire, zombie will be fired.
```

#### Note
```
You can use this to stop the fire action at specific conditions.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed