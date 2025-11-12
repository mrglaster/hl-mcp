# get_param_byref
#### Syntax
```
native get_param_byref(param);
```

#### Usage
param | ```Argument to retrieve, starting from 1```
---|---
#### Description
```
Returns the integer value of a by-reference parameter from the plugin calling
the native.
```

#### Return
```
Integer value
```

#### Error
```
If used outside of a native callback, or the native was
created with style 1, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

