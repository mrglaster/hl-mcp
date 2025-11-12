# ShowSyncHudMsg
#### Syntax
```
native ShowSyncHudMsg(target, syncObj, const fmt[], any:...);
```

#### Usage
target | ```Client index, use 0 to display to all clients```
---|---
syncObj | ```HUD sync object handle```
fmt | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Displays a synchronized HUD message.
```

#### Note
```
This will check that the HUD object has its previous display on the
screen cleared before it proceeds to write another message. It will
only do this in the case of that channel not having been cleared
already.
```

#### Note
```
This uses the display parameters set with set_hudmessage(), ignoring
the selected channel in favor of its own synchronization.
```

#### Note
```
This functions return value behaves differently depending on what is
used as the client index: If 0 is specified, then the function will
return 0 if nothing has been sent (no client connected). If either a
single client is specified, or there is at least one client connected,
the number of printed characters will refer to the message that is sent
last, to the client with the highest index.
```

#### Return
```
Number of printed characters
```

#### Error
```
If a single client is specified and the index is not within
the range of 1 to MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

