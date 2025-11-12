# Functions in zp50_items.inc
Function | Description  
---|---  
[zp_items_register](https://amxx-bg.info/api/zp50_items/zp_items_register) | ```
Registers a custom item which will be added to the extra items menu of ZP.

Note: The returned item ID can be later used to catch item
selection events for the zp_item_select_() forwards.
```
  
[zp_items_get_id](https://amxx-bg.info/api/zp50_items/zp_items_get_id) | ```
Returns an item's ID.
```
  
[zp_items_get_name](https://amxx-bg.info/api/zp50_items/zp_items_get_name) | ```
Returns an item's name.
```
  
[zp_items_get_real_name](https://amxx-bg.info/api/zp50_items/zp_items_get_real_name) | ```
Returns an item's real name (used when registering the item).
```
  
[zp_items_get_cost](https://amxx-bg.info/api/zp50_items/zp_items_get_cost) | ```
Returns an item's cost.
```
  
[zp_items_show_menu](https://amxx-bg.info/api/zp50_items/zp_items_show_menu) | ```
Shows menu with available extra items for player.
```
  
[zp_items_force_buy](https://amxx-bg.info/api/zp50_items/zp_items_force_buy) | ```
Forces a player to buy an extra item.
```
  
[zp_items_menu_text_add](https://amxx-bg.info/api/zp50_items/zp_items_menu_text_add) | ```
Appends text to an item being displayed on the extra items menu.
Use this on the item select pre forward.
```
  
[zp_fw_items_select_pre](https://amxx-bg.info/api/zp50_items/zp_fw_items_select_pre) | ```
Called when determining whether an item should be available to a player.

Possible return values are:
 - ZP_ITEM_AVAILABLE (show in menu, allow selection)
 - ZP_ITEM_NOT_AVAILABLE (show in menu, don't allow selection)
 - ZP_ITEM_DONT_SHOW (don't show in menu, don't allow selection)
```
  
[zp_fw_items_select_post](https://amxx-bg.info/api/zp50_items/zp_fw_items_select_post) | ```
Called after a player selected an item from the extra items menu.
```
  

This code is a part of zp50_items.inc. To use this code you should include zp50_items.inc as ```#include <zp50_items>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The include comes bundled with the Zombie Plague 5.0 mod for Counter-Strike 1.6 and will not work with other games (Half-Life, DoD, etc.) or without the Zombie Plague 5.0 mod installed.