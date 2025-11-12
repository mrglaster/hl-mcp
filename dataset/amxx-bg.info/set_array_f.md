# set_array_f
#### Syntax
```
native set_array_f(param, const Float:source[], size);
```

#### Usage
param | ```Argument to set, starting from 1```
---|---
source | ```Buffer to copy array from```
maxlen | ```Size of buffer```
#### Description
```
Copies a float array to the plugin calling the native.
```

#### Return
```
This function has no return value.
```

#### Error
```
If used outside of a native callback, or the native was
created with style 1, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

