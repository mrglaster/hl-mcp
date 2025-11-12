# okapi_ptr_get_vfunc_ptr
#### Syntax
```
native okapi_ptr_get_vfunc_ptr(ptr, offset);
```

#### Usage
ptr | ```Address of the object```
---|---
offset | ```Offset of the virtual function in the virtual table```
#### Description
```
Retrieves a virtual function address located in the virtual table of an object (can be a cbase or another one).
```

#### Return
```
Address of the virtual function
```


This code is a part of okapi_extra.inc. To use this code you should include okapi_extra.inc as ```#include <okapi_extra>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.