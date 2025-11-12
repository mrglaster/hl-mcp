# okapi_build_vfunc_class
#### Syntax
```
native okapi_func:okapi_build_vfunc_class(const classname[], offset, okapi_arg:ret, okapi_arg:...);
```

#### Usage
classname | ```Name of the class```
---|---
offset | ```Offset of the function in the virtual table```
ret | ```Return type of the method```
... | ```Rest of the types for the arguments of the function```
#### Description
```
Attaches okapi to a virtual function of an entity (using its class) so you can hook it and call it.
```

#### Note
```
You don't need to pass arg_cbase in the argument list for the entity itself.
```

#### Return
```
Handler to the function attached
```

#### Error
```
Invalid class name
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.