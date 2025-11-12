# okapi_set_mem_protect
#### Syntax
```
native bool:okapi_set_mem_protect(ptr, prot);
```

#### Usage
ptr | ```Address in memory```
---|---
prot | ```Protection value, see see PAGE_* constants```
#### Description
```
Changes the memory protection of the location pointed to by the address
```

#### Return
```
true if the operation was successful, false otherwise
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.