# Functions in reapi_gamedll.inc
Function | Description  
---|---  
[SetThink](https://amxx-bg.info/api/reapi_gamedll/SetThink) | ```
Sets Think callback for entity
```
  
[SetTouch](https://amxx-bg.info/api/reapi_gamedll/SetTouch) | ```
Sets Touch callback for entity
```
  
[SetUse](https://amxx-bg.info/api/reapi_gamedll/SetUse) | ```
Sets Use callback for entity
```
  
[SetBlocked](https://amxx-bg.info/api/reapi_gamedll/SetBlocked) | ```
Sets Blocked callback for entity
```
  
[SetMoveDone](https://amxx-bg.info/api/reapi_gamedll/SetMoveDone) | ```
Sets MoveDone callback for entity
```
  
[set_member_game](https://amxx-bg.info/api/reapi_gamedll/set_member_game) | ```
Sets a value to CSGameRules_Members members.
```
  
[get_member_game](https://amxx-bg.info/api/reapi_gamedll/get_member_game) | ```
Returns a value from CSGameRules_Members members
```
  
[set_member](https://amxx-bg.info/api/reapi_gamedll/set_member) | ```
Sets a value to an entity's member.
```
  
[get_member](https://amxx-bg.info/api/reapi_gamedll/get_member) | ```
Returns a value from an entity's member.
```
  
[set_pmove](https://amxx-bg.info/api/reapi_gamedll/set_pmove) | ```
Sets playermove var.
```
  
[get_pmove](https://amxx-bg.info/api/reapi_gamedll/get_pmove) | ```
Returns a playermove var.
```
  
[set_movevar](https://amxx-bg.info/api/reapi_gamedll/set_movevar) | ```
Sets a movevar value to a playermove.
```
  
[get_movevar](https://amxx-bg.info/api/reapi_gamedll/get_movevar) | ```
Returns a movevar value from a playermove.
```
  
[set_pmtrace](https://amxx-bg.info/api/reapi_gamedll/set_pmtrace) | ```
Sets a pmtrace var.
```
  
[get_pmtrace](https://amxx-bg.info/api/reapi_gamedll/get_pmtrace) | ```
Returns a pmtrace var
```
  
[set_rebuy](https://amxx-bg.info/api/reapi_gamedll/set_rebuy) | ```
Sets a RebuyStruct member.
```
  
[get_rebuy](https://amxx-bg.info/api/reapi_gamedll/get_rebuy) | ```
Returns a RebuyStruct member
```
  
[rg_set_animation](https://amxx-bg.info/api/reapi_gamedll/rg_set_animation) | ```
Assign the number of the player's animation.
```
  
[rg_add_account](https://amxx-bg.info/api/reapi_gamedll/rg_add_account) | ```
Adds money to player's account.
```
  
[rg_give_item](https://amxx-bg.info/api/reapi_gamedll/rg_give_item) | ```
Gives the player an item.
```
  
[rg_give_custom_item](https://amxx-bg.info/api/reapi_gamedll/rg_give_custom_item) | ```
Gives the player an custom item, this means that don't handled API things.
```
  
[rg_give_default_items](https://amxx-bg.info/api/reapi_gamedll/rg_give_default_items) | ```
Give the default items to a player.
```
  
[rg_give_shield](https://amxx-bg.info/api/reapi_gamedll/rg_give_shield) | ```
Gives the player a shield
```
  
[rg_dmg_radius](https://amxx-bg.info/api/reapi_gamedll/rg_dmg_radius) | ```
Inflicts damage in a radius from the source position.
```
  
[rg_multidmg_clear](https://amxx-bg.info/api/reapi_gamedll/rg_multidmg_clear) | ```
Resets the global multi damage accumulator.
```
  
[rg_multidmg_apply](https://amxx-bg.info/api/reapi_gamedll/rg_multidmg_apply) | ```
Inflicts contents of global multi damage registered on victim.
```
  
[rg_multidmg_add](https://amxx-bg.info/api/reapi_gamedll/rg_multidmg_add) | ```
Adds damage to the accumulator.
```
  
[rg_fire_bullets](https://amxx-bg.info/api/reapi_gamedll/rg_fire_bullets) | ```
Fires bullets from entity.
```
  
[[3] rg_fire_bullets3](https://amxx-bg.info/api/reapi_gamedll/\[3\]%20rg_fire_bullets3) | ```
Fires bullets from player's weapon.
```
  
[rg_round_end](https://amxx-bg.info/api/reapi_gamedll/rg_round_end) | ```
Forces the round to end.
```
  
[rg_update_teamscores](https://amxx-bg.info/api/reapi_gamedll/rg_update_teamscores) | ```
Updates current scores.
```
  
[rg_create_entity](https://amxx-bg.info/api/reapi_gamedll/rg_create_entity) | ```
Creates an entity using Counter-Strike's custom CreateNamedEntity wrapper.
```
  
[rg_find_ent_by_class](https://amxx-bg.info/api/reapi_gamedll/rg_find_ent_by_class) | ```
Finds an entity in the world using Counter-Strike's custom FindEntityByString wrapper.
```
  
[rg_find_ent_by_owner](https://amxx-bg.info/api/reapi_gamedll/rg_find_ent_by_owner) | ```
Finds an entity in the world using Counter-Strike's custom FindEntityByString wrapper, matching by owner.
```
  
[rg_find_weapon_bpack_by_name](https://amxx-bg.info/api/reapi_gamedll/rg_find_weapon_bpack_by_name) | ```
Finds the weapon by name in the player's inventory.
```
  
[rg_has_item_by_name](https://amxx-bg.info/api/reapi_gamedll/rg_has_item_by_name) | ```
Checks if the player has the item.
```
  
[rg_get_weapon_info](https://amxx-bg.info/api/reapi_gamedll/rg_get_weapon_info) | ```
Returns specific information about the weapon.
```
  
[rg_set_weapon_info](https://amxx-bg.info/api/reapi_gamedll/rg_set_weapon_info) | ```
Sets specific weapon info values.
```
  
[rg_remove_items_by_slot](https://amxx-bg.info/api/reapi_gamedll/rg_remove_items_by_slot) | ```
Remove all the player's stuff in a specific slot.
```
  
[rg_drop_items_by_slot](https://amxx-bg.info/api/reapi_gamedll/rg_drop_items_by_slot) | ```
Drop to floor all the player's stuff by specific slot.
```
  
[rg_remove_all_items](https://amxx-bg.info/api/reapi_gamedll/rg_remove_all_items) | ```
Remove all of the player's items.
```
  
[rg_drop_item](https://amxx-bg.info/api/reapi_gamedll/rg_drop_item) | ```
Forces the player to drop the specified item classname.
```
  
[rg_internal_cmd](https://amxx-bg.info/api/reapi_gamedll/rg_internal_cmd) | ```
Executes a client command on the gamedll side.
```
  
[rg_remove_item](https://amxx-bg.info/api/reapi_gamedll/rg_remove_item) | ```
Removes the specified item classname from the player
```
  
[rg_set_user_bpammo](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_bpammo) | ```
Sets the amount of ammo in the client's backpack for a specific weapon.
```
  
[rg_get_user_bpammo](https://amxx-bg.info/api/reapi_gamedll/rg_get_user_bpammo) | ```
Returns the amount of ammo in the client's backpack for a specific weapon.
```
  
[rg_set_user_ammo](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_ammo) | ```
Sets the amount of clip ammo for a specific weapon.
```
  
[rg_get_user_ammo](https://amxx-bg.info/api/reapi_gamedll/rg_get_user_ammo) | ```
Returns the amount of clip ammo for a specific weapon.
```
  
[rg_give_defusekit](https://amxx-bg.info/api/reapi_gamedll/rg_give_defusekit) | ```
Sets the client's defusekit status and allows to set a custom HUD icon and color.
```
  
[rg_get_user_armor](https://amxx-bg.info/api/reapi_gamedll/rg_get_user_armor) | ```
Returns the client's armor value and retrieves the type of armor.
```
  
[rg_set_user_armor](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_armor) | ```
Sets the client's armor value and the type of armor.
```
  
[rg_set_user_team](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_team) | ```
Sets the client's team without killing the player and sets the client's model.
```
  
[rg_set_user_model](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_model) | ```
Sets the client's player model.
```
  
[rg_reset_user_model](https://amxx-bg.info/api/reapi_gamedll/rg_reset_user_model) | ```
Resets the client's model.
```
  
[rg_set_user_footsteps](https://amxx-bg.info/api/reapi_gamedll/rg_set_user_footsteps) | ```
Enable/Disable player's footsteps.
```
  
[rg_get_user_footsteps](https://amxx-bg.info/api/reapi_gamedll/rg_get_user_footsteps) | ```
Get the current footsteps state of the player.
```
  
[rg_transfer_c4](https://amxx-bg.info/api/reapi_gamedll/rg_transfer_c4) | ```
Transfers C4 from one player to another.
```
  
[rg_instant_reload_weapons](https://amxx-bg.info/api/reapi_gamedll/rg_instant_reload_weapons) | ```
Instantly reload client's weapons.
```
  
[rg_set_account_rules](https://amxx-bg.info/api/reapi_gamedll/rg_set_account_rules) | ```
Sets the amount of reward in the game account for all players.
```
  
[rg_get_account_rules](https://amxx-bg.info/api/reapi_gamedll/rg_get_account_rules) | ```
Gets the specified reward rule's money amount.
```
  
[rg_is_bomb_planted](https://amxx-bg.info/api/reapi_gamedll/rg_is_bomb_planted) | ```
Checks if the bomb is planted.
```
  
[rg_join_team](https://amxx-bg.info/api/reapi_gamedll/rg_join_team) | ```
Forces a player to join a team.
```
  
[rg_balance_teams](https://amxx-bg.info/api/reapi_gamedll/rg_balance_teams) | ```
Instantly balances the teams.
```
  
[rg_swap_all_players](https://amxx-bg.info/api/reapi_gamedll/rg_swap_all_players) | ```
Swaps players' teams without reseting frags, deaths and wins.
```
  
[rg_switch_team](https://amxx-bg.info/api/reapi_gamedll/rg_switch_team) | ```
Instantly switches the player to his opposite team.
```
  
[rg_switch_weapon](https://amxx-bg.info/api/reapi_gamedll/rg_switch_weapon) | ```
Forces the player to switch to a specific weapon.
```
  
[rg_get_join_team_priority](https://amxx-bg.info/api/reapi_gamedll/rg_get_join_team_priority) | ```
Gets which team has a higher join priority.
```
  
[rg_is_player_can_takedamage](https://amxx-bg.info/api/reapi_gamedll/rg_is_player_can_takedamage) | ```
Checks whether the player can take damage from the attacker.
```
  
[rg_get_weaponbox_id](https://amxx-bg.info/api/reapi_gamedll/rg_get_weaponbox_id) | ```
Gets WeaponIdType from weaponbox
```
  
[rg_round_respawn](https://amxx-bg.info/api/reapi_gamedll/rg_round_respawn) | ```
Respawn on round for players/bots.
```
  
[rg_reset_maxspeed](https://amxx-bg.info/api/reapi_gamedll/rg_reset_maxspeed) | ```
Resets player's maxspeed.
```
  
[rg_send_bartime](https://amxx-bg.info/api/reapi_gamedll/rg_send_bartime) | ```
Draws a HUD progress bar which fills from 0% to 100% for the time duration in seconds.
```
  
[rg_send_bartime2](https://amxx-bg.info/api/reapi_gamedll/rg_send_bartime2) | ```
Same as BarTime, but StartPercent specifies how much of the bar is (already) filled.
```
  
[rg_send_audio](https://amxx-bg.info/api/reapi_gamedll/rg_send_audio) | ```
Sends the SendAudio message - plays the specified audio.
```
  
[rg_set_iteminfo](https://amxx-bg.info/api/reapi_gamedll/rg_set_iteminfo) | ```
Sets a parameter of the member CSPlayerItem::m_ItemInfo
```
  
[rg_get_iteminfo](https://amxx-bg.info/api/reapi_gamedll/rg_get_iteminfo) | ```
Gets a parameter of the member CSPlayerItem::m_ItemInfo
```
  
[rg_hint_message](https://amxx-bg.info/api/reapi_gamedll/rg_hint_message) | ```
Adds hint message to the queue.
```
  
[rg_restart_round](https://amxx-bg.info/api/reapi_gamedll/rg_restart_round) | ```
Instantly restart round.
```
  
[rg_check_win_conditions](https://amxx-bg.info/api/reapi_gamedll/rg_check_win_conditions) | ```
Instantly check win conditions.
```
  
[rg_initialize_player_counts](https://amxx-bg.info/api/reapi_gamedll/rg_initialize_player_counts) | ```
Instantly initialize player counts.
```
  
[rg_reset_can_hear_player](https://amxx-bg.info/api/reapi_gamedll/rg_reset_can_hear_player) | ```
Reset if player can hear another player.
```
  
[rg_set_can_hear_player](https://amxx-bg.info/api/reapi_gamedll/rg_set_can_hear_player) | ```
Set if player can hear another player
```
  
[rg_get_can_hear_player](https://amxx-bg.info/api/reapi_gamedll/rg_get_can_hear_player) | ```
Get if player can hear another player
```
  
[set_member_s](https://amxx-bg.info/api/reapi_gamedll/set_member_s) | ```
Sets a value to an entity's member.
Safe version, can guarantee that the present member is refers to derived class of the entity.
```
  
[get_member_s](https://amxx-bg.info/api/reapi_gamedll/get_member_s) | ```
Returns a value from an entity's member.
Safe version, can guarantee that the present member is refers to derived class of the entity.
```
  
[rg_fire_buckshots](https://amxx-bg.info/api/reapi_gamedll/rg_fire_buckshots) | ```
Fires buckshots from entity (used at XM1014 and M3 weapons).
```
  
[rg_plant_bomb](https://amxx-bg.info/api/reapi_gamedll/rg_plant_bomb) | ```
Plant a bomb.
```
  
[rg_is_player_can_respawn](https://amxx-bg.info/api/reapi_gamedll/rg_is_player_can_respawn) | ```
Checks whether the player can respawn.
```
  
[rg_spawn_head_gib](https://amxx-bg.info/api/reapi_gamedll/rg_spawn_head_gib) | ```
Spawn a head gib
```
  
[rg_spawn_random_gibs](https://amxx-bg.info/api/reapi_gamedll/rg_spawn_random_gibs) | ```
Spawn random gibs
```
  
[rg_set_global_iteminfo](https://amxx-bg.info/api/reapi_gamedll/rg_set_global_iteminfo) | ```
Sets a parameter of the global CBasePlayerItem::m_ItemInfoArray array
```
  
[rg_get_global_iteminfo](https://amxx-bg.info/api/reapi_gamedll/rg_get_global_iteminfo) | ```
Gets a parameter of the global CBasePlayerItem::m_ItemInfoArray array
```
  
[rg_spawn_grenade](https://amxx-bg.info/api/reapi_gamedll/rg_spawn_grenade) | ```
Spawn a grenade (HEGrenade, Flashbang, SmokeGrenade, or C4)
```
  
[rg_create_weaponbox](https://amxx-bg.info/api/reapi_gamedll/rg_create_weaponbox) | ```
Spawn a weaponbox entity with its properties
```
  
[rg_remove_entity](https://amxx-bg.info/api/reapi_gamedll/rg_remove_entity) | ```
Removes an entity using gamedll's UTIL_Remove function, which sets a frame delay to ensure its removal.
```
  
[rg_decal_trace](https://amxx-bg.info/api/reapi_gamedll/rg_decal_trace) | ```
Creates a Decal in world based on a traceresult.
```
  
[rg_emit_texture_sound](https://amxx-bg.info/api/reapi_gamedll/rg_emit_texture_sound) | ```
Emits a sound based on a traceresult simulating a bullet hit (metal, wood, concrete, etc.).
```
  
[rg_add_ammo_registry](https://amxx-bg.info/api/reapi_gamedll/rg_add_ammo_registry) | ```
Generates an ammo slot in game's logic
```
  
[rg_weapon_deploy](https://amxx-bg.info/api/reapi_gamedll/rg_weapon_deploy) | ```
Deploys a weapon attached to a player using the CBasePlayerWeapon::DefaultDeploy function.
```
  
[rg_weapon_reload](https://amxx-bg.info/api/reapi_gamedll/rg_weapon_reload) | ```
Reloads a weapon or a player's active weapon using the CBasePlayerWeapon::DefaultReload function.
```
  
[rg_weapon_shotgun_reload](https://amxx-bg.info/api/reapi_gamedll/rg_weapon_shotgun_reload) | ```
Forces shotgun reload thinking on a weapon or a player's active weapon using the CBasePlayerWeapon::DefaultShotgunReload function.
```
  
[rg_weapon_send_animation](https://amxx-bg.info/api/reapi_gamedll/rg_weapon_send_animation) | ```
Sends a weapon animation using the CBasePlayerWeapon::SendWeaponAnim function.
```
  
[rg_weapon_kickback](https://amxx-bg.info/api/reapi_gamedll/rg_weapon_kickback) | ```
Emits a "recoil" effect on weapon's player using the CBasePlayerWeapon::KickBack function.
```
  
[rg_switch_best_weapon](https://amxx-bg.info/api/reapi_gamedll/rg_switch_best_weapon) | ```
Switches player current weapon into the best one on its inventory using the CHalfLifeMultiplay::GetNextBestWeapon function.
```
  
[rg_disappear](https://amxx-bg.info/api/reapi_gamedll/rg_disappear) | ```
Disappear a player from the world. Used when VIP reaches escape zone. Basically a silent kill.
```
  
[rg_set_observer_mode](https://amxx-bg.info/api/reapi_gamedll/rg_set_observer_mode) | ```
Sets player current Observer mode.
```
  
[rg_death_notice](https://amxx-bg.info/api/reapi_gamedll/rg_death_notice) | ```
Emits a death notice (logs, DeathMsg event, win conditions check)
```
  
[rg_observer_find_next_player](https://amxx-bg.info/api/reapi_gamedll/rg_observer_find_next_player) | ```
Call origin function CBasePlayer::Observer_FindNextPlayer()
```
  
[rg_player_relationship](https://amxx-bg.info/api/reapi_gamedll/rg_player_relationship) | ```
Checks a player relationship with another reference
```
  
[rg_send_death_message](https://amxx-bg.info/api/reapi_gamedll/rg_send_death_message) | ```
Sends death messages to all players, including info about the killer, victim, weapon used,
extra death flags, death position, assistant, and kill rarity using the CHalfLifeMultiplay::SendDeathMessage function.
```
  

This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.