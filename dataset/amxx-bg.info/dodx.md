# Functions in dodx.inc
Function | Description  
---|---  
[register_statsfwd](https://amxx-bg.info/api/dodx/register_statsfwd) | ```
Use this function to register forwards
```
  
[client_damage](https://amxx-bg.info/api/dodx/client_damage) | ```
Function is called after player to player attacks ,
if players were damaged by teammate TA is set to 1
```
  
[client_death](https://amxx-bg.info/api/dodx/client_death) | ```
Function is called after player death ,
if player was killed by teammate TK is set to 1
```
  
[client_score](https://amxx-bg.info/api/dodx/client_score) | ```
Function is called if player scored
```
  
[dod_client_changeteam](https://amxx-bg.info/api/dodx/dod_client_changeteam) | ```
This Forward is called when a player changes team
```
  
[dod_client_changeclass](https://amxx-bg.info/api/dodx/dod_client_changeclass) | ```
This Forward is called if a player changes class, but just after spawn
```
  
[dod_client_spawn](https://amxx-bg.info/api/dodx/dod_client_spawn) | ```
This Forward is called when a player spawns
```
  
[dod_client_scope](https://amxx-bg.info/api/dodx/dod_client_scope) | ```
This will be called whenever a player scopes or unscopes
value = 1 scope up
value = 0 scope down
```
  
[dod_client_weaponpickup](https://amxx-bg.info/api/dodx/dod_client_weaponpickup) | ```
This will be called whenever a player drops a weapon
weapon is weapon dropped or picked up
value = 1 picked up
value = 0 dropped
```
  
[dod_client_prone](https://amxx-bg.info/api/dodx/dod_client_prone) | ```
Called whenever the the player goes to or comes from prone position
value = 1 going down
value = 0 getting up
```
  
[dod_client_weaponswitch](https://amxx-bg.info/api/dodx/dod_client_weaponswitch) | ```
This will be called whenever a player switches a weapon
```
  
[dod_grenade_explosion](https://amxx-bg.info/api/dodx/dod_grenade_explosion) | ```
Forward for when a grenade explodes and its location
```
  
[dod_rocket_explosion](https://amxx-bg.info/api/dodx/dod_rocket_explosion) | ```
Forward for when a rocket explodes and its location
```
  
[dod_client_objectpickup](https://amxx-bg.info/api/dodx/dod_client_objectpickup) | ```
Forward for when a player picks up a object
```
  
[dod_client_stamina](https://amxx-bg.info/api/dodx/dod_client_stamina) | ```
Forward for when a users stamina decreases
```
  
[dod_weapon_type](https://amxx-bg.info/api/dodx/dod_weapon_type) | ```
We want to get just the weapon of whichever type that the player is on him
Use DODWT_* in dodconst.inc for type
```
  
[dod_set_weaponlist](https://amxx-bg.info/api/dodx/dod_set_weaponlist) | ```
This native will change the position of a weapon within the users slots and its ammo ammount
```
  
[dod_set_model](https://amxx-bg.info/api/dodx/dod_set_model) | ```
Sets the model for a player
```
  
[dod_set_body_number](https://amxx-bg.info/api/dodx/dod_set_body_number) | ```
Sets the model for a player
```
  
[dod_clear_model](https://amxx-bg.info/api/dodx/dod_clear_model) | ```
Un-Sets the model for a player
```
  
[custom_weapon_add](https://amxx-bg.info/api/dodx/custom_weapon_add) | ```
function will return index of new weapon
```
  
[custom_weapon_dmg](https://amxx-bg.info/api/dodx/custom_weapon_dmg) | ```
Function will pass damage done by this custom weapon to stats module and other plugins
```
  
[custom_weapon_shot](https://amxx-bg.info/api/dodx/custom_weapon_shot) | ```
Function will pass info about custom weapon shot to stats module
```
  
[xmod_is_melee_wpn](https://amxx-bg.info/api/dodx/xmod_is_melee_wpn) | ```
function will return 1 if true
```
  
[xmod_get_wpnname](https://amxx-bg.info/api/dodx/xmod_get_wpnname) | ```
Returns weapon name.
```
  
[xmod_get_wpnlogname](https://amxx-bg.info/api/dodx/xmod_get_wpnlogname) | ```
Returns weapon logname.
```
  
[xmod_get_maxweapons](https://amxx-bg.info/api/dodx/xmod_get_maxweapons) | ```
Returns weapons array size
```
  
[xmod_get_stats_size](https://amxx-bg.info/api/dodx/xmod_get_stats_size) | ```
Returns stats array size ex. 8 in TS , 9 in DoD
```
  
[xmod_is_custom_wpn](https://amxx-bg.info/api/dodx/xmod_is_custom_wpn) | ```
Returns 1 if true
```
  
[dod_wpnlog_to_name](https://amxx-bg.info/api/dodx/dod_wpnlog_to_name) | ```
weapon logname to weapon name convertion
```
  
[dod_wpnlog_to_id](https://amxx-bg.info/api/dodx/dod_wpnlog_to_id) | ```
weapon logname to weapon index convertion
```
  
[dod_get_map_info](https://amxx-bg.info/api/dodx/dod_get_map_info) | ```
This function has no description.
```
  
[dod_get_user_weapon](https://amxx-bg.info/api/dodx/dod_get_user_weapon) | ```
Returns id of currently carried weapon. Gets also
ammount of ammo in clip and backpack.
```
  
[dod_get_team_score](https://amxx-bg.info/api/dodx/dod_get_team_score) | ```
Returns team score
```
  
[dod_get_user_class](https://amxx-bg.info/api/dodx/dod_get_user_class) | ```
Returns player class id
```
  
[dod_get_user_score](https://amxx-bg.info/api/dodx/dod_get_user_score) | ```
Returns player score
```
  
[dod_get_pronestate](https://amxx-bg.info/api/dodx/dod_get_pronestate) | ```
values are: 0-no prone, 1-prone, 2-prone + w_deploy
```
  
[dod_user_kill](https://amxx-bg.info/api/dodx/dod_user_kill) | ```
It is not as safe as original but player deaths will not be increased
```
  

This code is a part of dodx.inc. To use this code you should include dodx.inc as ```#include <dodx>```


  
  

Warning: This include is compatible only with Day of Defeat and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).