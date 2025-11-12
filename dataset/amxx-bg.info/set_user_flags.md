# set_user_flags
#### Syntax
```
native set_user_flags(index, flags = -1, id = 0);
```

#### Usage
index | ```Client index, 0 to set flags of server```
---|---
flags | ```Admin flags```
id | ```Flag set id, ranging from 0 to 31```
#### Description
```
Sets the specified admin flags to a client.
```

#### Note
```
For a list of possible flags, see the ADMIN_* constants in amxconst.inc
```

#### Note
```
This function just adds the flags using a bitwise-or operation. After it
has run, the flags may not exactly equal the specified bitflag sum.
```

#### Note
```
AMXX stores multiple sets of flags internally, but only flag set
0 is actively used. You should not change the value of the third
parameter from the default.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the index is not within the range of 0 to MaxClients, an
error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

