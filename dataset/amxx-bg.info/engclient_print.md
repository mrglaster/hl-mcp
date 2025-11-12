# engclient_print
#### Syntax
```
native engclient_print(player, type, const message[], any:...);
```

#### Usage
player | ```Client index, use 0 to display to all clients```
---|---
type | ```Message type, see engprint_* destination constants in amxconst.inc```
message | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a message to the client via the engine.
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


  
  

