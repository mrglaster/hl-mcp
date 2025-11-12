# CS_InternalCommand
#### Syntax
```
forward CS_InternalCommand(id, const cmd[]);
```

#### Usage
id | ```Client index```
---|---
cmd | ```Command string```
#### Description
```
Called when CS internally fires a command to a player.
```

#### Note
```
This is most notably used by the rebuy/autobuy functionality,
Condition Zero also uses this to pass commands to bots internally.
```

#### Return
```
PLUGIN_CONTINUE to let the command continue
PLUGIN_HANDLED to block the command
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).