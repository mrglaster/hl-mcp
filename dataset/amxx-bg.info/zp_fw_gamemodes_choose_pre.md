# zp_fw_gamemodes_choose_pre
#### Syntax
```
forward zp_fw_gamemodes_choose_pre(game_mode_id, skipchecks)
```

#### Usage
game_mode_id | ```Internal game mode ID.```
---|---
skipchecks | ```True when mode is being started by an admin.```
#### Description
```
Called when ZP tries to choose a game mode for the current
round. Returning PLUGIN_HANDLED here will tell the game modes
manager that your mode can't be chosen (useful to set custom
conditions, like a min amount of players, etc.)
```


This code is a part of zp50_gamemodes.inc. To use this code you should include zp50_gamemodes.inc as ```#include <zp50_gamemodes>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.