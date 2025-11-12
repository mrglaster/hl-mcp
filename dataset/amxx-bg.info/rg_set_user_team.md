# rg_set_user_team
#### Syntax
```
native rg_set_user_team(const index, {TeamName,_}:team, {ModelName,_}:model = MODEL_AUTO, const bool:send_teaminfo = true, const bool:check_win_conditions = false);
```

#### Usage
index | ```Client index```
---|---
team | ```Team id```
model | ```Internal model, use MODEL_AUTO for a random appearance or MODEL_UNASSIGNED to not update it```
send_teaminfo | ```If true, a TeamInfo message will be sent```
check_win_conditions | ```If true, a CheckWinConditions will be call```
#### Description
```
Sets the client's team without killing the player and sets the client's model.
```

#### Note
```
To obtain a TeamName use the following:
new TeamName:team = get_member(id, m_iTeam);
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.