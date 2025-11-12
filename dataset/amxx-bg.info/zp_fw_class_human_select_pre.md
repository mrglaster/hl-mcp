# zp_fw_class_human_select_pre
#### Syntax
```
forward zp_fw_class_human_select_pre(id, classid)
```

#### Usage
id | ```Player index.```
---|---
classid | ```Internal human class ID.```
#### Description
```
Called when determining whether a class should be available to a player.

Possible return values are:
 - ZP_CLASS_AVAILABLE (show in menu, allow selection)
 - ZP_CLASS_NOT_AVAILABLE (show in menu, don't allow selection)
 - ZP_CLASS_DONT_SHOW (don't show in menu, don't allow selection)
```


This code is a part of zp50_class_human.inc. To use this code you should include zp50_class_human.inc as ```#include <zp50_class_human>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.