# Functions in csx.inc
Function | Description  
---|---  
[client_damage](https://amxx-bg.info/api/csx/client_damage) | ```
Called after a client attacks another client.
```
  
[client_death](https://amxx-bg.info/api/csx/client_death) | ```
Called after a client death.
```
  
[grenade_throw](https://amxx-bg.info/api/csx/grenade_throw) | ```
Called after a grenade was thrown.
```
  
[bomb_planting](https://amxx-bg.info/api/csx/bomb_planting) | ```
Called after a bomb plant attempt has started.
```
  
[bomb_planted](https://amxx-bg.info/api/csx/bomb_planted) | ```
Called after a bomb plant has finished.
```
  
[bomb_explode](https://amxx-bg.info/api/csx/bomb_explode) | ```
Called when the bomb exploded.
```
  
[bomb_defusing](https://amxx-bg.info/api/csx/bomb_defusing) | ```
Called after a bomb defuse attempt has started.
```
  
[bomb_defused](https://amxx-bg.info/api/csx/bomb_defused) | ```
Called after a bomb defuse has finished.
```
  
[custom_weapon_add](https://amxx-bg.info/api/csx/custom_weapon_add) | ```
Adds a custom weapon to the stats system.
```
  
[custom_weapon_dmg](https://amxx-bg.info/api/csx/custom_weapon_dmg) | ```
Triggers a damage event on a custom weapon, adding it to the internal stats.
```
  
[custom_weapon_shot](https://amxx-bg.info/api/csx/custom_weapon_shot) | ```
Adds a shot event on a custom weapon to the internal stats.
```
  
[xmod_is_melee_wpn](https://amxx-bg.info/api/csx/xmod_is_melee_wpn) | ```
Returns if the weapon is considered a melee weapon.
```
  
[xmod_get_wpnname](https://amxx-bg.info/api/csx/xmod_get_wpnname) | ```
Retrieves the full weapon name of a weapon id.
```
  
[xmod_get_wpnlogname](https://amxx-bg.info/api/csx/xmod_get_wpnlogname) | ```
Retrieves the weapon log name of a weapon id.
```
  
[xmod_get_maxweapons](https://amxx-bg.info/api/csx/xmod_get_maxweapons) | ```
Returns the maximum amount of weapons that the stats system supports.
```
  
[xmod_get_stats_size](https://amxx-bg.info/api/csx/xmod_get_stats_size) | ```
Returns the number of stats tracked by the stats system.
```
  
[get_map_objectives](https://amxx-bg.info/api/csx/get_map_objectives) | ```
Returns the current map's objectives as a bitflag value.
```
  

This code is a part of csx.inc. To use this code you should include csx.inc as ```#include <csx>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).