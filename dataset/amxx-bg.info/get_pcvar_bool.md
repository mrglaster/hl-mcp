# get_pcvar_bool
#### Syntax
```
native bool:get_pcvar_bool(pcvar);
```

#### Usage
pcvar | ```Pointer to cvar to retrieve value from```
---|---
#### Description
```
Returns an boolean value from a cvar via direct pointer access.
```

#### Return
```
Cvar value, converted to bool
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

