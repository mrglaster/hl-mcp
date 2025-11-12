# okapi_mem_replace
#### Syntax
```
native okapi_mem_replace(start_address, range_length, type, any:...);
```

#### Usage
start_address | ```Address where the search starts```
---|---
range_length | ```Length range of bytes where function is allowed to search in.```
type | ```Value data type, See okapi_mem_* constants```
... | ```Variable parameters to provide. if type is integer or float: <old_value> <new_value> if type is array : <old array> <new_array> <num_bytes> if type is string: <old string> <new_string> [force = 0] If force parameter is set to 1, it will skip the restrition of the string replacement size.```
#### Description
```
Replaces every value with another one that occurs in a range from a start address.
```

#### Note
```
Only string, array, integer and float can be replaced.
```

#### Note
```
The replacement string should be of equal or shorter size than the original.
If you know what you are doing and want to skip this check, make force to 1.
```

#### Note
```
Available helpers: okapi_mod_replace_string    okapi_engine_replace_string
                   okapi_mod_replace_array     okapi_engine_replace_array
                   okapi_mod_replace_int       okapi_engine_replace_int
                   okapi_mod_replace_float     okapi_engine_replace_float
```

#### Return
```
Number of replacements ocurred
```

#### Error
```
Invalid data type
Incorrect parameters count
Invalid replacement string length
Missing array size
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.