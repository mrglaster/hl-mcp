# get_pcvar_flags
#### Syntax
```
native get_pcvar_flags(pcvar);
```

#### Usage
pcvar | ```Pointer to cvar to retrieve flags from```
---|---
#### Description
```
Returns flags of a cvar via direct pointer access.
```

#### Note
```
For a list of possible flags see the FCVAR_* constants in amxconst.inc
```

#### Return
```
1 on success, 0 if cvar pointer is invalid
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

