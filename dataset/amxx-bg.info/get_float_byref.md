# get_float_byref
#### Syntax
```
native Float:get_float_byref(param);
```

#### Usage
param | ```Argument to retrieve, starting from 1```
---|---
#### Description
```
Returns the float value of a by-reference parameter from the plugin calling
the native.
```

#### Return
```
Float value
```

#### Error
```
If used outside of a native callback, or the native was
created with style 1, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

