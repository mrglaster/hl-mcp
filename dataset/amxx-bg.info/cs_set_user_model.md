# cs_set_user_model
#### Syntax
```
native cs_set_user_model(index, const model[], bool:update_index = false);
```

#### Usage
index | ```Client index```
---|---
model | ```Model name```
update_index | ```If true, the modelindex is updated as well```
#### Description
```
Sets the client's player model.
```

#### Note
```
This is not a one-time set. The CStrike module will remember the
selected model and try to prevent attempts at changing the player
model, or immediately re-apply it if necessary.
```

#### Note
```
Updating modelindex is useful for custom models which don't have
the same structure as the default ones (hitbox, etc..). Model must
be precached before.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, the client is not connected, the provided
model is empty, or if modeindex is updated and the
provided model is not precached, an error will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).