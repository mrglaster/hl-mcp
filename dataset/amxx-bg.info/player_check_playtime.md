# player_check_playtime
#### Syntax
```
forward player_check_playtime(szPlayers[MAX_PLAYERS], iTotalPlayers);
```

#### Description
```
@description             Multiforward called after the player array was sorted.

@param szPlayers         Array which contains player's indexes.
@param iTotalPlayers     Total of players included in the sorting algorithm.

@note                    Array will be passed in kicking function with the changes made inside this forward.

@return                  Forward ignores return values.
```


This code is a part of advanced_slot_res.inc. To use this code you should include advanced_slot_res.inc as ```#include <advanced_slot_res>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. 