# okapi_build_method
#### Syntax
```
native okapi_func:okapi_build_method(ptr, okapi_arg:ret, okapi_arg:class, okapi_arg:...);
```

#### Usage
ptr | ```Address of the method```
---|---
ret | ```Return type of the method```
class | ```Type of the method class```
... | ```Rest of the types for the arguments of the function```
#### Description
```
Attaches okapi to a method (class member function) so you can hook it and call it.
```

#### Return
```
Handler to the method attached
```

#### Error
```
Invalid method address
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.