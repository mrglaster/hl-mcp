# Functions in csstats.inc
Function | Description  
---|---  
[get_user_wstats](https://amxx-bg.info/api/csstats/get_user_wstats) | ```
Retrieves the client's current weapon statistics.
```
  
[get_user_wrstats](https://amxx-bg.info/api/csstats/get_user_wrstats) | ```
Retrieves the client's weapon statistics from the current round.
```
  
[get_user_stats](https://amxx-bg.info/api/csstats/get_user_stats) | ```
Retrieves the client's weapon statistics from the permanent storage on the
server.
```
  
[get_user_rstats](https://amxx-bg.info/api/csstats/get_user_rstats) | ```
Retrieves the client's statistics from the current round.
```
  
[get_user_vstats](https://amxx-bg.info/api/csstats/get_user_vstats) | ```
Retrieves the client's statistics inflicted upon another client from the
current round.
```
  
[get_user_astats](https://amxx-bg.info/api/csstats/get_user_astats) | ```
Retrieves the client's statistics received from another client from the
current round.
```
  
[reset_user_wstats](https://amxx-bg.info/api/csstats/reset_user_wstats) | ```
Resets the current round weapon, attacker and victim statistics.
```
  
[get_stats](https://amxx-bg.info/api/csstats/get_stats) | ```
Retrieves statistics from the permanent storage on the server via iterative,
incremental access.
```
  
[get_statsnum](https://amxx-bg.info/api/csstats/get_statsnum) | ```
Returns the number of all entries in the permanent statistics storage.
```
  
[get_user_stats2](https://amxx-bg.info/api/csstats/get_user_stats2) | ```
Retrieves the client's objective statistics from the permanent storage.
```
  
[get_stats2](https://amxx-bg.info/api/csstats/get_stats2) | ```
Retrieves objective statistics from the permanent storage on the server via
iterative, incremental access.
```
  

This code is a part of csstats.inc. To use this code you should include csstats.inc as ```#include <csstats>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).