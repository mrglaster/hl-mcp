# get_pcvar_num
#### Syntax
```
native get_pcvar_num(pcvar);
```

#### Usage
pcvar | ```Pointer to cvar to retrieve value from```
---|---
#### Description
```
Returns an integer value from a cvar via direct pointer access.
```

#### Return
```
Cvar value, converted to int
```

#### Error
```
If an invalid cvar pointer is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

