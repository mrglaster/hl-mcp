# Functions in zp50_class_human.inc
Function | Description  
---|---  
[zp_class_human_get_current](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_current) | ```
Returns a player's current human class ID.
```
  
[zp_class_human_get_next](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_next) | ```
Returns a player's next human class ID (for the next infection).
```
  
[zp_class_human_set_next](https://amxx-bg.info/api/zp50_class_human/zp_class_human_set_next) | ```
Sets a player's next human class ID (for the next infection).
```
  
[zp_class_human_get_max_health](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_max_health) | ```
Returns the default maximum health for a specific human class.

Note: does not take into account any kind of HP bonuses.
```
  
[zp_class_human_register](https://amxx-bg.info/api/zp50_class_human/zp_class_human_register) | ```
Registers a custom class which will be added to the human classes menu of ZP.

Note: The returned human class ID can be later used to identify
the class when calling the zp_get_user_human_class() natives.
```
  
[zp_class_human_register_model](https://amxx-bg.info/api/zp50_class_human/zp_class_human_register_model) | ```
Registers a custom player model for a given human class.
```
  
[zp_class_human_get_id](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_id) | ```
Returns a human class' ID.
```
  
[zp_class_human_get_name](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_name) | ```
Returns a human class' name.
```
  
[zp_class_human_get_real_name](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_real_name) | ```
Returns a human class' real name (used when registering the class).
```
  
[zp_class_human_get_desc](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_desc) | ```
Returns a human class' description.
```
  
[zp_class_human_get_count](https://amxx-bg.info/api/zp50_class_human/zp_class_human_get_count) | ```
Returns number of registered human classes.
```
  
[zp_class_human_show_menu](https://amxx-bg.info/api/zp50_class_human/zp_class_human_show_menu) | ```
Shows menu with available human classes to a player.
```
  
[zp_class_human_menu_text_add](https://amxx-bg.info/api/zp50_class_human/zp_class_human_menu_text_add) | ```
Appends text to a class being displayed on the human classes menu.
Use this on the class select pre forward.
```
  
[zp_fw_class_human_select_pre](https://amxx-bg.info/api/zp50_class_human/zp_fw_class_human_select_pre) | ```
Called when determining whether a class should be available to a player.

Possible return values are:
 - ZP_CLASS_AVAILABLE (show in menu, allow selection)
 - ZP_CLASS_NOT_AVAILABLE (show in menu, don't allow selection)
 - ZP_CLASS_DONT_SHOW (don't show in menu, don't allow selection)
```
  
[zp_fw_class_human_select_post](https://amxx-bg.info/api/zp50_class_human/zp_fw_class_human_select_post) | ```
Called right after a player selects a class from the menu.
```
  

This code is a part of zp50_class_human.inc. To use this code you should include zp50_class_human.inc as ```#include <zp50_class_human>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.