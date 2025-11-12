# ze_set_human_speed_factor
#### Syntax
```
native ze_set_human_speed_factor(id, iFactor);
```

#### Usage
id | ```Client index.```
---|---
iFactor | ```The factor to be added to current speed.```
#### Description
```
Description:     Increase human speed with this factor.
                 This factor added to his current speed depend on which weapon he carries.
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
This native will add speed to current speed.
For example, ze_set_human_speed_factor(id, 0) will not set player speed to zero
it won't increase his speed so he will have normal weapon speed.
Example, if player carry knife and ze_set_human_speed_factor(id, 20) his speed will be
increased by 20 so his total speed will be 270 (default knife speed: 250)
You may use negative factors to decrease this speed.
Using this native will set the players speed for the whole map.
Speeds reset if this player disconnect, or reset using reset native.
This is limited by sv_maxspeed cvar.
This will throw error in case of invalid player.
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed