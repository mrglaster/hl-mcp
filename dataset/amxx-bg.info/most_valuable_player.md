# Functions in most_valuable_player.inc
Function | Description  
---|---  
[mvp_scenario](https://amxx-bg.info/api/most_valuable_player/mvp_scenario) | ```
@description         Multiforward called when a round end.

@param scenario      Scenario index. See WinScenario enum

@return              Scenario index.
```
  
[get_user_mvp_kills](https://amxx-bg.info/api/most_valuable_player/get_user_mvp_kills) | ```
@description         Returns player's MVP kills.

@param id            Player index.

@return              Amount of kills. -1 on error.
```
  
[get_user_mvp_topkiller](https://amxx-bg.info/api/most_valuable_player/get_user_mvp_topkiller) | ```
@description         Returns top killer's index.

@param id            Top killer index.

@return              Top killer's index. -1 on error.
```
  
[get_user_mvp_damage](https://amxx-bg.info/api/most_valuable_player/get_user_mvp_damage) | ```
@description         Returns player's MVP damage.

@param id            Player index.

@return              Player index. -1 on error.
```
  
[get_user_mvp_hs_damage](https://amxx-bg.info/api/most_valuable_player/get_user_mvp_hs_damage) | ```
@description         Returns player's MVP damage made with headshot.

@param id            Player index.

@return              Player index. -1 on error.
```
  
[get_user_mvps](https://amxx-bg.info/api/most_valuable_player/get_user_mvps) | ```
@description         Returns Player's MVPs.

@param id            Player index.

@return              Player index. -1 on error.
```
  
[get_user_mvp_track](https://amxx-bg.info/api/most_valuable_player/get_user_mvp_track) | ```
@description         Returns Player's selected Track.

@param id            Player index.

@return              Player index. -1 on error.
```
  
[get_mvp_track_info](https://amxx-bg.info/api/most_valuable_player/get_mvp_track_info) | ```
@description         Returns informations about certain Track.

@param iTrackID      Track index.
@param szName[]      Variable to store track name.
@param iNameLen      Track name lenght.
@param szPath[]      Variable to store track's path.
@param iPathLen      Track path lenght.

@return              1 on success. -1 if TrackID is invalid or on error.
```
  
[get_mvp_index](https://amxx-bg.info/api/most_valuable_player/get_mvp_index) | ```
@description         Returns MVP of the round index.

@noparam

@return              MVPlayer index. -1 if there is no MVP.
```
  

This code is a part of most_valuable_player.inc. To use this code you should include most_valuable_player.inc as ```#include <most_valuable_player>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.