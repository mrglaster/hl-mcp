# Functions in jbshop.inc
Function | Description  
---|---  
[jbshop_initialized](https://amxx-bg.info/api/jbshop/jbshop_initialized) | ```
Called when the shop system is fully initialized.
```
  
[jbshop_shop_created](https://amxx-bg.info/api/jbshop/jbshop_shop_created) | ```
Called when a shop is created. Use this to add additional items to the shop via other plugins.
```
  
[jbshop_shop_selected](https://amxx-bg.info/api/jbshop/jbshop_shop_selected) | ```
Called when the client attempts to open a shop.
```
  
[jbshop_item_selected](https://amxx-bg.info/api/jbshop/jbshop_item_selected) | ```
Called when the client attempts to buy an item from a shop.
```
  
[jbshop_item_removed](https://amxx-bg.info/api/jbshop/jbshop_item_removed) | ```
Called when the client's item is removed
```
  
[jbshop_find_item_by_name](https://amxx-bg.info/api/jbshop/jbshop_find_item_by_name) | ```
Finds the specific shop item's id by its name.
```
  
[jbshop_find_shop_by_command](https://amxx-bg.info/api/jbshop/jbshop_find_shop_by_command) | ```
Finds a shop's id by a command it's registered to.
```
  
[jbshop_find_shop_by_name](https://amxx-bg.info/api/jbshop/jbshop_find_shop_by_name) | ```
Finds a shop's id by its name.
```
  
[jbshop_find_shop_by_key](https://amxx-bg.info/api/jbshop/jbshop_find_shop_by_key) | ```
Finds a shop's id by its key.
```
  
[jbshop_get_item_count](https://amxx-bg.info/api/jbshop/jbshop_get_item_count) | ```
Returns the total number of items in a specified shop.
```
  
[jbshop_get_plugin_prefix](https://amxx-bg.info/api/jbshop/jbshop_get_plugin_prefix) | ```
Returns the plugin's chat prefix.
```
  
[jbshop_get_shop_count](https://amxx-bg.info/api/jbshop/jbshop_get_shop_count) | ```
Returns the total number of registered shops.
```
  
[jbshop_register_item](https://amxx-bg.info/api/jbshop/jbshop_register_item) | ```
Registers a shop item.
```
  
[jbshop_register_shop](https://amxx-bg.info/api/jbshop/jbshop_register_shop) | ```
Registers a shop.
```
  
[jbshop_user_has_item](https://amxx-bg.info/api/jbshop/jbshop_user_has_item) | ```
Checks if the client currently has an item.
```
  
[jbshop_remove_item](https://amxx-bg.info/api/jbshop/jbshop_remove_item) | ```
Removes an item from the client.
```
  
[jbshop_give_item](https://amxx-bg.info/api/jbshop/jbshop_give_item) | ```
Gives the player an item from the specified shop.
```
  
[jbshop_give_item_by_keys](https://amxx-bg.info/api/jbshop/jbshop_give_item_by_keys) | ```
Gives the player an item from the specified shop using keys.
```
  
[jbshop_play_fail_sound](https://amxx-bg.info/api/jbshop/jbshop_play_fail_sound) | ```
Plays the sound that is used when the client cannot purchase an item.
```
  
[jbshop_lock_shop](https://amxx-bg.info/api/jbshop/jbshop_lock_shop) | ```
Locks a specific shop so no players can access it.
The shop stays closed until manually opened with jbshop_unlock_shop()
```
  
[jbshop_unlock_shop](https://amxx-bg.info/api/jbshop/jbshop_unlock_shop) | ```
Unlocks a specific shop.
The shop stays opened unless manually closed with jbshop_lock_shop()
```
  
[jbshop_is_shop_unlocked](https://amxx-bg.info/api/jbshop/jbshop_is_shop_unlocked) | ```
Checks whether a specific shop is unlocked or not.
```
  
[jbshop_open_shop](https://amxx-bg.info/api/jbshop/jbshop_open_shop) | ```
Attempts to open a shop for the client.
```
  
[jbshop_set_item_message](https://amxx-bg.info/api/jbshop/jbshop_set_item_message) | ```
Sets a message that will be displayed in chat after purchasing the item.
```
  
[jbshop_get_shop_key](https://amxx-bg.info/api/jbshop/jbshop_get_shop_key) | ```
Gets a shop's key.
```
  
[jbshop_is_item_class](https://amxx-bg.info/api/jbshop/jbshop_is_item_class) | ```
Checks whether an item class is present
```
  

This code is a part of jbshop.inc. To use this code you should include jbshop.inc as ```#include <jbshop>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.