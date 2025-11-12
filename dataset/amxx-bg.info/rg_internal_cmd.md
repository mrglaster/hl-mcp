# rg_internal_cmd
#### Syntax
```
native rg_internal_cmd(const index, const cmd[], const arg[] = "");
```

#### Usage
index | ```Client index```
---|---
command | ```Client command to execute```
arg | ```Optional command arguments```
#### Description
```
Executes a client command on the gamedll side.
```

#### Return
```
1 on success, 0 otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.