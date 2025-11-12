# zp_fw_core_infect_pre
#### Syntax
```
forward zp_fw_core_infect_pre(id, attacker)
```

#### Usage
id | ```Player index who is being infected/cured.```
---|---
attacker | ```Player who is triggering the infection/cure. (0 if not available, id = attacker if he is infecting/curing himself)```
#### Description
```
Called on a player infect/cure attempt. You can block it by
returning PLUGIN_HANDLED in your plugin.
```


This code is a part of zp50_core.inc. To use this code you should include zp50_core.inc as ```#include <zp50_core>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.