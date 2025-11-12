# cs_get_user_team
#### Syntax
```
native CsTeams:cs_get_user_team(index, &any:model = CS_DONTCHANGE);
```

#### Usage
index | ```Client index```
---|---
model | ```Optional variable to store model id in```
#### Description
```
Returns the client's team and optionally the model id.
```

#### Note
```
For a list of valid team ids see the CsTeams enum, and for a list of
valid internal model ids see the CsInternalModel enum.
```

#### Return
```
Team id
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).