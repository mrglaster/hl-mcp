# zp_override_user_model
#### Syntax
```
native zp_override_user_model(id, const newmodel[], modelindex = 0)
```

#### Usage
id | ```Player index.```
---|---
newmodel | ```Model name.```
modelindex | ```Modelindex (optional).```
#### Description
```
Overrides ZP player model with a different custom model.

Note: This will last until player's next infection/humanization/respawn.

Note: Don't call more often than absolutely needed.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed