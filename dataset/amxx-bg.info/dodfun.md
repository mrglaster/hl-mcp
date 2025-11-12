# Functions in dodfun.inc
Function | Description  
---|---  
[grenade_throw](https://amxx-bg.info/api/dodfun/grenade_throw) | ```
Function is called after grenade throw
```
  
[rocket_shoot](https://amxx-bg.info/api/dodfun/rocket_shoot) | ```
Function is called after a rocket is shot
```
  
[dod_set_stamina](https://amxx-bg.info/api/dodfun/dod_set_stamina) | ```
value is from 0 - 100
```
  
[dod_set_fuse](https://amxx-bg.info/api/dodfun/dod_set_fuse) | ```
types : new or preprimed
```
  
[dod_set_user_class](https://amxx-bg.info/api/dodfun/dod_set_user_class) | ```
Sets player class
```
  
[dod_set_user_team](https://amxx-bg.info/api/dodfun/dod_set_user_team) | ```
Sets player team and random class. Don't work for spectators.
```
  
[dod_get_next_class](https://amxx-bg.info/api/dodfun/dod_get_next_class) | ```
Returns next player class. Usefull is player is using random class
```
  
[dod_is_randomclass](https://amxx-bg.info/api/dodfun/dod_is_randomclass) | ```
Returns 1 if player choose random class
```
  
[dod_get_pl_deaths](https://amxx-bg.info/api/dodfun/dod_get_pl_deaths) | ```
Returns player deaths
```
  
[dod_set_pl_deaths](https://amxx-bg.info/api/dodfun/dod_set_pl_deaths) | ```
Sets player deaths.
Note if you opt to refresh the scoreboard, it
will make the player appear as "DEAD" in the scoreboard.
```
  
[dod_get_user_kills](https://amxx-bg.info/api/dodfun/dod_get_user_kills) | ```
Returns player deaths.
```
  
[dod_set_user_kills](https://amxx-bg.info/api/dodfun/dod_set_user_kills) | ```
Sets player kills.
```
  
[dod_set_user_score](https://amxx-bg.info/api/dodfun/dod_set_user_score) | ```
Sets player score.
```
  
[dod_set_pl_teamname](https://amxx-bg.info/api/dodfun/dod_set_pl_teamname) | ```
Sets new team name for this player
```
  
[dod_get_pl_teamname](https://amxx-bg.info/api/dodfun/dod_get_pl_teamname) | ```
Gets player team name
```
  
[dod_is_deployed](https://amxx-bg.info/api/dodfun/dod_is_deployed) | ```
Returns 1 is player weapon is deployed (bar,mg..)
```
  
[dod_set_user_ammo](https://amxx-bg.info/api/dodfun/dod_set_user_ammo) | ```
Sets the ammo of the specified weapon entity id
```
  
[dod_get_user_ammo](https://amxx-bg.info/api/dodfun/dod_get_user_ammo) | ```
Gets the ammo of the specified weapon entity id
```
  
[controlpoints_init](https://amxx-bg.info/api/dodfun/controlpoints_init) | ```
called after first InitObj
```
  
[objectives_get_num](https://amxx-bg.info/api/dodfun/objectives_get_num) | ```
returns number of objectives
```
  
[objectives_reinit](https://amxx-bg.info/api/dodfun/objectives_reinit) | ```
use this function to update client(s) hud. You need to do this sometimes. Check CP_VALUE comments.
if player is 0 , all clients will get this message
```
  
[objective_get_data](https://amxx-bg.info/api/dodfun/objective_get_data) | ```
use this function to get info about specified control point
```
  
[objective_set_data](https://amxx-bg.info/api/dodfun/objective_set_data) | ```
use this function to change control point's data
```
  
[area_get_data](https://amxx-bg.info/api/dodfun/area_get_data) | ```
use this function to get info about specified control point's area
```
  
[area_set_data](https://amxx-bg.info/api/dodfun/area_set_data) | ```
use this function to change control point's area data
```
  

This code is a part of dodfun.inc. To use this code you should include dodfun.inc as ```#include <dodfun>```


  
  

Warning: This include is compatible only with Day of Defeat and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).