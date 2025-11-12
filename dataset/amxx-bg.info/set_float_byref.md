# set_float_byref
#### Syntax
```
native set_float_byref(param, Float:value);
```

#### Usage
param | ```Argument to set, starting from 1```
---|---
value | ```Value to set parameter to```
#### Description
```
Sets the float value of a by-reference parameter to the plugin calling the
native.
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


  
  

