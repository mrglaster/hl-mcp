# get_concmd_plid
#### Syntax
```
native get_concmd_plid(cid, flag_mask, id_type);
```

#### Usage
cid | ```Command index```
---|---
flag_mask | ```Only considers commands that can be accessed with the specified privilege flags.```
id_type | ```If set to 0 only server commands will be considered, positive will only consider client commands, otherwise all console commands will be considered.```
#### Description
```
Returns the parent plugin id of a console command.
```

#### Note
```
For a list of possible access flags, see the ADMIN_* constants in
amxconst.inc
```

#### Return
```
Plugin id
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

