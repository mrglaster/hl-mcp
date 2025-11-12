# get_cvar_pointer
#### Syntax
```
native get_cvar_pointer(const cvar[]);
```

#### Usage
cvar | ```Cvar name to find```
---|---
#### Description
```
Returns the cvar pointer of the specified cvar.
```

#### Note
```
A pointer is also returned by register_cvar() and create_cvar().
Plugins can (and should) retrieve and use pointers for already existing
mod cvars.
```

#### Return
```
Cvar pointer on success, 0 if cvar was not found
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

