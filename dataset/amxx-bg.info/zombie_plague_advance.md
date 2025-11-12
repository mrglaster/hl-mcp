# Functions in zombie_plague_advance.inc
Function | Description  
---|---  
[zp_get_user_zombie](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_zombie) | ```
Returns whether a player is a zombie.
```
  
[zp_get_user_nemesis](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_nemesis) | ```
Returns whether a player is a nemesis.
```
  
[zp_get_user_survivor](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_survivor) | ```
Returns whether a player is a survivor.
```
  
[zp_get_user_first_zombie](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_first_zombie) | ```
Returns whether a player is the first zombie.
```
  
[zp_get_user_last_zombie](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_last_zombie) | ```
Returns whether a player is the last zombie.
```
  
[zp_get_user_last_human](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_last_human) | ```
Returns whether a player is the last human.
```
  
[zp_get_user_zombie_class](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_zombie_class) | ```
Returns a player's current zombie class ID.
```
  
[zp_get_user_next_class](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_next_class) | ```
Returns a player's next zombie class ID (for the next infection).
```
  
[zp_set_user_zombie_class](https://amxx-bg.info/api/zombie_plague_advance/zp_set_user_zombie_class) | ```
Sets a player's next zombie class ID (for the next infection).
```
  
[zp_get_user_ammo_packs](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_ammo_packs) | ```
Returns a player's ammo pack count.
```
  
[zp_set_user_ammo_packs](https://amxx-bg.info/api/zombie_plague_advance/zp_set_user_ammo_packs) | ```
Sets a player's ammo pack count.
```
  
[zp_get_zombie_maxhealth](https://amxx-bg.info/api/zombie_plague_advance/zp_get_zombie_maxhealth) | ```
Returns the default maximum health of a zombie.

Note: Takes into account first zombie's HP multiplier.
```
  
[zp_get_user_batteries](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_batteries) | ```
Returns a player's custom flashlight batteries charge.
```
  
[zp_set_user_batteries](https://amxx-bg.info/api/zombie_plague_advance/zp_set_user_batteries) | ```
Sets a player's custom flashlight batteries charge.
```
  
[zp_get_user_nightvision](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_nightvision) | ```
Returns whether a player has night vision.
```
  
[zp_set_user_nightvision](https://amxx-bg.info/api/zombie_plague_advance/zp_set_user_nightvision) | ```
Sets whether a player has night vision.
```
  
[zp_infect_user](https://amxx-bg.info/api/zombie_plague_advance/zp_infect_user) | ```
Forces a player to become a zombie.

Note: Unavailable for last human/survivor/sniper.
```
  
[zp_disinfect_user](https://amxx-bg.info/api/zombie_plague_advance/zp_disinfect_user) | ```
Forces a player to become a human.

Note: Unavailable for last zombie/nemesis.
```
  
[zp_make_user_nemesis](https://amxx-bg.info/api/zombie_plague_advance/zp_make_user_nemesis) | ```
Forces a player to become a nemesis.

Note: Unavailable for last human/survivor/sniper.
```
  
[zp_make_user_survivor](https://amxx-bg.info/api/zombie_plague_advance/zp_make_user_survivor) | ```
Forces a player to become a survivor.

Note: Unavailable for last zombie/nemesis.
```
  
[zp_respawn_user](https://amxx-bg.info/api/zombie_plague_advance/zp_respawn_user) | ```
Respawns a player into a specific team.
```
  
[zp_force_buy_extra_item](https://amxx-bg.info/api/zombie_plague_advance/zp_force_buy_extra_item) | ```
Forces a player to buy an extra item.
```
  
[zp_get_user_sniper](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_sniper) | ```
Returns whether a player is a sniper.
```
  
[zp_make_user_sniper](https://amxx-bg.info/api/zombie_plague_advance/zp_make_user_sniper) | ```
Forces a player to become a sniper.

Note: Unavailable for last zombie/nemesis/assassin.
```
  
[zp_get_user_assassin](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_assassin) | ```
Returns whether a player is an assassin.
```
  
[zp_make_user_assassin](https://amxx-bg.info/api/zombie_plague_advance/zp_make_user_assassin) | ```
Forces a player to become a assassin.

Note: Unavailable for last human/survivor/sniper.
```
  
[zp_has_round_started](https://amxx-bg.info/api/zombie_plague_advance/zp_has_round_started) | ```
Returns whether the ZP round has started, i.e. first zombie
has been chosen or a game mode has begun.
```
  
[zp_is_nemesis_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_nemesis_round) | ```
Returns whether the current round is a nemesis round.
```
  
[zp_is_survivor_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_survivor_round) | ```
Returns whether the current round is a survivor round.
```
  
[zp_is_swarm_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_swarm_round) | ```
Returns whether the current round is a swarm round.
```
  
[zp_is_plague_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_plague_round) | ```
Returns whether the current round is a plague round.
```
  
[zp_is_lnj_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_lnj_round) | ```
Returns whether the current round is a Armageddon round.
```
  
[zp_get_zombie_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_zombie_count) | ```
Returns number of alive zombies.
```
  
[zp_get_human_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_human_count) | ```
Returns number of alive humans.
```
  
[zp_get_nemesis_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_nemesis_count) | ```
Returns number of alive nemesis.
```
  
[zp_get_survivor_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_survivor_count) | ```
Returns number of alive survivors.
```
  
[zp_is_sniper_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_sniper_round) | ```
Returns whether the current round is a sniper round.
```
  
[zp_is_assassin_round](https://amxx-bg.info/api/zombie_plague_advance/zp_is_assassin_round) | ```
Returns whether the current round is a assassin round.
```
  
[zp_get_sniper_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_sniper_count) | ```
Returns number of alive snipers.
```
  
[zp_get_assassin_count](https://amxx-bg.info/api/zombie_plague_advance/zp_get_assassin_count) | ```
Returns number of alive assassins.
```
  
[zp_get_current_mode](https://amxx-bg.info/api/zombie_plague_advance/zp_get_current_mode) | ```
Returns the current game mode ID

Note: For default game modes you can use, for eg. MODE_SWARM,
to check if the current round is swarm mode.

Note: For custom game modes you must have the custom game
mode ID to detect it
```
  
[zp_get_user_model](https://amxx-bg.info/api/zombie_plague_advance/zp_get_user_model) | ```
Allows you to properly retrieve a player's model

Note: You should use this native for retrieving a player's
current model instead of other methods

Note: The model name which is retrieved is the model's folder
name for eg: zombie_source and is not the model's actual name.
```
  
[zp_set_user_model](https://amxx-bg.info/api/zombie_plague_advance/zp_set_user_model) | ```
Properly sets the given model for the player.

Note: You should use this native for setting a player's model
instead of other methods.

Note: The model name which is passed should be the model's folder
name for eg: zombie_source and the folder should contain the
actual model file in it eg: zombie_source.mdl

Note: The model you are setting should be precached in the
sub-plugin using the plugin_precache forward to prevent problems.

Note: It is highly advised to set the models with an additional
delay during round start to prevent SVC_BAD errors/kicks.
```
  
[zp_get_extra_item_id](https://amxx-bg.info/api/zombie_plague_advance/zp_get_extra_item_id) | ```
Returns an extra item's ID.
```
  
[zp_get_zombie_class_id](https://amxx-bg.info/api/zombie_plague_advance/zp_get_zombie_class_id) | ```
Returns a zombie class' ID.
```
  
[zp_register_game_mode](https://amxx-bg.info/api/zombie_plague_advance/zp_register_game_mode) | ```
Registers a custom game mode which will be added to the admin menu of ZP

Note: The returned game mode ID can later be used to detect the game mode
which is called in zp_round_started_pre. There you can start the game mode
externally by using this game mode ID.
```
  
[zp_register_extra_item](https://amxx-bg.info/api/zombie_plague_advance/zp_register_extra_item) | ```
Registers a custom item which will be added to the extra items menu of ZP.

Note: The returned extra item ID can be later used to catch item
purchase events for the zp_extra_item_selected() forward.

Note: ZP_TEAM_NEMESIS, ZP_TEAM_SURVIVOR, ZP_TEAM_ASSASSIN and ZP_TEAM_SNIPER
can be used to make an item available to Nemesis,
Survivors, Assassins and Snipers.
```
  
[zp_register_zombie_class](https://amxx-bg.info/api/zombie_plague_advance/zp_register_zombie_class) | ```
Registers a custom class which will be added to the zombie classes menu of ZP.

Note: The returned zombie class ID can be later used to identify
the class when calling the zp_get_user_zombie_class() natives.
```
  
[zp_round_started](https://amxx-bg.info/api/zombie_plague_advance/zp_round_started) | ```
Called when the ZP round starts, i.e. first zombie
is chosen or a game mode begins.
```
  
[zp_round_started_pre](https://amxx-bg.info/api/zombie_plague_advance/zp_round_started_pre) | ```
Called before the ZP round starts. This is only
called for custom game modes.

Note: The custom game mode id can be used to start
the game mode externally

Note: returning ZP_PLUGIN_HANDLED will cause the
game mode to be blocked and other game modes will
be given a chance.
```
  
[zp_round_ended](https://amxx-bg.info/api/zombie_plague_advance/zp_round_ended) | ```
Called when the round ends.
```
  
[zp_user_infected_pre](https://amxx-bg.info/api/zombie_plague_advance/zp_user_infected_pre) | ```
Called when a player gets infected.
```
  
[zp_user_infected_post](https://amxx-bg.info/api/zombie_plague_advance/zp_user_infected_post) | ```
This function has no description.
```
  
[zp_user_humanized_pre](https://amxx-bg.info/api/zombie_plague_advance/zp_user_humanized_pre) | ```
This function has no description.
```
  
[zp_user_humanized_post](https://amxx-bg.info/api/zombie_plague_advance/zp_user_humanized_post) | ```
This function has no description.
```
  
[zp_user_infect_attempt](https://amxx-bg.info/api/zombie_plague_advance/zp_user_infect_attempt) | ```
Called on a player infect/cure attempt. You can use this to block
an infection/humanization by returning ZP_PLUGIN_HANDLED in your plugin.

Note: Right now this is only available after the ZP round starts, since some
situations (like blocking a first zombie's infection) are not yet handled.
```
  
[zp_user_humanize_attempt](https://amxx-bg.info/api/zombie_plague_advance/zp_user_humanize_attempt) | ```
This function has no description.
```
  
[zp_game_mode_selected](https://amxx-bg.info/api/zombie_plague_advance/zp_game_mode_selected) | ```
Called when an admin selects a custom game mode from the ZP admin menu.

Note: You should trigger the custom game mode here with out any checks
```
  
[zp_extra_item_selected](https://amxx-bg.info/api/zombie_plague_advance/zp_extra_item_selected) | ```
Called when a player buys an extra item from the ZP menu.

Note: You can now return ZP_PLUGIN_HANDLED in your plugin to block
the purchase and the player will be automatically refunded.
```
  
[zp_user_unfrozen](https://amxx-bg.info/api/zombie_plague_advance/zp_user_unfrozen) | ```
Called when a player gets unfrozen (frostnades).
```
  
[zp_user_last_zombie](https://amxx-bg.info/api/zombie_plague_advance/zp_user_last_zombie) | ```
Called when a player becomes the last zombie.

Note: This is called for the first zombie too.
```
  
[zp_user_last_human](https://amxx-bg.info/api/zombie_plague_advance/zp_user_last_human) | ```
Called when a player becomes the last human.
```
  
[zp_player_spawn_post](https://amxx-bg.info/api/zombie_plague_advance/zp_player_spawn_post) | ```
Called when a player spawns. This is also called for CZ bots
which are spawning.

Note: You should use this, instead of other spawn forwards,
for changing a player's class after the player's spawn.
```
  

This code is a part of zombie_plague_advance.inc. To use this code you should include zombie_plague_advance.inc as ```#include <zombie_plague_advance>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.