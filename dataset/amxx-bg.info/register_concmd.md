# register_concmd
#### Syntax
```
native register_concmd(const cmd[], const function[], flags = -1, const info[] = "", FlagManager = -1, bool:info_ml = false);
```

#### Usage
client_cmd | ```Command to register```
---|---
function | ```Callback function```
flags | ```Admin privilege flags required```
info | ```Command description```
FlagManager | ```0 opts out of flag manager, 1 opts in, -1 selects automatically```
info_ml | ```If true, the parameter "info" will be looked up as multilingual key```
#### Description
```
Registers a callback to be called when the client or server executes a
command from the console.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
```

#### Note
```
Opting in to FlagManager enables the admin privileges to be overwritten
by the end user via the cmdaccess.ini config file.
```

#### Note
```
Automatic detection for FlagManager will only include a command if it
has required privileges (flags is not -1) and it is not a command
starting with "say".
```

#### Return
```
Command id, 0 on failure
```

#### Error
```
If an invalid callback function is specified, an error
will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

