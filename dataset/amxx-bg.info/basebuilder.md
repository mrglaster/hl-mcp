# Functions in basebuilder.inc
Function | Description  
---|---  
[is_basebuilder_active](https://amxx-bg.info/api/basebuilder/is_basebuilder_active) | ```
Returns whether Base Builder is active.
```
  
[bb_register_zombie_class](https://amxx-bg.info/api/basebuilder/bb_register_zombie_class) | ```
Registers a custom class which will be added to the zombie classes menu of BB.

Note: The returned zombie class ID can be later used to identify
the class when calling the bb_get_user_zombie_class() natives.
```
  
[zp_register_zombie_class](https://amxx-bg.info/api/basebuilder/zp_register_zombie_class) | ```
This function has no description.
```
  
[bb_get_class_cost](https://amxx-bg.info/api/basebuilder/bb_get_class_cost) | ```
Returns a zombie classes cost.
```
  
[bb_get_user_zombie_class](https://amxx-bg.info/api/basebuilder/bb_get_user_zombie_class) | ```
Returns a player's current zombie class ID.
```
  
[zp_get_user_zombie_class](https://amxx-bg.info/api/basebuilder/zp_get_user_zombie_class) | ```
This function has no description.
```
  
[bb_get_user_next_class](https://amxx-bg.info/api/basebuilder/bb_get_user_next_class) | ```
Returns a player's next zombie class ID (when they respawn).
```
  
[zp_get_user_next_class](https://amxx-bg.info/api/basebuilder/zp_get_user_next_class) | ```
This function has no description.
```
  
[bb_set_user_zombie_class](https://amxx-bg.info/api/basebuilder/bb_set_user_zombie_class) | ```
Sets a player's next zombie class ID (when they respawn).
```
  
[zp_set_user_zombie_class](https://amxx-bg.info/api/basebuilder/zp_set_user_zombie_class) | ```
This function has no description.
```
  
[bb_is_user_zombie](https://amxx-bg.info/api/basebuilder/bb_is_user_zombie) | ```
Returns whether a player is a zombie.
```
  
[zp_get_user_zombie](https://amxx-bg.info/api/basebuilder/zp_get_user_zombie) | ```
This function has no description.
```
  
[bb_is_user_banned](https://amxx-bg.info/api/basebuilder/bb_is_user_banned) | ```
Returns whether a player is banned from building.
```
  
[bb_is_build_phase](https://amxx-bg.info/api/basebuilder/bb_is_build_phase) | ```
Returns whether the game is still in the build phase.
```
  
[bb_is_prep_phase](https://amxx-bg.info/api/basebuilder/bb_is_prep_phase) | ```
Returns whether the game is in the preparation phase.
```
  
[bb_get_build_time](https://amxx-bg.info/api/basebuilder/bb_get_build_time) | ```
Returns the current build time (in seconds).
```
  
[bb_set_build_time](https://amxx-bg.info/api/basebuilder/bb_set_build_time) | ```
Sets the build timer to a specified number.
```
  
[bb_get_user_color](https://amxx-bg.info/api/basebuilder/bb_get_user_color) | ```
Returns the players current color ENUM.
```
  
[bb_set_user_color](https://amxx-bg.info/api/basebuilder/bb_set_user_color) | ```
Sets the build timer to a specified number.
```
  
[bb_drop_user_block](https://amxx-bg.info/api/basebuilder/bb_drop_user_block) | ```
Drops the users entity (if he has one).
```
  
[bb_get_user_block](https://amxx-bg.info/api/basebuilder/bb_get_user_block) | ```
Returns the users entity..
```
  
[bb_set_user_block](https://amxx-bg.info/api/basebuilder/bb_set_user_block) | ```
Sets the users current moving block to the entity specified.
```
  
[bb_is_locked_block](https://amxx-bg.info/api/basebuilder/bb_is_locked_block) | ```
Returns whether a block is locked or not.
```
  
[bb_lock_block](https://amxx-bg.info/api/basebuilder/bb_lock_block) | ```
Locks specified block if applicable.
```
  
[bb_unlock_block](https://amxx-bg.info/api/basebuilder/bb_unlock_block) | ```
Unlocks specified block if applicable.
```
  
[bb_release_zombies](https://amxx-bg.info/api/basebuilder/bb_release_zombies) | ```
Releases the zombies if valid.
```
  
[bb_set_user_primary](https://amxx-bg.info/api/basebuilder/bb_set_user_primary) | ```
Sets their "primary weapon" (weapon that is drawn at round start).
```
  
[bb_get_user_primary](https://amxx-bg.info/api/basebuilder/bb_get_user_primary) | ```
Returns their current primary weapon.
```
  
[bb_get_flags_build](https://amxx-bg.info/api/basebuilder/bb_get_flags_build) | ```
Returns current mod admin flags for the following
```
  
[bb_get_flags_lock](https://amxx-bg.info/api/basebuilder/bb_get_flags_lock) | ```
This function has no description.
```
  
[bb_get_flags_buildban](https://amxx-bg.info/api/basebuilder/bb_get_flags_buildban) | ```
This function has no description.
```
  
[bb_get_flags_swap](https://amxx-bg.info/api/basebuilder/bb_get_flags_swap) | ```
This function has no description.
```
  
[bb_get_flags_revive](https://amxx-bg.info/api/basebuilder/bb_get_flags_revive) | ```
This function has no description.
```
  
[bb_get_flags_guns](https://amxx-bg.info/api/basebuilder/bb_get_flags_guns) | ```
This function has no description.
```
  
[bb_get_flags_release](https://amxx-bg.info/api/basebuilder/bb_get_flags_release) | ```
This function has no description.
```
  
[bb_get_flags_override](https://amxx-bg.info/api/basebuilder/bb_get_flags_override) | ```
This function has no description.
```
  
[bb_round_started](https://amxx-bg.info/api/basebuilder/bb_round_started) | ```
Called when the zombies are released
at the end of the build or preparation phase
```
  
[bb_prepphase_started](https://amxx-bg.info/api/basebuilder/bb_prepphase_started) | ```
Called when the preparation phase begins
at the end of the build phase, before zombie release
```
  
[bb_buildphase_started](https://amxx-bg.info/api/basebuilder/bb_buildphase_started) | ```
Called when the build phase begins
When the round starts (logevent)
```
  
[bb_zombie_class_picked](https://amxx-bg.info/api/basebuilder/bb_zombie_class_picked) | ```
Called when a player picks his NEXT zombie class
```
  
[bb_zombie_class_set](https://amxx-bg.info/api/basebuilder/bb_zombie_class_set) | ```
Called when a player has his CURRENT class applied. (respawn)
```
  
[bb_block_pushpull](https://amxx-bg.info/api/basebuilder/bb_block_pushpull) | ```
Called when a player pushes or pulls an entity
```
  
[bb_grab_pre](https://amxx-bg.info/api/basebuilder/bb_grab_pre) | ```
Called when a player grabs an entity
 Before entity successfully grabbed
```
  
[bb_grab_post](https://amxx-bg.info/api/basebuilder/bb_grab_post) | ```
Called when a player grabs an entity
 After the entity is grabbed
```
  
[bb_drop_pre](https://amxx-bg.info/api/basebuilder/bb_drop_pre) | ```
Called when a player drops an entity
 Before entity actually dropped
```
  
[bb_drop_post](https://amxx-bg.info/api/basebuilder/bb_drop_post) | ```
Called when a player drops an entity
 After the entity is dropped
```
  
[bb_new_color](https://amxx-bg.info/api/basebuilder/bb_new_color) | ```
Called when a player receives a new color
 Only when they random or select from menu
```
  
[bb_lock_pre](https://amxx-bg.info/api/basebuilder/bb_lock_pre) | ```
Called when a player locks an entity
 Before entity actually locked
```
  
[bb_lock_post](https://amxx-bg.info/api/basebuilder/bb_lock_post) | ```
Called when a player locks an entity
 After the entity is locked
```
  

This code is a part of basebuilder.inc. To use this code you should include basebuilder.inc as ```#include <basebuilder>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and is provided with basebuilder mod.