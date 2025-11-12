# zp_register_game_mode
#### Syntax
```
native zp_register_game_mode( const name[], flags, chance, allow, dm_mode)
```

#### Usage
name | ```The game mode's name which will help in identifing it.```
---|---
flags | ```Access flags required by the admins to start this game mode.```
chance | ```Chance level of this game mode. (1 in X).```
allow | ```Whether to permit infection after zombie to player attacks.```
dm_mode | ```Death match mode which will be used during this game.```
#### Description
```
Registers a custom game mode which will be added to the admin menu of ZP

Note: The returned game mode ID can later be used to detect the game mode
which is called in zp_round_started_pre. There you can start the game mode
externally by using this game mode ID.
```

#### Return
```
An internal game mode ID or -1 on failure.
```


This code is a part of zombie_plague_advance.inc. To use this code you should include zombie_plague_advance.inc as ```#include <zombie_plague_advance>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.