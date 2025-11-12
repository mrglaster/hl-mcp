# get_cvar_flags
#### Syntax
```
native get_cvar_flags(const cvar[]);
```

#### Usage
cvar | ```Cvar name to retrieve flags from```
---|---
#### Description
```
Returns flags of a cvar. The cvar is accessed by name.
```

#### Note
```
For a list of possible flags see the FCVAR_* constants in amxconst.inc
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the otherwise equivalent get_pcvar_flags() function should be used
instead.
```

#### Return
```
Flag value
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

