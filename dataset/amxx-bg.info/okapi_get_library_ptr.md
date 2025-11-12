# okapi_get_library_ptr
#### Syntax
```
native okapi_get_library_ptr(const lib_name[])
```

#### Usage
lib_name | ```Library name```
---|---
#### Description
```
Gets the base address of where the provided library is allocated in memory.
```

#### Note
```
By default Okapi registers the game as "mod", the engine as "engine" and
any library where its file path contains "addons". To get the library name,
module keeps only the file name without extension and without "_i386" for linux.
Examples: "metamod", "amxmodx_mm", "okapi_amxx"
```

#### Note
```
Available helpers: okapi_get_mod_address, okapi_get_engine_address
```

#### Return
```
Base address on success, 0 otherwise.
```


This code is a part of okapi_extra.inc. To use this code you should include okapi_extra.inc as ```#include <okapi_extra>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.