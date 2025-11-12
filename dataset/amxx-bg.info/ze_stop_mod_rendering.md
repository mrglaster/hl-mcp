# ze_stop_mod_rendering
#### Syntax
```
native ze_stop_mod_rendering(id, bool:bSet);
```

#### Usage
id | ```Client index.```
---|---
bSet | ```True or false, True will stop the rendering that comes from ze_effects_messages.sma false will continue setting rendering from ze_effects_messages.sma```
#### Description
```
Description:     Stop/Resume setting rendering from ze_effects_messages.sma plugin.
```

#### Return
```
true  | If set successfully
false | If this player not connected
```

#### Erorr
```
If player not connected.
```

#### Note
```
This native will not throw error if player not connected. It will just return false.
You before you set rendering for any player in any plugin you should first make: ze_stop_mod_rendering(id, true)
This will ensure that no rendering is setting from ze_effects_messages.sma plugin.
When you remove rendering, you should use: ze_stop_mod_rendering(id, false)
```


This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed