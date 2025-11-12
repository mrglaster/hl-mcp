# cs_set_user_team
#### Syntax
```
native cs_set_user_team(index, any:team, any:model = CS_DONTCHANGE, bool:send_teaminfo = true);
```

#### Usage
index | ```Client index```
---|---
team | ```Team id```
model | ```Internal model id, if CS_DONTCHANGE the game will choose the model or if CS_NORESET the game will not update it.```
send_teaminfo | ```If true, a TeamInfo message will be sent```
#### Description
```
Sets the client's team without killing the player, and sets the client model.
```

#### Note
```
For a list of valid team ids see the CsTeams enum, and for a list of
valid internal model ids see the CsInternalModel enum.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).