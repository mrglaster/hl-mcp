# amxclient_cmd
#### Syntax
```
native amxclient_cmd(index, const command[], const arg1[] = "", const arg2[] = "");
```

#### Usage
index | ```Client index, use 0 to execute from all clients```
---|---
command | ```Client command to execute on```
arg1 | ```Optional command arguments```
arg2 | ```Optional command arguments```
#### Description
```
Execute a command from the client without actually sending it to the client's
DLL. This triggers plugin command hooks.
```

#### Note
```
This emulates a client command on the server side, and is an excellent
tool to force a client to do certain actions related to the game.
```

#### Note
```
The command has to stand alone in the command parameter, only add
arguments using the designated parameters.
```

#### Note
```
Commands emulated using this function will trigger other plugin's
command hooks. For an alternative that doesn't, see engclient_cmd()
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


  
  

