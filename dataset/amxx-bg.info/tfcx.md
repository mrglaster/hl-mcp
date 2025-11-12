# Functions in tfcx.inc
Function | Description  
---|---  
[register_statsfwd](https://amxx-bg.info/api/tfcx/register_statsfwd) | ```
Use this function to register forwards
```
  
[client_damage](https://amxx-bg.info/api/tfcx/client_damage) | ```
Function is called after player to player attacks ,
if players were damaged by teammate TA is set to 1
```
  
[client_death](https://amxx-bg.info/api/tfcx/client_death) | ```
Function is called after player death ,
if player was killed by teammate TK is set to 1
```
  
[custom_weapon_add](https://amxx-bg.info/api/tfcx/custom_weapon_add) | ```
function will return index of new weapon
```
  
[custom_weapon_dmg](https://amxx-bg.info/api/tfcx/custom_weapon_dmg) | ```
Function will pass damage done by this custom weapon to stats module and other plugins
```
  
[custom_weapon_shot](https://amxx-bg.info/api/tfcx/custom_weapon_shot) | ```
Function will pass info about custom weapon shot to stats module
```
  
[xmod_is_melee_wpn](https://amxx-bg.info/api/tfcx/xmod_is_melee_wpn) | ```
function will return 1 if true
```
  
[xmod_get_wpnname](https://amxx-bg.info/api/tfcx/xmod_get_wpnname) | ```
Returns weapon name.
```
  
[xmod_get_wpnlogname](https://amxx-bg.info/api/tfcx/xmod_get_wpnlogname) | ```
Returns weapon logname.
```
  
[xmod_get_maxweapons](https://amxx-bg.info/api/tfcx/xmod_get_maxweapons) | ```
Returns weapons array size
```
  
[xmod_get_stats_size](https://amxx-bg.info/api/tfcx/xmod_get_stats_size) | ```
Returns stats array size ex. 8 in TS , 9 in DoD
```
  
[xmod_is_custom_wpn](https://amxx-bg.info/api/tfcx/xmod_is_custom_wpn) | ```
Returns 1 if true
```
  
[tfc_isgrenade](https://amxx-bg.info/api/tfcx/tfc_isgrenade) | ```
*********** Shared Natives End *******************************
```
  
[tfc_userkill](https://amxx-bg.info/api/tfcx/tfc_userkill) | ```
This function has no description.
```
  
[tfc_setpddata](https://amxx-bg.info/api/tfcx/tfc_setpddata) | ```
Use this function to set private data offsets if needed
Default offsets:
timer: 932
sentrygun: 83
from AssKicR
shells: 53
bullets: 55
cells: 57
rockets: 59
nade1: 14
nade2: 15
```
  
[tfc_setmodel](https://amxx-bg.info/api/tfcx/tfc_setmodel) | ```
******************************************************************
```
  
[tfc_clearmodel](https://amxx-bg.info/api/tfcx/tfc_clearmodel) | ```
This function has no description.
```
  
[tfc_getbammo](https://amxx-bg.info/api/tfcx/tfc_getbammo) | ```
Ammo Types in tfcconst.inc
```
  
[tfc_setbammo](https://amxx-bg.info/api/tfcx/tfc_setbammo) | ```
Set amount of ammo in backpack on a user for a specific weapon
```
  
[tfc_getweaponbammo](https://amxx-bg.info/api/tfcx/tfc_getweaponbammo) | ```
Weapons list in tfcconst.inc
```
  
[tfc_setweaponbammo](https://amxx-bg.info/api/tfcx/tfc_setweaponbammo) | ```
Sets amount of ammo in weapon's clip (backpack)
```
  
[tfc_getweaponammo](https://amxx-bg.info/api/tfcx/tfc_getweaponammo) | ```
Index must be weapon's entity index
```
  
[tfc_setweaponammo](https://amxx-bg.info/api/tfcx/tfc_setweaponammo) | ```
Index must be weapon's entity index
```
  
[tfc_get_user_goalitem](https://amxx-bg.info/api/tfcx/tfc_get_user_goalitem) | ```
Returns 1 if user is carrying a goal item such as a flag or a keycard, else 0.
Team is by reference parameter that will be set to owning team(s) of the goal item.
Use the TFC_GOALITEM_* constants to determine the owning team.
```
  
[tfc_is_user_feigning](https://amxx-bg.info/api/tfcx/tfc_is_user_feigning) | ```
Returns 1 if the player is a spy and is currently feigning death
```
  
[tfc_is_team_ally](https://amxx-bg.info/api/tfcx/tfc_is_team_ally) | ```
Returns 1 if the two teams are allies, 0 otherwise
Note: Team must be 1->4
      Team 0 will always return 0
      Any other team will result in an error
```
  

This code is a part of tfcx.inc. To use this code you should include tfcx.inc as ```#include <tfcx>```


  
  

Warning: This include is compatible only with Team Fortress: Classic and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).