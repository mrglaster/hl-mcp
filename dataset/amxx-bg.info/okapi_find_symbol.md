# okapi_find_symbol
#### Syntax
```
native okapi_find_symbol(lib_ptr, const symbol[]);
```

#### Usage
lib_ptr | ```Library base address to search function address in.```
---|---
symbol | ```Symbolic name of a function```
#### Description
```
Gets the address of a function located in a registered library, given it's symbolic name.
```

#### Note
```
Available helpers: okapi_mod_find_symbol
                   okapi_engine_find_symbol
```

#### Return
```
Address of the function on success, 0 otherwise
```


This code is a part of okapi_memory.inc. To use this code you should include okapi_memory.inc as ```#include <okapi_memory>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.