# RageTryGetFunction
#### Syntax
```
native RageFunc:RageTryGetFunction(const libFunctionName[])
```

#### Usage
libFunctionName | ```The name of the function as it is in the file where the function is defined```
---|---
#### Description
```
Tries to retrieve a function based on a function name
If it doesn't find one it returns invalid function instead of failing
The name must be the same as the one in the file where the function is defined
```

#### Return
```
A handler to the function
```


This code is a part of rage.inc. To use this code you should include rage.inc as ```#include <rage>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.