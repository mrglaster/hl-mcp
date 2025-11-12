# SetHamParamVector
#### Syntax
```
native SetHamParamVector(which, const Float:value[3]);
```

#### Usage
which | ```Which parameter to change.  Starts at 1, and works up from the left to right.  1 is always "this".```
---|---
value | ```The value to change it to.```
#### Description
```
Sets a parameter on the fly of the current hook.  This has no effect in post hooks.
Use this on parameters that are Vectors.
```


This code is a part of hamsandwich.inc. To use this code you should include hamsandwich.inc as ```#include <hamsandwich>```


  
  

