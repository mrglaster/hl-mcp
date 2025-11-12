# set_pcvar_bounds
#### Syntax
```
native set_pcvar_bounds(pcvar, CvarBounds:type, bool:set, Float:value = 0.0);
```

#### Usage
pcvar | ```Pointer to cvar```
---|---
type | ```Type of boundary to set```
set | ```If true the cvar boundary will be set, otherwise it will be removed (value is ignored)```
value | ```Floating point value to use as the boundary```
#### Description
```
Sets the specified boundary of a cvar.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid cvar pointer or boundary type is provided, an
error will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

