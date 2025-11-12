# remove_cvar_flags
#### Syntax
```
native remove_cvar_flags(const cvar[], flags=-1);
```

#### Usage
cvar | ```Cvar name to remove flags from```
---|---
flags | ```Bitflag sum of flags to remove```
#### Description
```
Removes specified flags from a cvar. The cvar is accessed by name.
```

#### Note
```
Not permitted for the "amx_version", "amxmodx_version", "fun_version"
and "sv_cheats" cvars.
```

#### Note
```
For a list of possible flags see the FCVAR_* constants in amxconst.inc
```

#### Note
```
This function removes the flags using a bitwise-and operation.
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the set_pcvar_flags() function should be used instead.
```

#### Return
```
1 on success, 0 if cvar does not exist or is not permitted
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

