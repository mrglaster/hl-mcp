# Functions in okapi_extra.inc
Function | Description  
---|---  
[okapi_get_library_ptr](https://amxx-bg.info/api/okapi_extra/okapi_get_library_ptr) | ```
Gets the base address of where the provided library is allocated in memory.
```
  
[okapi_get_library_size](https://amxx-bg.info/api/okapi_extra/okapi_get_library_size) | ```
Gets the length of the library.
```
  
[okapi_find_library_by_ptr](https://amxx-bg.info/api/okapi_extra/okapi_find_library_by_ptr) | ```
Finds informations of a library from a given address.
This will look up among all libraries registered by module.
```
  
[okapi_cbase_to_id](https://amxx-bg.info/api/okapi_extra/okapi_cbase_to_id) | ```
Converts a cbase (that is, the address of the c++ object of an entity) to an id.
```
  
[okapi_id_to_cbase](https://amxx-bg.info/api/okapi_extra/okapi_id_to_cbase) | ```
Converts the id of an entity to its cbase (that is, the address of the c++ object of an entity).
```
  
[okapi_cbase_get_vfunc_ptr](https://amxx-bg.info/api/okapi_extra/okapi_cbase_get_vfunc_ptr) | ```
Retrieves a virtual function address located in the virtual table of an entity.
```
  
[okapi_class_get_vfunc_ptr](https://amxx-bg.info/api/okapi_extra/okapi_class_get_vfunc_ptr) | ```
Retrieves a virtual function address located in the virtual table of an entity, created using it's classname.
```
  
[okapi_ptr_get_vfunc_ptr](https://amxx-bg.info/api/okapi_extra/okapi_ptr_get_vfunc_ptr) | ```
Retrieves a virtual function address located in the virtual table of an object (can be a cbase or another one).
```
  
[okapi_get_ptr_symbol](https://amxx-bg.info/api/okapi_extra/okapi_get_ptr_symbol) | ```
Retrieves the symbolic name of an address, if one exists.
This functions just works/makes sense on linux/osx.
```
  
[okapi_get_engfunc_ptr](https://amxx-bg.info/api/okapi_extra/okapi_get_engfunc_ptr) | ```
Retrieves the address of an engfunc function.
```
  
[okapi_get_dllfunc_ptr](https://amxx-bg.info/api/okapi_extra/okapi_get_dllfunc_ptr) | ```
Retrieves the address of an dllfunc function.
```
  
[okapi_get_engfunc_ptr_by_offset](https://amxx-bg.info/api/okapi_extra/okapi_get_engfunc_ptr_by_offset) | ```
Retrieves the address of an engfunc function by its relative offset in the struct enginefuncs_t.
```
  
[okapi_get_dllfunc_ptr_by_offset](https://amxx-bg.info/api/okapi_extra/okapi_get_dllfunc_ptr_by_offset) | ```
Retrieves the address of a dllfunc function by its relative offset in the struct DLL_FUNCTIONS.
```
  

This code is a part of okapi_extra.inc. To use this code you should include okapi_extra.inc as ```#include <okapi_extra>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.