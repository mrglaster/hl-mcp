# param_convert
#### Syntax
```
native param_convert(num);
```

#### Usage
num | ```Argument to convert, starting from 1```
---|---
#### Description
```
Converts a parameter to work as a by-reference parameter.
```

This function is deprecated, do NOT use it!
**Reason:** Style 1 natives are deprecated and should be converted to style 0. This should not be used.
#### Note
```
This only needs to be called if the native was registered with style 1.
```

#### Note
```
Remember that arrays (and strings) are always by-reference and need to
be converted.
```

#### Return
```
This function has no return value.
```

#### Error
```
If used outside of a native callback, or the native was
created with style 0, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

