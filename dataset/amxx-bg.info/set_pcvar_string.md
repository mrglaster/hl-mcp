# set_pcvar_string
#### Syntax
```
native set_pcvar_string(pcvar, const string[]);
```

#### Usage
pcvar | ```Pointer to cvar to retrieve value from```
---|---
string | ```Value to set cvar to```
#### Description
```
Sets a string value to a cvar via direct pointer access.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

