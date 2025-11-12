# bb_register_zombie_class
#### Syntax
```
native bb_register_zombie_class(const name[], const info[], const model[], const clawmodel[], hp, speed, Float:gravity, Float:knockback = 0.0, adminflags = ADMIN_ALL, credits = 0 )
```

#### Usage
name | ```Caption to display on the menu.```
---|---
info | ```Brief description of the class.```
model | ```Player model to be used.```
clawmodel | ```Claws model to be used.```
hp | ```Initial health points.```
speed | ```Maximum speed.```
gravity | ```Gravity multiplier.```
knockback | ```Empty value.```
adminflags | ```Set flag of admin only class, ADMIN_USER is normal players.```
credits | ```Cost of unlocking this class (if credits is enabled).```
#### Description
```
Registers a custom class which will be added to the zombie classes menu of BB.

Note: The returned zombie class ID can be later used to identify
the class when calling the bb_get_user_zombie_class() natives.
```

#### Return
```
An internal zombie class ID, or -1 on failure.
```


This code is a part of basebuilder.inc. To use this code you should include basebuilder.inc as ```#include <basebuilder>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and is provided with basebuilder mod.