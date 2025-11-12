# Functions in zp50_class_zombie.inc
Function | Description  
---|---  
[zp_class_zombie_get_current](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_current) | ```
Returns a player's current zombie class ID.
```
  
[zp_class_zombie_get_next](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_next) | ```
Returns a player's next zombie class ID (for the next infection).
```
  
[zp_class_zombie_set_next](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_set_next) | ```
Sets a player's next zombie class ID (for the next infection).
```
  
[zp_class_zombie_get_max_health](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_max_health) | ```
Returns the default maximum health for a specific zombie class.

Note: does not take into account any kind of HP multipliers.
```
  
[zp_class_zombie_register](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_register) | ```
Registers a custom class which will be added to the zombie classes menu of ZP.

Note: The returned zombie class ID can be later used to identify
the class when calling the zp_get_user_zombie_class() natives.
```
  
[zp_class_zombie_register_model](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_register_model) | ```
Registers a custom player model for a given zombie class.
```
  
[zp_class_zombie_register_claw](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_register_claw) | ```
Registers a custom claw model for a given zombie class.
```
  
[zp_class_zombie_register_kb](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_register_kb) | ```
Registers a zombie class' knockback multiplier.
```
  
[zp_class_zombie_get_id](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_id) | ```
Returns a zombie class' ID.
```
  
[zp_class_zombie_get_name](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_name) | ```
Returns a zombie class' name.
```
  
[zp_class_zombie_get_real_name](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_real_name) | ```
Returns a zombie class' real name (used when registering the class).
```
  
[zp_class_zombie_get_desc](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_desc) | ```
Returns a zombie class' description.
```
  
[zp_class_zombie_get_kb](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_kb) | ```
Returns a zombie class' knockback multiplier.
```
  
[zp_class_zombie_get_count](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_get_count) | ```
Returns number of registered zombie classes.
```
  
[zp_class_zombie_show_menu](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_show_menu) | ```
Shows menu with available zombie classes to a player.
```
  
[zp_class_zombie_menu_text_add](https://amxx-bg.info/api/zp50_class_zombie/zp_class_zombie_menu_text_add) | ```
Appends text to a class being displayed on the zombie classes menu.
Use this on the class select pre forward.
```
  
[zp_fw_class_zombie_select_pre](https://amxx-bg.info/api/zp50_class_zombie/zp_fw_class_zombie_select_pre) | ```
Called when determining whether a class should be available to a player.

Possible return values are:
 - ZP_CLASS_AVAILABLE (show in menu, allow selection)
 - ZP_CLASS_NOT_AVAILABLE (show in menu, don't allow selection)
 - ZP_CLASS_DONT_SHOW (don't show in menu, don't allow selection)
```
  
[zp_fw_class_zombie_select_post](https://amxx-bg.info/api/zp50_class_zombie/zp_fw_class_zombie_select_post) | ```
Called right after a player selects a class from the menu.
```
  

This code is a part of zp50_class_zombie.inc. To use this code you should include zp50_class_zombie.inc as ```#include <zp50_class_zombie>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.