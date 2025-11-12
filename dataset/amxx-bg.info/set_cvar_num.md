# set_cvar_num
#### Syntax
```
native set_cvar_num(const cvarname[], value);
```

#### Usage
cvar | ```Cvar name to set value of```
---|---
value | ```Value to set cvar to```
#### Description
```
Sets a cvar to a given integer value. The cvar is accessed by name.
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the otherwise equivalent set_pcvar_num() function should be used
instead.
```

#### Return
```
This function has no return value.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

