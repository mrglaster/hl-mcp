# register_srvcmd
#### Syntax
```
native register_srvcmd(const server_cmd[], const function[], flags = -1, const info[] = "", bool:info_ml = false);
```

#### Usage
client_cmd | ```Command to register```
---|---
function | ```Callback function```
flags | ```Admin privilege flags required```
info | ```Command description```
info_ml | ```If true, the parameter "info" will be looked up as multilingual key```
#### Description
```
Registers a callback to be called when the server executes a command from the
console.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
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


  
  

