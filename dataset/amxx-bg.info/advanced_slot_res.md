# Functions in advanced_slot_res.inc
Function | Description  
---|---  
[player_kick_pre](https://amxx-bg.info/api/advanced_slot_res/player_kick_pre) | ```
@description             Multiforward called before a player will be kicked to free a player slot.

@param id                Choosen player to be kicked index.
@param szPlayerData      Array which contains data of the reserved client.

@return                  Return SLOT_KICK_YES if you want to not let the plugin kick the player or SLOT_KICK_NO to continue executing.
```
  
[player_kick_post](https://amxx-bg.info/api/advanced_slot_res/player_kick_post) | ```
@description             Multiforward called right before a player will be kicked to free a player slot.

@param id                Choosen player to be kicked index.
@param szPlayerData      Array which contains data of the reserved client.

@return                  Forward ignores return values.
```
  
[player_check_playtime](https://amxx-bg.info/api/advanced_slot_res/player_check_playtime) | ```
@description             Multiforward called after the player array was sorted.

@param szPlayers         Array which contains player's indexes.
@param iTotalPlayers     Total of players included in the sorting algorithm.

@note                    Array will be passed in kicking function with the changes made inside this forward.

@return                  Forward ignores return values.
```
  
[get_players_ex](https://amxx-bg.info/api/advanced_slot_res/get_players_ex) | ```
Support for AmxModX versions lower that 1.8.3
```
  
[get_playersnum_ex](https://amxx-bg.info/api/advanced_slot_res/get_playersnum_ex) | ```
This function has no description.
```
  

This code is a part of advanced_slot_res.inc. To use this code you should include advanced_slot_res.inc as ```#include <advanced_slot_res>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 