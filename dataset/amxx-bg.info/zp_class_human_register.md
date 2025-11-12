# zp_class_human_register
#### Syntax
```
native zp_class_human_register(const name[], const description[], health, Float:speed, Float:gravity)
```

#### Usage
name | ```Caption to display on the menu.```
---|---
description | ```Brief description of the class.```
health | ```Class health.```
speed | ```Class maxspeed (can be a multiplier).```
gravity | ```Class gravity multiplier.```
#### Description
```
Registers a custom class which will be added to the human classes menu of ZP.

Note: The returned human class ID can be later used to identify
the class when calling the zp_get_user_human_class() natives.
```

#### Return
```
An internal human class ID, or ZP_INVALID_HUMAN_CLASS on failure.
```


This code is a part of zp50_class_human.inc. To use this code you should include zp50_class_human.inc as ```#include <zp50_class_human>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.