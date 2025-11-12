# okapi_mem_find
#### Syntax
```
native okapi_mem_find(start_address, range_length, type, any:...);
```

#### Usage
start_address | ```Address where the search starts```
---|---
range_length | ```Length range of bytes where function is allowed to search in.```
type | ```Value data type, See okapi_mem_* constants```
... | ```Variable parameters to provide. if type is intege, float, string: <value> if type is array : <array> <size_array>ze.```
#### Description
```
Searches for a value in a library in a range from a start address.
```

#### Note
```
Only string, array, integer and float can be searched.
```

#### Note
```
Available helpers: okapi_mod_find_string_at      okapi_engine_find_string_at
                   okapi_mod_find_string         okapi_engine_find_string
                   okapi_mod_find_array_at       okapi_engine_find_array_at
                   okapi_mod_find_array          okapi_engine_find_array
                   okapi_mod_find_int_at         okapi_engine_find_int_at
                   okapi_mod_find_int            okapi_engine_find_int
                   okapi_mod_find_float_at       okapi_engine_find_float_at
                   okapi_mod_find_float          okapi_engine_find_float
                   okapi_mod_find_byte_at        okapi_engine_find_byte_at
                   okapi_mod_find_byte           okapi_engine_find_byte
```

#### Return
```
Address where the first string was found, 0 otherwise.
```

#### Error
```
Invalid data type
Incorrect parameters count
Missing array size parameter
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.