# zp_user_infect_attempt
#### Syntax
```
forward zp_user_infect_attempt(id, infector, nemesis)
```

#### Description
```
Called on a player infect/cure attempt. You can use this to block
an infection/humanization by returning ZP_PLUGIN_HANDLED in your plugin.

Note: Right now this is only available after the ZP round starts, since some
situations (like blocking a first zombie's infection) are not yet handled.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed