# cs_user_spawn
#### Syntax
```
native cs_user_spawn(player);
```

#### Usage
player | ```Client index```
---|---
#### Description
```
Sets a dead client up for spawning.
```

#### Note
```
This sets the client deadflag and triggers a client think, effectively
making the game respawn the client. Should only be used on dead
clients.
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