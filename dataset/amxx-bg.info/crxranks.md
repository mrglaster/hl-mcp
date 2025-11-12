# Functions in crxranks.inc
Function | Description  
---|---  
[crxranks_user_level_updated](https://amxx-bg.info/api/crxranks/crxranks_user_level_updated) | ```
Called when the client's level changes.
```
  
[crxranks_user_receive_xp](https://amxx-bg.info/api/crxranks/crxranks_user_receive_xp) | ```
Called right before the client receives XP.
```
  
[crxranks_user_xp_updated](https://amxx-bg.info/api/crxranks/crxranks_user_xp_updated) | ```
Called right after the client's XP amount changes.
```
  
[crxranks_get_chat_prefix](https://amxx-bg.info/api/crxranks/crxranks_get_chat_prefix) | ```
Returns the chat prefix set in the plugin's configuration file.
```
  
[crxranks_get_final_flags](https://amxx-bg.info/api/crxranks/crxranks_get_final_flags) | ```
Returns the flags that clients will receive when they reach the final level.
```
  
[crxranks_get_hudinfo_format](https://amxx-bg.info/api/crxranks/crxranks_get_hudinfo_format) | ```
Returns the HUD info format set in the plugin's configuration file.
```
  
[crxranks_get_max_levels](https://amxx-bg.info/api/crxranks/crxranks_get_max_levels) | ```
Returns the number of available levels.
```
  
[crxranks_get_rank_by_level](https://amxx-bg.info/api/crxranks/crxranks_get_rank_by_level) | ```
Searches for a rank name by a specific level number.
```
  
[crxranks_get_save_type](https://amxx-bg.info/api/crxranks/crxranks_get_save_type) | ```
Returns the data saving type set in the plugin's configuration file.
```
  
[crxranks_get_setting](https://amxx-bg.info/api/crxranks/crxranks_get_setting) | ```
Returns a key value set in the [Settings] section in the plugin's configuration file.
```
  
[crxranks_get_user_hudinfo](https://amxx-bg.info/api/crxranks/crxranks_get_user_hudinfo) | ```
Returns the client's HUD information.
```
  
[crxranks_get_user_level](https://amxx-bg.info/api/crxranks/crxranks_get_user_level) | ```
Returns the client's current level.
```
  
[crxranks_get_user_next_rank](https://amxx-bg.info/api/crxranks/crxranks_get_user_next_rank) | ```
Returns the client's next rank.
```
  
[crxranks_get_user_next_xp](https://amxx-bg.info/api/crxranks/crxranks_get_user_next_xp) | ```
Returns the XP needed for the client to reach the next level.
```
  
[crxranks_get_user_rank](https://amxx-bg.info/api/crxranks/crxranks_get_user_rank) | ```
Returns the client's current rank.
```
  
[crxranks_get_user_xp](https://amxx-bg.info/api/crxranks/crxranks_get_user_xp) | ```
Returns the amount of XP that the client has.
```
  
[crxranks_get_vault_name](https://amxx-bg.info/api/crxranks/crxranks_get_vault_name) | ```
Returns the vault name set in the plugin's configuration file.
```
  
[crxranks_get_vip_flags](https://amxx-bg.info/api/crxranks/crxranks_get_vip_flags) | ```
Returns the VIP flags set in the plugin's configuration file.
```
  
[crxranks_get_xp_for_level](https://amxx-bg.info/api/crxranks/crxranks_get_xp_for_level) | ```
Returns the amount of XP required for a specific level.
```
  
[crxranks_get_xp_reward](https://amxx-bg.info/api/crxranks/crxranks_get_xp_reward) | ```
Returns the XP reward that the client will get in a specific sitaution.
```
  
[crxranks_give_user_xp](https://amxx-bg.info/api/crxranks/crxranks_give_user_xp) | ```
Gives a specific amount of XP to the client.
```
  
[crxranks_has_user_hudinfo](https://amxx-bg.info/api/crxranks/crxranks_has_user_hudinfo) | ```
Checks if the client has HUD information enabled.
```
  
[crxranks_is_hi_using_dhud](https://amxx-bg.info/api/crxranks/crxranks_is_hi_using_dhud) | ```
Checks if the HUD info system is using DHUD messages.
```
  
[crxranks_is_hud_enabled](https://amxx-bg.info/api/crxranks/crxranks_is_hud_enabled) | ```
Checks if the HUD information system is enabled.
```
  
[crxranks_is_sfdn_enabled](https://amxx-bg.info/api/crxranks/crxranks_is_sfdn_enabled) | ```
Checks if the screen fade when a client loses a level is enabled.
```
  
[crxranks_is_sfup_enabled](https://amxx-bg.info/api/crxranks/crxranks_is_sfup_enabled) | ```
Checks if the screen fade when a client gains a level is enabled.
```
  
[crxranks_is_user_on_final](https://amxx-bg.info/api/crxranks/crxranks_is_user_on_final) | ```
Checks if the client is on the final level.
```
  
[crxranks_is_user_vip](https://amxx-bg.info/api/crxranks/crxranks_is_user_vip) | ```
Checks if the client is VIP according to the VIP flags set in the plugin's configuration file.
```
  
[crxranks_is_using_mysql](https://amxx-bg.info/api/crxranks/crxranks_is_using_mysql) | ```
Checks if the plugin is using MySQL to save/load XP.
```
  
[crxranks_is_xpn_enabled](https://amxx-bg.info/api/crxranks/crxranks_is_xpn_enabled) | ```
Checks if the XP notifier system is enabled.
```
  
[crxranks_is_xpn_using_dhud](https://amxx-bg.info/api/crxranks/crxranks_is_xpn_using_dhud) | ```
Checks if the XP notifier system is using DHUD messages.
```
  
[crxranks_set_user_xp](https://amxx-bg.info/api/crxranks/crxranks_set_user_xp) | ```
Sets the exact amount of XP that th client has.
```
  
[crxranks_using_combined_events](https://amxx-bg.info/api/crxranks/crxranks_using_combined_events) | ```
Checks if the plugin's option to use combined events is enabled.
```
  

This code is a part of crxranks.inc. To use this code you should include crxranks.inc as ```#include <crxranks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.