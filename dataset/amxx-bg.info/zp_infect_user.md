# zp_infect_user
#### Syntax
```
native zp_infect_user(id, infector = 0, silent = 0, rewards = 0)
```

#### Usage
id | ```Player index to be infected.```
---|---
infector | ```Player index who infected him (optional).```
silent | ```If set, there will be no HUD messages or infection sounds.```
rewards | ```Whether to show DeathMsg and reward frags, hp, and ammo packs to infector.```
#### Description
```
Forces a player to become a zombie.

Note: Unavailable for last human/survivor.
```

#### Return
```
True on success, false otherwise.
```


This code is a part of zombieplague.inc. To use this code you should include zombieplague.inc as ```#include <zombieplague>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is the old version of Zombie Plague mod for Counter Strike 1.6. It won't work with other games (Half-Life, DoD, etc) or without the mod installed