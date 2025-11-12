# ClearSyncHud
#### Syntax
```
native ClearSyncHud(target, syncObj);
```

#### Usage
target | ```Client index, use 0 to display to all clients```
---|---
syncObj | ```HUD sync object handle```
#### Description
```
Clears the display on a HUD sync object.
```

#### Note
```
This sends an empty message to the previously occupied HUD channel.
It is not quite the same as manually sending an empty message to the
sync object as that would send out two separate messages, one for
clearing the occupied channel and another using a new channel, which
will subsequently not mark the sync object as cleared.
```

#### Return
```
This function has no return value.
```

#### Error
```
If a single client is specified and the index is not within
the range of 1 to MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

