# bind_pcvar_float
#### Syntax
```
native bind_pcvar_float(pcvar, &Float:var);
```

#### Usage
pcvar | ```Pointer to cvar```
---|---
var | ```Global variable to keep updated```
#### Description
```
Binds a cvar's float value to a global variable. The variable will then
always contain the current cvar value as it is automatically kept up to date.
```

#### Note
```
The variable *has* to be a global or a static variable. Local variables
created within functions can not be used for technical reasons.
```

#### Note
```
Variables can not be bound to multiple cvars.
```

#### Return
```
This function has no return value.
```

#### Error
```
If an invalid cvar pointer or variable is provided, an error
will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

