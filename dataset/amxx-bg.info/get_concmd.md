# get_concmd
#### Syntax
```
native get_concmd(index, cmd[], len1, &flags, info[], len2, flag, id = -1, &bool:info_ml = false);
```

#### Usage
index | ```Command index```
---|---
command | ```Buffer to copy command name to```
len1 | ```Maximum name buffer size```
flags | ```Variable to store privilege flags to```
info | ```Buffer to copy command description to```
len2 | ```Maximum description buffer size```
flag | ```Only considers commands that can be accessed with the specified privilege flags```
id | ```If set to 0 only server commands will be considered, positive will only consider client commands, otherwise all console commands will be considered```
info_ml | ```Variable to store whether the parameter "info" is a multilingual key```
#### Description
```
Retrieves information about a console command.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
```

#### Return
```
1 on success, 0 if command was not found
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

