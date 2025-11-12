# ze_reset_human_speed
#### Syntax
```
native ze_reset_human_speed(id);
```

#### Usage
id | ```Client index.```
---|---
#### Description
```
Description: Reset human speed to default value used in ze_human_speed_factor cvar.
```

#### Return
```
true  | If reset successfully
false | If this player not connected
```

#### Error
```
If player not connected.
```

#### Note
```
This will remove the custom speed factor set by
ze_set_human_speed_factor(id, iFactor) native.
And will use the default factor in ze_human_speed_factor cvar.
This will throw error in case of invalid player.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed