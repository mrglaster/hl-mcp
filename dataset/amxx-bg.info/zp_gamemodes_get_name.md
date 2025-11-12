# zp_gamemodes_get_name
#### Syntax
```
native zp_gamemodes_get_name(game_mode_id, name[], len)
```

#### Usage
game_mode_id | ```A valid game mode ID.```
---|---
name | ```The buffer to store the string in.```
len | ```Character size of the output buffer.```
#### Description
```
Returns a game mode's name.
```

#### Return
```
True on success, false otherwise.
```


This code is a part of zp50_gamemodes.inc. To use this code you should include zp50_gamemodes.inc as ```#include <zp50_gamemodes>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.