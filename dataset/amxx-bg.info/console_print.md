# console_print
#### Syntax
```
native console_print(id, const message[], any:...);
```

#### Usage
index | ```Client index, or 0 to print to the server console```
---|---
message | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Sends a message to the console of a client or the server.
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


  
  

