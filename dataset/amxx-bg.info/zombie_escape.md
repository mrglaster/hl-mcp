# Functions in zombie_escape.inc
Function | Description  
---|---  
[ze_roundend](https://amxx-bg.info/api/zombie_escape/ze_roundend) | ```
Description:     Called on round end event.
```
  
[ze_user_humanized](https://amxx-bg.info/api/zombie_escape/ze_user_humanized) | ```
Description: Called after user humanized, it called whenever
             ze_set_user_human(id) native used.
             It's called also at every new round when all players humanized.
```
  
[ze_user_infected_pre](https://amxx-bg.info/api/zombie_escape/ze_user_infected_pre) | ```
Description:     Called before user get infected by player.
```
  
[ze_user_infected](https://amxx-bg.info/api/zombie_escape/ze_user_infected) | ```
Description:     Called when user infected by player or by the server.
                 Called also at the first choose of zombies (in this case server is the infector).
```
  
[ze_zombie_appear](https://amxx-bg.info/api/zombie_escape/ze_zombie_appear) | ```
Description: Called when zombies chosen.
```
  
[ze_zombie_release](https://amxx-bg.info/api/zombie_escape/ze_zombie_release) | ```
Description: Called when the chosen zombies released.
```
  
[ze_game_started](https://amxx-bg.info/api/zombie_escape/ze_game_started) | ```
Description: Called every new round if game started.
```
  
[ze_fire_pre](https://amxx-bg.info/api/zombie_escape/ze_fire_pre) | ```
Description:  Called before zombie (or human) get fired by fire nade.
```
  
[ze_frost_pre](https://amxx-bg.info/api/zombie_escape/ze_frost_pre) | ```
Description: Called before zombie (or human) get frozen by frost nade.
```
  
[ze_frost_unfreeze](https://amxx-bg.info/api/zombie_escape/ze_frost_unfreeze) | ```
Description: Called when zombie get unfrozen.
```
  
[ze_select_item_pre](https://amxx-bg.info/api/zombie_escape/ze_select_item_pre) | ```
Description:         Called when player opens the extra-items menu.
                     Or when he choose the item but before he get it.
```
  
[ze_select_item_post](https://amxx-bg.info/api/zombie_escape/ze_select_item_post) | ```
Description:         Called after player choose the item,
                     called only if ze_select_item_pre() returned ZE_ITEM_AVAILABLE.
```
  
[ze_player_disconnect](https://amxx-bg.info/api/zombie_escape/ze_player_disconnect) | ```
Description:          Called when player disconnect.
```
  
[ze_is_user_zombie](https://amxx-bg.info/api/zombie_escape/ze_is_user_zombie) | ```
Description: Check if user zombie or not.
```
  
[ze_is_game_started](https://amxx-bg.info/api/zombie_escape/ze_is_game_started) | ```
Description: Check if game started (Zombie Escape Mod) or not.
             Game start when minimun required players connected.
```
  
[ze_is_zombie_frozen](https://amxx-bg.info/api/zombie_escape/ze_is_zombie_frozen) | ```
Description: Check if this zombie in pre-release time or not.
             Pre-Release time is said to be freeze time for zombies.
```
  
[ze_get_round_number](https://amxx-bg.info/api/zombie_escape/ze_get_round_number) | ```
Description: Return current round number (Integer).
             First round is round 1, second is 2 ... etc.
```
  
[ze_get_humans_number](https://amxx-bg.info/api/zombie_escape/ze_get_humans_number) | ```
Description: Return alive humans number (Integer).
```
  
[ze_get_zombies_number](https://amxx-bg.info/api/zombie_escape/ze_get_zombies_number) | ```
Description: Return alive zombies number (Integer).
```
  
[ze_set_user_zombie](https://amxx-bg.info/api/zombie_escape/ze_set_user_zombie) | ```
Description: Set user to zombie team.
```
  
[ze_set_user_human](https://amxx-bg.info/api/zombie_escape/ze_set_user_human) | ```
Description: Set user to human team.
```
  
[ze_set_human_speed_factor](https://amxx-bg.info/api/zombie_escape/ze_set_human_speed_factor) | ```
Description:     Increase human speed with this factor.
                 This factor added to his current speed depend on which weapon he carries.
```
  
[ze_reset_human_speed](https://amxx-bg.info/api/zombie_escape/ze_reset_human_speed) | ```
Description: Reset human speed to default value used in ze_human_speed_factor cvar.
```
  
[ze_set_zombie_speed](https://amxx-bg.info/api/zombie_escape/ze_set_zombie_speed) | ```
Description:     Set this zombie speed to custom value.
```
  
[ze_reset_zombie_speed](https://amxx-bg.info/api/zombie_escape/ze_reset_zombie_speed) | ```
Description: Reset zombie speed to default value used in ze_zombie_speed cvar.
```
  
[ze_get_escape_coins](https://amxx-bg.info/api/zombie_escape/ze_get_escape_coins) | ```
Description: Get player escape coins.
```
  
[ze_set_escape_coins](https://amxx-bg.info/api/zombie_escape/ze_set_escape_coins) | ```
Description:     Set player escape coins.
```
  
[ze_get_escape_leader_id](https://amxx-bg.info/api/zombie_escape/ze_get_escape_leader_id) | ```
Description:     Get escape leader index.
```
  
[ze_stop_mod_rendering](https://amxx-bg.info/api/zombie_escape/ze_stop_mod_rendering) | ```
Description:     Stop/Resume setting rendering from ze_effects_messages.sma plugin.
```
  
[ze_set_fire_grenade](https://amxx-bg.info/api/zombie_escape/ze_set_fire_grenade) | ```
Description: Used to set/stop fire on zombie.
```
  
[ze_zombie_in_fire](https://amxx-bg.info/api/zombie_escape/ze_zombie_in_fire) | ```
Description: Tells you if this zombie burning now or not.
```
  
[ze_set_frost_grenade](https://amxx-bg.info/api/zombie_escape/ze_set_frost_grenade) | ```
Description: Used to set/stop freeze on zombie.
```
  
[ze_zombie_in_forst](https://amxx-bg.info/api/zombie_escape/ze_zombie_in_forst) | ```
Description: Tells you if this zombie frozen now or not.
```
  
[ze_register_item](https://amxx-bg.info/api/zombie_escape/ze_register_item) | ```
Description:         Register extra-item in the items-menu.
```
  
[ze_show_items_menu](https://amxx-bg.info/api/zombie_escape/ze_show_items_menu) | ```
Description: Open items menu for specific player.
```
  
[ze_force_buy_item](https://amxx-bg.info/api/zombie_escape/ze_force_buy_item) | ```
Description:         Force player to buy specific extra-item.
```
  
[ze_get_item_id](https://amxx-bg.info/api/zombie_escape/ze_get_item_id) | ```
Description:         Get item id by it's name.
```
  
[ze_get_item_cost](https://amxx-bg.info/api/zombie_escape/ze_get_item_cost) | ```
Description:         Get item cost (Integer) by it's id.
```
  
[ze_add_text_to_item](https://amxx-bg.info/api/zombie_escape/ze_add_text_to_item) | ```
Description:     Add extra-text to the item name.
```
  
[ze_get_item_limit](https://amxx-bg.info/api/zombie_escape/ze_get_item_limit) | ```
Description:     Return item limit.
```
  
[ze_is_valid_itemid](https://amxx-bg.info/api/zombie_escape/ze_is_valid_itemid) | ```
Description:     Check if this item id is valid or not.
```
  
[ze_get_item_name](https://amxx-bg.info/api/zombie_escape/ze_get_item_name) | ```
Description:     Return the item name by it's id.
```
  
[ze_set_item_level](https://amxx-bg.info/api/zombie_escape/ze_set_item_level) | ```
Description:      Set this item for specific level.
```
  
[ze_get_item_level](https://amxx-bg.info/api/zombie_escape/ze_get_item_level) | ```
Description:     Get item level.
```
  
[ze_set_item_vip](https://amxx-bg.info/api/zombie_escape/ze_set_item_vip) | ```
Description:      Set this item for VIPs on specific flag.
```
  
[ze_get_item_vip](https://amxx-bg.info/api/zombie_escape/ze_get_item_vip) | ```
Description:     See if this item for VIP or not, and on which flag.
```
  
[ze_zombie_in_madness](https://amxx-bg.info/api/zombie_escape/ze_zombie_in_madness) | ```
Description: Check if this zombie in madness or not.
```
  
[ze_show_weapon_menu](https://amxx-bg.info/api/zombie_escape/ze_show_weapon_menu) | ```
Description: Show weapon menu for player.
```
  
[ze_is_auto_buy_enabled](https://amxx-bg.info/api/zombie_escape/ze_is_auto_buy_enabled) | ```
Description: Check if auto buy enabled or not.
```
  
[ze_disable_auto_buy](https://amxx-bg.info/api/zombie_escape/ze_disable_auto_buy) | ```
Description: This will disable auto buy for player.
```
  
[ze_set_starting_sounds](https://amxx-bg.info/api/zombie_escape/ze_set_starting_sounds) | ```
Description: Enable and disable Ready&PreRelease sounds for any player.
```
  
[ze_set_ambiance_sounds](https://amxx-bg.info/api/zombie_escape/ze_set_ambiance_sounds) | ```
Description: Enable and disable ambiance sound for any player.
```
  
[ze_is_starting_sounds_enabled](https://amxx-bg.info/api/zombie_escape/ze_is_starting_sounds_enabled) | ```
Description: Check for any player if Ready&PreRelease sounds enabled or disabled.
```
  
[ze_is_ambiance_sounds_enabled](https://amxx-bg.info/api/zombie_escape/ze_is_ambiance_sounds_enabled) | ```
Description: Check for any player if ambiance sounds enabled or disabled.
```
  
[ze_user_humanized_pre](https://amxx-bg.info/api/zombie_escape/ze_user_humanized_pre) | ```
Description: Called when user humanized, it called whenever
             ze_set_user_human(id) native used.
             It's called also at every new round when all players humanized.
```
  
[ze_zombie_appear_ex](https://amxx-bg.info/api/zombie_escape/ze_zombie_appear_ex) | ```
Description: Called when zombies chosen.
```
  
[ze_game_started_pre](https://amxx-bg.info/api/zombie_escape/ze_game_started_pre) | ```
Description: Called every new round if game started.
```
  
[ze_player_spawn_post](https://amxx-bg.info/api/zombie_escape/ze_player_spawn_post) | ```
Description:     Called when player spawn.
```
  
[ze_gamemode_chosen_pre](https://amxx-bg.info/api/zombie_escape/ze_gamemode_chosen_pre) | ```
Description:         Called before game mode chosen.
```
  
[ze_gamemode_chosen](https://amxx-bg.info/api/zombie_escape/ze_gamemode_chosen) | ```
Description:     Called when game mode chosen.
```
  
[ze_user_last_human](https://amxx-bg.info/api/zombie_escape/ze_user_last_human) | ```
Description: Called when player become last Human.
```
  
[ze_user_last_zombie](https://amxx-bg.info/api/zombie_escape/ze_user_last_zombie) | ```
Description: Called when player become last Zombie.
```
  
[ze_is_user_zombie_ex](https://amxx-bg.info/api/zombie_escape/ze_is_user_zombie_ex) | ```
Description: Check if user zombie or not
             If player not found is will return false not NULLENT.
```
  
[ze_set_user_zombie_ex](https://amxx-bg.info/api/zombie_escape/ze_set_user_zombie_ex) | ```
Description: Set user to zombie team.
```
  
[ze_get_user_knockback](https://amxx-bg.info/api/zombie_escape/ze_get_user_knockback) | ```
Description: Get user knockback.
```
  
[ze_get_user_knockback_f](https://amxx-bg.info/api/zombie_escape/ze_get_user_knockback_f) | ```
Description: Get user knockback (Float value).
```
  
[ze_set_user_knockback](https://amxx-bg.info/api/zombie_escape/ze_set_user_knockback) | ```
Description: Set user knockback.
```
  
[ze_reset_user_knockback](https://amxx-bg.info/api/zombie_escape/ze_reset_user_knockback) | ```
Description: Reset user knockback to use value from CVAR.
```
  
[ze_set_user_gravity](https://amxx-bg.info/api/zombie_escape/ze_set_user_gravity) | ```
Description:         Set user gravity.
```
  
[ze_reset_user_gravity](https://amxx-bg.info/api/zombie_escape/ze_reset_user_gravity) | ```
Description: Reset user gravity to use value from CVAR.
```
  
[ze_remove_zombie_freeze_msg](https://amxx-bg.info/api/zombie_escape/ze_remove_zombie_freeze_msg) | ```
Description: Remove zombie freeze time message.
```
  
[ze_give_escape_coins](https://amxx-bg.info/api/zombie_escape/ze_give_escape_coins) | ```
Description:     Give player escape coins.
```
  
[ze_set_fire_grenade_ex](https://amxx-bg.info/api/zombie_escape/ze_set_fire_grenade_ex) | ```
Description: Used to set fire on zombie with duration.
```
  
[ze_set_frost_grenade_ex](https://amxx-bg.info/api/zombie_escape/ze_set_frost_grenade_ex) | ```
Description: Used to set/stop freeze on zombie with specific duration.
```
  
[ze_get_item_global_limit](https://amxx-bg.info/api/zombie_escape/ze_get_item_global_limit) | ```
Description:     Return item global limit.
```
  
[ze_show_user_hud_info](https://amxx-bg.info/api/zombie_escape/ze_show_user_hud_info) | ```
Description:     Show HUDs info for player.
```
  
[ze_hide_user_hud_info](https://amxx-bg.info/api/zombie_escape/ze_hide_user_hud_info) | ```
Description:     Hide HUDs info for player.
```
  
[ze_allow_respawn_as_zombie](https://amxx-bg.info/api/zombie_escape/ze_allow_respawn_as_zombie) | ```
Description:     Allow spawning player Zombie.
```
  
[ze_disallow_respawn_as_zombie](https://amxx-bg.info/api/zombie_escape/ze_disallow_respawn_as_zombie) | ```
Description:     Disallow spawning player Zombie.
```
  
[ze_gamemode_register](https://amxx-bg.info/api/zombie_escape/ze_gamemode_register) | ```
Description:     Registers a new game mode.
```
  
[ze_gamemode_set_default](https://amxx-bg.info/api/zombie_escape/ze_gamemode_set_default) | ```
Description:     Sets a default game mode.
```
  
[ze_gamemode_get_current](https://amxx-bg.info/api/zombie_escape/ze_gamemode_get_current) | ```
Description:     Gets a current game mode.
```
  
[ze_gamemode_get_name](https://amxx-bg.info/api/zombie_escape/ze_gamemode_get_name) | ```
Description:     Gets a game mode's name.
```
  
[ze_gamemode_get_id](https://amxx-bg.info/api/zombie_escape/ze_gamemode_get_id) | ```
Description:     Gets a game mode's ID.
```
  
[ze_gamemode_get_count](https://amxx-bg.info/api/zombie_escape/ze_gamemode_get_count) | ```
Description:     Get number of registered game modes.
```
  
[ze_gamemode_start](https://amxx-bg.info/api/zombie_escape/ze_gamemode_start) | ```
Description:     Forces a game mode to start and stop countdown.
```
  
[ze_hide_user_rankhud](https://amxx-bg.info/api/zombie_escape/ze_hide_user_rankhud) | ```
Description: Hide rank HUD for specific player.
```
  
[ze_show_user_rankhud](https://amxx-bg.info/api/zombie_escape/ze_show_user_rankhud) | ```
Description: Show rank HUD for specific player.
```
  
[ze_is_user_first_zombie](https://amxx-bg.info/api/zombie_escape/ze_is_user_first_zombie) | ```
Description: Check player is first Zombie or not.
```
  
[ze_is_user_last_zombie](https://amxx-bg.info/api/zombie_escape/ze_is_user_last_zombie) | ```
Description: Check player is last Zombie.
```
  
[ze_is_user_last_human](https://amxx-bg.info/api/zombie_escape/ze_is_user_last_human) | ```
Description: Check player is last Human.
```
  
[ze_get_last_human](https://amxx-bg.info/api/zombie_escape/ze_get_last_human) | ```
Description: Get client index of last Human.
```
  
[ze_get_last_zombie](https://amxx-bg.info/api/zombie_escape/ze_get_last_zombie) | ```
Description: Get client index of last Zombie.
```
  
[ze_set_user_nvg](https://amxx-bg.info/api/zombie_escape/ze_set_user_nvg) | ```
Description: Set player custom Night Vision with colors.
```
  
[ze_reset_user_nvg](https://amxx-bg.info/api/zombie_escape/ze_reset_user_nvg) | ```
Description: Remove player custom Night Vision.
```
  
[ze_is_nvg_on](https://amxx-bg.info/api/zombie_escape/ze_is_nvg_on) | ```
Description: Check Night Vision is ON or OFF.
```
  
[ze_is_user_nemesis](https://amxx-bg.info/api/zombie_escape/ze_is_user_nemesis) | ```
Description: Check player is Nemesis.
```
  
[ze_set_user_nemesis](https://amxx-bg.info/api/zombie_escape/ze_set_user_nemesis) | ```
Description: Set player Nemesis.
```
  
[ze_remove_user_nemesis](https://amxx-bg.info/api/zombie_escape/ze_remove_user_nemesis) | ```
Description: Remove player Nemesis attributes
```
  
[ze_is_round_escape](https://amxx-bg.info/api/zombie_escape/ze_is_round_escape) | ```
Description: Check round is Escape mode.
```
  
[ze_is_round_nemesis](https://amxx-bg.info/api/zombie_escape/ze_is_round_nemesis) | ```
Description: Check round is Nemesis mode.
```
  
[ze_set_user_leap](https://amxx-bg.info/api/zombie_escape/ze_set_user_leap) | ```
Description: Set player Leap (Long-Jump).
```
  
[ze_remove_user_leap](https://amxx-bg.info/api/zombie_escape/ze_remove_user_leap) | ```
Description: Remove player Leap (Long-Jump).
```
  
[ze_block_user_leap](https://amxx-bg.info/api/zombie_escape/ze_block_user_leap) | ```
Description: Block the player use Leap in every team.
```
  
[ze_unblock_user_leap](https://amxx-bg.info/api/zombie_escape/ze_unblock_user_leap) | ```
Description: Unblock the player to use Leap for All teams.
```
  

This code is a part of zombie_escape.inc. To use this code you should include zombie_escape.inc as ```#include <zombie_escape>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. The source of this include is Zombie Escape mod for Counter Strike 1.6.  It won't work with other games (Half-Life, DoD, etc) or without the mod installed