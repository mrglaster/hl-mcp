# get_cvar_string
#### Syntax
```
native get_cvar_string(const cvarname[], output[], iLen);
```

#### Usage
cvar | ```Cvar name to retrieve value from```
---|---
output | ```Buffer to copy cvar value to```
iLen | ```Maximum size of the buffer```
#### Description
```
Gets a string value from a cvar. The cvar is accessed by name.
```

#### Note
```
Accessing a Cvar by name is slower than direct pointer access, which is
why the otherwise equivalent get_pcvar_string() function should be used
instead.
```

#### Return
```
Number of cells written to buffer.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

