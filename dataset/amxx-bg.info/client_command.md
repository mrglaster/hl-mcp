# client_command
#### Syntax
```
forward client_command(id);
```

#### Usage
id | ```Client index```
---|---
#### Description
```
Called when a client attempts to execute a command.
```

#### Note
```
The command and its arguments can be read using the read_arg* set of
functions.
```

#### Return
```
PLUGIN_CONTINUE to let the client execute the command
PLUGIN_HANDLED or higher to stop the command
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

