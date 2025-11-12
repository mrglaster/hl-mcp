# okapi_mem_get
#### Syntax
```
native any:okapi_mem_get(address, type, any:...);
```

#### Usage
address | ```The address where is located the value```
---|---
type | ```The value data type, See okapi_mem_* constants```
... | ```If zero additional parameters are provided, the function will return an integer or float value directly. If one additional parameter is provided, the function will store an integer as float, a float or vector. If two additional parameters are provided, the function will copy a string or an array to the buffer provided in the second parameter, using the third as the maximum buffer size.```
#### Description
```
Retrieves the value in an address.
```

#### Note
```
Available helpers: okapi_get_ptr_ent
                   okapi_get_ptr_edict
                   okapi_get_ptr_cbase
                   okapi_get_ptr_int
                   okapi_get_ptr_float
                   okapi_get_ptr_byte
                   okapi_get_ptr_array
                   okapi_get_ptr_strning
```

#### Return
```
If zero additional parameters are provided, the function
will return an integer or float value.
If two additional parameters are provided and data typ is
a string, the function will return the number of cells
written to the buffer.
```

#### Error
```
Invalid return type
Incorrect parameters count
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.