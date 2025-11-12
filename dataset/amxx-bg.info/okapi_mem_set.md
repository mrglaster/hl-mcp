# okapi_mem_set
#### Syntax
```
native okapi_mem_set(address, type, any:...);
```

#### Usage
address | ```The address where is located the value```
---|---
type | ```The value data type, See okapi_mem_* constants```
... | ```The value to set. If parameter is an array, its size is required as second parameter.```
#### Description
```
Sets the value of the location pointed by the address.
```

#### Note
```
Available helpers: okapi_set_ptr_ent
                   okapi_set_ptr_edict
                   okapi_set_ptr_cbase
                   okapi_set_ptr_int
                   okapi_set_ptr_byte
                   okapi_set_ptr_float
                   okapi_set_ptr_array
                   okapi_set_ptr_string
```

#### Return
```
This function has no return value.
```

#### Error
```
Incorrect parameters count
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.