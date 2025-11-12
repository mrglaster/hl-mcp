# zp_round_started_pre
#### Syntax
```
forward zp_round_started_pre(gameid)
```

#### Usage
gameid | ```Custom mode id which is called```
---|---
#### Description
```
Called before the ZP round starts. This is only
called for custom game modes.

Note: The custom game mode id can be used to start
the game mode externally

Note: returning ZP_PLUGIN_HANDLED will cause the
game mode to be blocked and other game modes will
be given a chance.
```


This code is a part of zombie_plague_advance.inc. To use this code you should include zombie_plague_advance.inc as ```#include <zombie_plague_advance>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.