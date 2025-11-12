# cs_get_user_tked
#### Syntax
```
native cs_get_user_tked(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if the client has committed a team kill in the current round.
```

#### Note
```
If this is set to 1 the client will be punished at the start of the
next round depending on the value of the mp_tkpunish cvar. The team
kill status is then reset.
```

#### Return
```
1 if the client has committed a team kill, 0 otherwise
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).