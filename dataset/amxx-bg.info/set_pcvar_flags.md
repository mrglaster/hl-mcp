# set_pcvar_flags
#### Syntax
```
native set_pcvar_flags(pcvar, flags);
```

#### Usage
pcvar | ```Pointer to cvar to set flags of```
---|---
flags | ```Bitflag sum of flags to set```
#### Description
```
Sets specified flags to a cvar via direct pointer access.
```

#### Note
```
For a list of possible flags see the FCVAR_* constants in amxconst.inc
```

#### Note
```
This function directly sets the provided bitflag, unlike set_cvar_flags
which adds them using a bitwise OR.
```

#### Return
```
1 on success, 0 if cvar does not exist or is not permitted
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

