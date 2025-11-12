# okapi_build_vfunc_cbase
#### Syntax
```
native okapi_func:okapi_build_vfunc_cbase(id, offset, okapi_arg:ret, okapi_arg:...);
```

#### Usage
id | ```Index of the entity```
---|---
offset | ```Offset of the function in the virtual table```
ret | ```Return type of the method```
... | ```Rest of the types for the arguments of the function```
#### Description
```
Attaches okapi to a virtual function of an entity so you can hook it and call it.
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
Invalid entity
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.