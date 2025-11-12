# ns_unstick_player
#### Syntax
```
native ns_unstick_player(id, StartDistance=32, MaxAttempts=128);
```

#### Usage
id | ```Player to unstick.```
---|---
StartDistance | ```Distance to start from the player to check for a new location.```
MaxAttempts | ```How many attempts to try to find a new spot before giving up.```
#### Description
```
Attempts to unstick a player.
```

#### Return
```
1 on success, 0 on cannot find a place to move player to,
-1 on invalid state (stunned/webbed), -2 on invalid class (comm/egg)
-3 if the player is dead or a spectator, -4 on invalid player,
-5 if the player is not connected.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).