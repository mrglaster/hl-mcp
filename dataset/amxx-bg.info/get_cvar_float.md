# get_cvar_float
#### Syntax
```
native Float:get_cvar_float(const cvarname[]);
```

#### Usage
cvarname | ```Cvar name to retrieve value from```
---|---
#### Description
```
Returns a floating value from a cvar. The cvar is accessed by name.
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the otherwise equivalent get_pcvar_float() function should be used
instead.
```

#### Return
```
Cvar value, converted to float
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

