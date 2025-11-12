# get_pcvar_bounds
#### Syntax
```
native bool:get_pcvar_bounds(pcvar, CvarBounds:type, &Float:value);
```

#### Usage
pcvar | ```Pointer to cvar```
---|---
type | ```Type of boundary to retrieve```
value | ```Variable to store the specified boundary to```
#### Description
```
Retrieves the specified value boundary of a cvar.
```

#### Return
```
True if the cvar has a boundary set, false otherwise
```

#### Error
```
If an invalid cvar pointer or boundary type is provided,
an error will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

