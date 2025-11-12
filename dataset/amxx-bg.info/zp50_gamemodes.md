# Functions in zp50_gamemodes.inc
Function | Description  
---|---  
[zp_gamemodes_register](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_register) | ```
Registers a new game mode.
```
  
[zp_gamemodes_set_default](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_set_default) | ```
Sets a default game mode (to start if no other game mode can been started).
```
  
[zp_gamemodes_get_default](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_default) | ```
Returns default game mode.
```
  
[zp_gamemodes_get_chosen](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_chosen) | ```
Returns game mode that was chosen for the current round.
```
  
[zp_gamemodes_get_current](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_current) | ```
Returns game mode that is currently in progress.
```
  
[zp_gamemodes_get_id](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_id) | ```
Returns a game mode's ID.
```
  
[zp_gamemodes_get_name](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_name) | ```
Returns a game mode's name.
```
  
[zp_gamemodes_start](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_start) | ```
Forces a game mode to start.
```
  
[zp_gamemodes_get_count](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_count) | ```
Returns number of registered game modes.
```
  
[zp_gamemodes_set_allow_infect](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_set_allow_infect) | ```
Sets whether zombies can infect humans for the current game mode.
```
  
[zp_gamemodes_get_allow_infect](https://amxx-bg.info/api/zp50_gamemodes/zp_gamemodes_get_allow_infect) | ```
Returns whether zombies are allowed to infect humans for the current game mode.
```
  
[zp_fw_gamemodes_choose_pre](https://amxx-bg.info/api/zp50_gamemodes/zp_fw_gamemodes_choose_pre) | ```
Called when ZP tries to choose a game mode for the current
round. Returning PLUGIN_HANDLED here will tell the game modes
manager that your mode can't be chosen (useful to set custom
conditions, like a min amount of players, etc.)
```
  
[zp_fw_gamemodes_choose_post](https://amxx-bg.info/api/zp50_gamemodes/zp_fw_gamemodes_choose_post) | ```
Called when a game mode is chosen for the current round.
```
  
[zp_fw_gamemodes_start](https://amxx-bg.info/api/zp50_gamemodes/zp_fw_gamemodes_start) | ```
Called when a game mode starts.
```
  
[zp_fw_gamemodes_end](https://amxx-bg.info/api/zp50_gamemodes/zp_fw_gamemodes_end) | ```
Called when a game mode ends.

Note: this can pass ZP_NO_GAME_MODE (if no game mode was in progress).
```
  

This code is a part of zp50_gamemodes.inc. To use this code you should include zp50_gamemodes.inc as ```#include <zp50_gamemodes>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.