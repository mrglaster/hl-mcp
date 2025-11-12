# Functions in ns.inc
Function | Description  
---|---  
[client_changeclass](https://amxx-bg.info/api/ns/client_changeclass) | ```
Called whenever the client's class is changed.
```
  
[client_built](https://amxx-bg.info/api/ns/client_built) | ```
Called whenever the client builds a structure.
```
  
[ns_is_combat](https://amxx-bg.info/api/ns/ns_is_combat) | ```
Tell whether or not the map is combat.
```
  
[ns_get_gameplay](https://amxx-bg.info/api/ns/ns_get_gameplay) | ```
Returns the gameplay type for the currently active map.
Refer to ns_const.inc's NSGameplay enum for details.
```
  
[ns_get_user_team](https://amxx-bg.info/api/ns/ns_get_user_team) | ```
Exact syntax as get_user_team, but should be more accurate.
```
  
[ns_popup](https://amxx-bg.info/api/ns/ns_popup) | ```
Send an NS-style popup message.
```
  
[ns_set_player_model](https://amxx-bg.info/api/ns/ns_set_player_model) | ```
Sets a player model.  Omit the second parameter to return to default
```
  
[ns_set_player_skin](https://amxx-bg.info/api/ns/ns_set_player_skin) | ```
Sets a player skin.  Omit the second parameter to return to default
```
  
[ns_set_player_body](https://amxx-bg.info/api/ns/ns_set_player_body) | ```
Sets a player body.  Omit the second parameter to return to default
```
  
[ns_set_speedchange](https://amxx-bg.info/api/ns/ns_set_speedchange) | ```
Set this to modify the player's speed by a certain amount.
```
  
[ns_get_speedchange](https://amxx-bg.info/api/ns/ns_get_speedchange) | ```
Returns a client's current speed modifier.
```
  
[ns_get_maxspeed](https://amxx-bg.info/api/ns/ns_get_maxspeed) | ```
Returns a client's maxspeed before the speed change modifier is factored in.
```
  
[ns_get_mask](https://amxx-bg.info/api/ns/ns_get_mask) | ```
Returns whether or not this mask is set from the entity's iuser4 field.  Use the "mask" enum for reference.
```
  
[ns_set_mask](https://amxx-bg.info/api/ns/ns_set_mask) | ```
Sets or removes the mask from the entity's iuser4 field. Set "value" to 1 to turn the mask on, 0 to turn it off.
```
  
[ns_get_build](https://amxx-bg.info/api/ns/ns_get_build) | ```
Returns built/unbuilt structures.
If:
builtOnly is 1 (default):
Only fully built structures are counted.
builtOnly is 0:
Any structure meeting the classname is counted.

Number is 0 (default):
The total number of matching structures is returned.
Number is any other value:
The index of the #th matching structure is returned.
```
  
[ns_has_weapon](https://amxx-bg.info/api/ns/ns_has_weapon) | ```
Returns if the player has the weapon or not in their pev->weapons field.
set "setweapon" to 0 to turn the bit off, set to 1 to turn it on. Or omit it to just return the value.
```
  
[ns_get_spawn](https://amxx-bg.info/api/ns/ns_get_spawn) | ```
Gets spawn point for specified team (type).
If:
Team is equal to 0:
Ready room spawns are returned.
Team is greater than 0:
Spawns for the team are returned.

Number is equal to 0:
Total number of spawns is returned.
Number is greater than 0:
The location of the specified spawn is returned.
```
  
[ns_get_class](https://amxx-bg.info/api/ns/ns_get_class) | ```
Returns the class of the player.  Look in the classes enum in ns_const.inc for the value's meaning.
```
  
[ns_get_jpfuel](https://amxx-bg.info/api/ns/ns_get_jpfuel) | ```
Gets the player's jetpack fuel reserve.
```
  
[ns_set_jpfuel](https://amxx-bg.info/api/ns/ns_set_jpfuel) | ```
Sets the player's jetpack fuel reserve.
```
  
[ns_add_jpfuel](https://amxx-bg.info/api/ns/ns_add_jpfuel) | ```
Adds to the player's jetpack fuel reserve.
```
  
[ns_get_energy](https://amxx-bg.info/api/ns/ns_get_energy) | ```
Gets the player's energy percentage.
```
  
[ns_set_energy](https://amxx-bg.info/api/ns/ns_set_energy) | ```
Sets the player's energy percentage.
```
  
[ns_add_energy](https://amxx-bg.info/api/ns/ns_add_energy) | ```
Adds to the player's energy percentage.
```
  
[ns_get_res](https://amxx-bg.info/api/ns/ns_get_res) | ```
Returns a player's resources.
```
  
[ns_set_res](https://amxx-bg.info/api/ns/ns_set_res) | ```
Sets a player's resources.
```
  
[ns_add_res](https://amxx-bg.info/api/ns/ns_add_res) | ```
Adds an amount of resources to the player.
```
  
[ns_get_teamres](https://amxx-bg.info/api/ns/ns_get_teamres) | ```
Returns the team's resources.
```
  
[ns_set_teamres](https://amxx-bg.info/api/ns/ns_set_teamres) | ```
Sets the team's resources in the resource pool.
```
  
[ns_add_teamres](https://amxx-bg.info/api/ns/ns_add_teamres) | ```
Adds to the team's resources in the resource pool.
```
  
[ns_get_exp](https://amxx-bg.info/api/ns/ns_get_exp) | ```
Returns the player's experience.
```
  
[ns_set_exp](https://amxx-bg.info/api/ns/ns_set_exp) | ```
Sets the player's experience.
```
  
[ns_add_exp](https://amxx-bg.info/api/ns/ns_add_exp) | ```
Adds to the player's experience.
```
  
[ns_get_points](https://amxx-bg.info/api/ns/ns_get_points) | ```
Gets the player's points spent count in combat.
```
  
[ns_set_points](https://amxx-bg.info/api/ns/ns_set_points) | ```
Sets the player's points spent count in combat.
```
  
[ns_add_points](https://amxx-bg.info/api/ns/ns_add_points) | ```
Adds to the player's points spent count in combat.
```
  
[ns_get_weap_dmg](https://amxx-bg.info/api/ns/ns_get_weap_dmg) | ```
Gets the damage for this weapon.
```
  
[ns_set_weap_dmg](https://amxx-bg.info/api/ns/ns_set_weap_dmg) | ```
Sets the damage for this weapon.
```
  
[ns_get_weap_range](https://amxx-bg.info/api/ns/ns_get_weap_range) | ```
Gets the maximum range for this weapon.
```
  
[ns_set_weap_range](https://amxx-bg.info/api/ns/ns_set_weap_range) | ```
Sets the maximum range for this weapon.
```
  
[ns_get_weap_clip](https://amxx-bg.info/api/ns/ns_get_weap_clip) | ```
Gets the weapon's clip ammo.
```
  
[ns_set_weap_clip](https://amxx-bg.info/api/ns/ns_set_weap_clip) | ```
Sets the weapon's ammo in the clip.
```
  
[ns_get_weap_reserve](https://amxx-bg.info/api/ns/ns_get_weap_reserve) | ```
Gets the player's weapon reserve (backpack ammo) for the specified
type of weapon.
```
  
[ns_set_weap_reserve](https://amxx-bg.info/api/ns/ns_set_weap_reserve) | ```
Sets the player's weapon reserve (backpack ammo) for the specified
type of weapon.
```
  
[ns_get_score](https://amxx-bg.info/api/ns/ns_get_score) | ```
Gets the player's score.
```
  
[ns_set_score](https://amxx-bg.info/api/ns/ns_set_score) | ```
Sets the player's score.
```
  
[ns_add_score](https://amxx-bg.info/api/ns/ns_add_score) | ```
Adds to a player's score
Returns the new score on success
```
  
[ns_get_deaths](https://amxx-bg.info/api/ns/ns_get_deaths) | ```
Gets a player's death count.
```
  
[ns_set_deaths](https://amxx-bg.info/api/ns/ns_set_deaths) | ```
Sets a player's death count.
```
  
[ns_add_deaths](https://amxx-bg.info/api/ns/ns_add_deaths) | ```
Adds to a player's death count
Returns the new death count on success
```
  
[ns_get_struct_owner](https://amxx-bg.info/api/ns/ns_get_struct_owner) | ```
Gets the index of the owner of a structure. -1 for no owner.
```
  
[ns_set_struct_owner](https://amxx-bg.info/api/ns/ns_set_struct_owner) | ```
Sets the index of the owner of a structure. -1 for no owner.
```
  
[ns_get_hive_trait](https://amxx-bg.info/api/ns/ns_get_hive_trait) | ```
Gets the trait type tied to the hive.  Look at the hivetrait enum for the values.
```
  
[ns_set_hive_trait](https://amxx-bg.info/api/ns/ns_set_hive_trait) | ```
Sets the trait type tied to the hive.  Look at the hivetrait enum for the values.
```
  
[ns_set_fov](https://amxx-bg.info/api/ns/ns_set_fov) | ```
Sets the players field of view, set "_fov" to 0.0 (or omit it) to return to normal. FOV change will persist until disconnect unless reset by a plugin
```
  
[ns_give_item](https://amxx-bg.info/api/ns/ns_give_item) | ```
Give the player an item.
```
  
[ns_get_hive_ability](https://amxx-bg.info/api/ns/ns_get_hive_ability) | ```
Returns 1 if a player has the hive ability number.
If ability is 0, it will return the number of active hives.
```
  
[client_changeteam](https://amxx-bg.info/api/ns/client_changeteam) | ```
Triggered whenever a client's pev->team changes.
```
  
[client_spawn](https://amxx-bg.info/api/ns/client_spawn) | ```
Triggered whenever a client's pev->deadflag changes from >0 to 0.
```
  
[ns_takedamage](https://amxx-bg.info/api/ns/ns_takedamage) | ```
Calls NS's private damage routine on the victim entity.
```
  
[ns_unstick_player](https://amxx-bg.info/api/ns/ns_unstick_player) | ```
Attempts to unstick a player.
```
  
[ns_round_in_progress](https://amxx-bg.info/api/ns/ns_round_in_progress) | ```
Whether or not there is a game in progress.
```
  
[round_start](https://amxx-bg.info/api/ns/round_start) | ```
Called at the approximate time that a round is started.
```
  
[round_end](https://amxx-bg.info/api/ns/round_end) | ```
Called immediately when a round ends
```
  
[map_reset](https://amxx-bg.info/api/ns/map_reset) | ```
This function has no description.
```
  
[ns_get_weapon](https://amxx-bg.info/api/ns/ns_get_weapon) | ```
This function has no description.
```
  
[ns_get_locationname](https://amxx-bg.info/api/ns/ns_get_locationname) | ```
Returns the location name of the provided x/y position
(z origin is ignored; can't have location over location)
-
Note that as of NS 3.2 beta 2, on the following maps
the returned string should be passed through ns_lookup_title
to be human readable:
  ns_bast, ns_hera, ns_nothing, ns_tanith,
  ns_nancy, ns_caged, ns_eclipse, ns_veil

Passing the 5th parameter as non zero will auto look up
the title if it exists.
```
  
[ns_lookup_title](https://amxx-bg.info/api/ns/ns_lookup_title) | ```
Looks up a key from titles.txt
Returns -1 if the key is not found
Otherwise it returns the length of the output
```
  
[ns_build_structure](https://amxx-bg.info/api/ns/ns_build_structure) | ```
Forces the structure to fully build
Removes the ghost state from marine structures.
Do not use this on hives! It wont work.
```
  
[ns_recycle](https://amxx-bg.info/api/ns/ns_recycle) | ```
Forces the structure to begin recycling
Passing an index other than a marine structure will
have undefined results!
-
Note: This calls a private NS function!
      Be careful when using this!
```
  
[ns_finish_weldable](https://amxx-bg.info/api/ns/ns_finish_weldable) | ```
Forces the weldable to trigger
Passing an index other than a weldable
will have undefined results!
-
NS renames func_weldable to avhweldable
at map load.
-
Note: This calls a private NS function!
      Be careful when using this!
```
  
[ns_get_weld_time](https://amxx-bg.info/api/ns/ns_get_weld_time) | ```
Gets the total time needed to weld this
func_weldable shut.
Note: NS renames "func_weldable"s to "avhweldable"s
at run time!
```
  
[ns_set_weld_time](https://amxx-bg.info/api/ns/ns_set_weld_time) | ```
Sets the total time needed to weld this
func_weldable shut.
```
  
[ns_add_weld_time](https://amxx-bg.info/api/ns/ns_add_weld_time) | ```
Adds to the weldable's time required to open.
Returns the new required time on success.
Note this native clamps the low value to 0.
```
  
[ns_get_weld_done](https://amxx-bg.info/api/ns/ns_get_weld_done) | ```
Gets the total time this func_weldable
has been welded.
```
  
[ns_set_weld_done](https://amxx-bg.info/api/ns/ns_set_weld_done) | ```
Sets the total time this func_weldable
has been welded.
```
  
[ns_add_weld_done](https://amxx-bg.info/api/ns/ns_add_weld_done) | ```
Adds to the total time this func_weldable
has been welded.  Returns the new value.
Note this native clamps the low value to 0.0
```
  
[ns_get_obs_energy](https://amxx-bg.info/api/ns/ns_get_obs_energy) | ```
Gets/sets/adds to the energy pool of this observatory.
```
  
[ns_set_obs_energy](https://amxx-bg.info/api/ns/ns_set_obs_energy) | ```
This function has no description.
```
  
[ns_add_obs_energy](https://amxx-bg.info/api/ns/ns_add_obs_energy) | ```
This function has no description.
```
  
[ns_remove_upgrade](https://amxx-bg.info/api/ns/ns_remove_upgrade) | ```
Removes an upgrade from the player's bought and active upgrade lists.
This will not refund the points spent on the upgrade, nor will it
immediately strip the upgrade if the player is alive.  Rather, it will
make it so the player no longer receives the upgrade on spawn.
```
  
[ns_create_ps](https://amxx-bg.info/api/ns/ns_create_ps) | ```
Creates a handle to the a particle system to configure
-
Note! this is not a particle system you can pass to
ns_fire_ps()!
```
  
[ns_set_ps_name](https://amxx-bg.info/api/ns/ns_set_ps_name) | ```
Sets the name of the particle system.
-
This is used for things like ns_get_ps_id()
and through calling another particle system
through the "ps_to_gen" field
```
  
[ns_set_ps_sprite](https://amxx-bg.info/api/ns/ns_set_ps_sprite) | ```
Sets the sprite to use for the particle system
-
You do NOT have to precache the sprite, BUT
the sprite must obviously be on the client to
display.
```
  
[ns_spawn_ps](https://amxx-bg.info/api/ns/ns_spawn_ps) | ```
Finalizes the particle system.  Do not configure it after this.
A usable particle system handle is returned.
```
  
[ns_fire_ps](https://amxx-bg.info/api/ns/ns_fire_ps) | ```
Draws a particle system at the given origin (and angles)
Flags are the FEV_* defines from hlsdk_const.inc
Only use handles returned by ns_spawn_ps or ns_get_ps_id here!
```
  
[ns_get_ps_id](https://amxx-bg.info/api/ns/ns_get_ps_id) | ```
Looks up a particle system by name
Returns a usable particle system handle.
```
  
[ns_set_ps_genrate](https://amxx-bg.info/api/ns/ns_set_ps_genrate) | ```
The following are the parameters for configuring the
particle system.  Look through the fgd and NSPSEdit
for details!
```
  
[ns_set_ps_genshape](https://amxx-bg.info/api/ns/ns_set_ps_genshape) | ```
This function has no description.
```
  
[ns_set_ps_genshape_params](https://amxx-bg.info/api/ns/ns_set_ps_genshape_params) | ```
This function has no description.
```
  
[ns_set_ps_spriteframes](https://amxx-bg.info/api/ns/ns_set_ps_spriteframes) | ```
This function has no description.
```
  
[ns_set_ps_numparticles](https://amxx-bg.info/api/ns/ns_set_ps_numparticles) | ```
This function has no description.
```
  
[ns_set_ps_size](https://amxx-bg.info/api/ns/ns_set_ps_size) | ```
This function has no description.
```
  
[ns_set_ps_vel_params](https://amxx-bg.info/api/ns/ns_set_ps_vel_params) | ```
This function has no description.
```
  
[ns_set_ps_vel_shape](https://amxx-bg.info/api/ns/ns_set_ps_vel_shape) | ```
This function has no description.
```
  
[ns_set_ps_sys_life](https://amxx-bg.info/api/ns/ns_set_ps_sys_life) | ```
This function has no description.
```
  
[ns_set_ps_particle_life](https://amxx-bg.info/api/ns/ns_set_ps_particle_life) | ```
This function has no description.
```
  
[ns_set_ps_rendermode](https://amxx-bg.info/api/ns/ns_set_ps_rendermode) | ```
This function has no description.
```
  
[ns_set_ps_to_gen](https://amxx-bg.info/api/ns/ns_set_ps_to_gen) | ```
This function has no description.
```
  
[ns_set_ps_anim_speed](https://amxx-bg.info/api/ns/ns_set_ps_anim_speed) | ```
This function has no description.
```
  
[ns_set_ps_spawn_flags](https://amxx-bg.info/api/ns/ns_set_ps_spawn_flags) | ```
This function has no description.
```
  
[ns_set_ps_base_color](https://amxx-bg.info/api/ns/ns_set_ps_base_color) | ```
This function has no description.
```
  
[ns_set_ps_scale](https://amxx-bg.info/api/ns/ns_set_ps_scale) | ```
This function has no description.
```
  
[ns_set_ps_max_alpha](https://amxx-bg.info/api/ns/ns_set_ps_max_alpha) | ```
This function has no description.
```
  

This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).