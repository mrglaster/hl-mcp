# zp_class_human_get_max_health
#### Syntax
```
native zp_class_human_get_max_health(id, classid)
```

#### Usage
id | ```Player index.```
---|---
classid | ```A valid human class ID.```
#### Description
```
Returns the default maximum health for a specific human class.

Note: does not take into account any kind of HP bonuses.
```

#### Return
```
Maximum amount of health points, -1 on error.
```


This code is a part of zp50_class_human.inc. To use this code you should include zp50_class_human.inc as ```#include <zp50_class_human>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.