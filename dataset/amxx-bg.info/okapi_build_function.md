# okapi_build_function
#### Syntax
```
native okapi_func:okapi_build_function(ptr, okapi_arg:ret, okapi_arg:...);
```

#### Usage
ptr | ```Address of the method```
---|---
ret | ```Return type of the method```
... | ```Rest of the types for the arguments of the function```
#### Description
```
Attaches okapi to a function so you can hook it and call it.
```

#### Return
```
Handler to the function attached
```

#### Error
```
Invalid function address
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.