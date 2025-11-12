# Functions in zp50_core.inc
Function | Description  
---|---  
[zp_core_is_zombie](https://amxx-bg.info/api/zp50_core/zp_core_is_zombie) | ```
Returns whether a player is a zombie.
```
  
[zp_core_is_first_zombie](https://amxx-bg.info/api/zp50_core/zp_core_is_first_zombie) | ```
Returns whether a player is the first zombie.
```
  
[zp_core_is_last_zombie](https://amxx-bg.info/api/zp50_core/zp_core_is_last_zombie) | ```
Returns whether a player is the last zombie.
```
  
[zp_core_is_last_human](https://amxx-bg.info/api/zp50_core/zp_core_is_last_human) | ```
Returns whether a player is the last human.
```
  
[zp_core_get_zombie_count](https://amxx-bg.info/api/zp50_core/zp_core_get_zombie_count) | ```
Returns number of alive zombies.
```
  
[zp_core_get_human_count](https://amxx-bg.info/api/zp50_core/zp_core_get_human_count) | ```
Returns number of alive humans.
```
  
[zp_core_infect](https://amxx-bg.info/api/zp50_core/zp_core_infect) | ```
Turns a player into a zombie.
```
  
[zp_core_cure](https://amxx-bg.info/api/zp50_core/zp_core_cure) | ```
Turns a player into a human.
```
  
[zp_core_force_infect](https://amxx-bg.info/api/zp50_core/zp_core_force_infect) | ```
Forces a player to become a zombie/human.

Note: use this only when previous checks need to be skipped.
```
  
[zp_core_force_cure](https://amxx-bg.info/api/zp50_core/zp_core_force_cure) | ```
This function has no description.
```
  
[zp_core_respawn_as_zombie](https://amxx-bg.info/api/zp50_core/zp_core_respawn_as_zombie) | ```
Sets whether the player will be respawned as zombie or human.
```
  
[zp_fw_core_infect](https://amxx-bg.info/api/zp50_core/zp_fw_core_infect) | ```
Called when a player gets infected.
```
  
[zp_fw_core_infect_post](https://amxx-bg.info/api/zp50_core/zp_fw_core_infect_post) | ```
This function has no description.
```
  
[zp_fw_core_cure](https://amxx-bg.info/api/zp50_core/zp_fw_core_cure) | ```
Called when a player turns back to human.
```
  
[zp_fw_core_cure_post](https://amxx-bg.info/api/zp50_core/zp_fw_core_cure_post) | ```
This function has no description.
```
  
[zp_fw_core_infect_pre](https://amxx-bg.info/api/zp50_core/zp_fw_core_infect_pre) | ```
Called on a player infect/cure attempt. You can block it by
returning PLUGIN_HANDLED in your plugin.
```
  
[zp_fw_core_cure_pre](https://amxx-bg.info/api/zp50_core/zp_fw_core_cure_pre) | ```
This function has no description.
```
  
[zp_fw_core_last_zombie](https://amxx-bg.info/api/zp50_core/zp_fw_core_last_zombie) | ```
Called when a player becomes the last zombie/human.

Note: This is called for the first zombie too.
```
  
[zp_fw_core_last_human](https://amxx-bg.info/api/zp50_core/zp_fw_core_last_human) | ```
This function has no description.
```
  
[zp_fw_core_spawn_post](https://amxx-bg.info/api/zp50_core/zp_fw_core_spawn_post) | ```
Called when a player spawns, before applying human/zombie attributes to him.
```
  

This code is a part of zp50_core.inc. To use this code you should include zp50_core.inc as ```#include <zp50_core>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.