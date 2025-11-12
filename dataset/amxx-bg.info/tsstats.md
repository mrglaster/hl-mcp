# Functions in tsstats.inc
Function | Description  
---|---  
[get_user_wstats](https://amxx-bg.info/api/tsstats/get_user_wstats) | ```
Gets stats from given weapon index. If wpnindex is 0
then the stats are from all weapons. If weapon has not been used function
returns 0 in other case 1. Fields in stats are:
0 - kills
1 - deaths
2 - headshots
3 - teamkilling
4 - shots
5 - hits
6 - damage
For body hits fields see amxconst.inc.
```
  
[get_user_wrstats](https://amxx-bg.info/api/tsstats/get_user_wrstats) | ```
Gets round stats from given weapon index.
```
  
[get_user_wlstats](https://amxx-bg.info/api/tsstats/get_user_wlstats) | ```
Gets life (from spawn to spawn) stats from given weapon index.
```
  
[get_user_stats](https://amxx-bg.info/api/tsstats/get_user_stats) | ```
Gets overall stats which are stored in file on server
and updated on every respawn or user disconnect.
Function returns the position in stats by diff. kills to deaths.
```
  
[get_user_rstats](https://amxx-bg.info/api/tsstats/get_user_rstats) | ```
Gets round stats of player.
```
  
[get_user_vstats](https://amxx-bg.info/api/tsstats/get_user_vstats) | ```
Gets stats with which user have killed/hurt his victim. If victim is 0
then stats are from all victims. If victim has not been hurt, function
returns 0 in other case 1. User stats are reset on his respawn.
```
  
[get_user_astats](https://amxx-bg.info/api/tsstats/get_user_astats) | ```
Gets stats with which user have been killed/hurt. If killer is 0
then stats are from all attacks. If killer has not hurt user, function
returns 0 in other case 1. User stats are reset on his respawn.
```
  
[reset_user_wstats](https://amxx-bg.info/api/tsstats/reset_user_wstats) | ```
Resets life, weapon, victims and attackers user stats.
```
  
[get_stats](https://amxx-bg.info/api/tsstats/get_stats) | ```
Gets overall stats which stored in stats.dat file in amx folder
and updated on every mapchange or user disconnect.
Function returns next index of stats entry or 0 if no more exists.
```
  
[get_statsnum](https://amxx-bg.info/api/tsstats/get_statsnum) | ```
Returns number of all entries in stats.
```
  

This code is a part of tsstats.inc. To use this code you should include tsstats.inc as ```#include <tsstats>```


  
  

