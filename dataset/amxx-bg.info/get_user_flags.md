# get_user_flags
#### Syntax
```
native get_user_flags(index, id = 0);
```

#### Usage
index | ```Client index, 0 to set flags of server```
---|---
id | ```Flag set id, ranging from 0 to 31```
#### Description
```
Returns the client's admin flags as a bitflag sum.
```

#### Note
```
For a list of possible flags, see the ADMIN_* constants in amxconst.inc
```

#### Note
```
AMXX stores multiple sets of flags internally, but only flag set
0 is actively used. You should not change the value of the second
parameter from the default.
```

#### Return
```
Bitflag sum of client's admin flags
```

#### Error
```
If the index is not within the range of 0 to MaxClients, an
error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

