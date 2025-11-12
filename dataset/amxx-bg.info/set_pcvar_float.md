# set_pcvar_float
#### Syntax
```
native set_pcvar_float(pcvar, Float:num);
```

#### Usage
pcvar | ```Pointer to cvar to set value of```
---|---
num | ```Value to set cvar to```
#### Description
```
Sets a float value to a cvar via direct pointer access.
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


  
  

