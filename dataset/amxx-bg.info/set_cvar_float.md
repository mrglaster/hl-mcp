# set_cvar_float
#### Syntax
```
native set_cvar_float(const cvar[], Float:value);
```

#### Usage
cvar | ```Cvar name to set value of```
---|---
value | ```Value to set cvar to```
#### Description
```
Sets a cvar to a given float value. The cvar is accessed by name.
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the otherwise equivalent set_pcvar_float() function should be used
instead.
```

#### Return
```
This function has no return value.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

