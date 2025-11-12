# okapi_find_library_by_ptr
#### Syntax
```
native bool:okapi_find_library_by_ptr(ptr, &lib_ptr, &lib_size = 0, const lib_name[] = "", lib_namelen = 0);
```

#### Usage
ptr | ```Address to search```
---|---
lib_ptr | ```Variable to store the library base address in```
lib_size | ```Variable to store the library length in```
lib_name | ```Buffer to copy library name to```
lib_namelen | ```Maximum size of the buffer```
#### Description
```
Finds informations of a library from a given address.
This will look up among all libraries registered by module.
```

#### Return
```
true on successful lookup, false otherwise.
```


This code is a part of okapi_extra.inc. To use this code you should include okapi_extra.inc as ```#include <okapi_extra>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.