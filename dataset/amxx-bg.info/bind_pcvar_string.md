# bind_pcvar_string
#### Syntax
```
native bind_pcvar_string(pcvar, any:var[], varlen);
```

#### Usage
pcvar | ```Pointer to cvar```
---|---
var | ```Global array to keep updated```
varlen | ```Maximum length of string array```
#### Description
```
Binds a cvar's string value to a global array. The array will then
always contain the current cvar value as it is automatically kept up to date.
```

#### Note
```
The array *has* to be a global or a static array. Local arrays
created within functions can not be used for technical reasons.
```

#### Note
```
Arrays can not be bound to multiple cvars.
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


  
  

