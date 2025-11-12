# client_cmd
#### Syntax
```
native client_cmd(index, const command[], any:...);
```

#### Usage
index | ```Client index, use 0 to execute on all clients```
---|---
command | ```Formatting rules```
... | ```Variable number of formatting parameters```
#### Description
```
Executes a command on the client.
```

#### Note
```
Executing malicious commands on the client ("slowhacking") is frowned
upon.
```

#### Note
```
Valve has introduced a command filter to Counter-Strike 1.6. It is not
possible to execute many commands if the client has opted in to this.
```

#### Return
```
Length of formatted command string
```

#### Error
```
If a single client is specified and the index is not within
the range of 1 to MaxClients, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

