# cs_set_user_vip
#### Syntax
```
native cs_set_user_vip(index, vip = 1, model = 1, scoreboard = 1);
```

#### Usage
index | ```Client index```
---|---
vip | ```If nonzero the client will be made a VIP, otherwise the VIP status will be removed```
model | ```If nonzero the client's model will be changed to the VIP model, otherwise a random CT model will be selected```
scoreboard | ```If nonzero the scoreboard will be updated to reflect the new VIP status```
#### Description
```
Sets the client's VIP status and displayed model and scoreboard flag.
```

#### Note
```
This is mostly useful for removing VIP status so the client can change
teams and/or buy items properly. It does not alter gameplay, the player
that is selected as VIP at the start of a round will retain the
internal VIP status and remain the primary objective for the game mode.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).