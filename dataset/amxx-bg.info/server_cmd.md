# server_cmd
#### Syntax
```
native server_cmd(const command[], any:...);
```

#### Usage
command | ```Formatting rules```
---|---
... | ```Variable number of formatting parameters```
#### Description
```
Queues a command to be executed from the server console.
```

#### Note
```
Warning: This is a potential source of command injection. Do not feed
client-controlled input (including client names) to this function
without sanitizing it first.
```

#### Note
```
The queued commands will be executed by the engine on the next frame.
If you require them to be executed immediately, see server_exec()
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

