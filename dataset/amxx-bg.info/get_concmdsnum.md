# get_concmdsnum
#### Syntax
```
native get_concmdsnum(flag, id = -1);
```

#### Usage
flag | ```Only considers commands that can be accessed with the specified privilege flags```
---|---
id | ```If set to 0 only server commands will be considered, positive will only consider client commands, otherwise all console commands will be considered```
#### Description
```
Returns number of registered console commands.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
```

#### Return
```
Number of registered console commands
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

