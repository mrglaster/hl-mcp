# Functions in okapi.inc
Function | Description  
---|---  
[okapi_build_method](https://amxx-bg.info/api/okapi/okapi_build_method) | ```
Attaches okapi to a method (class member function) so you can hook it and call it.
```
  
[okapi_build_function](https://amxx-bg.info/api/okapi/okapi_build_function) | ```
Attaches okapi to a function so you can hook it and call it.
```
  
[okapi_build_vfunc_cbase](https://amxx-bg.info/api/okapi/okapi_build_vfunc_cbase) | ```
Attaches okapi to a virtual function of an entity so you can hook it and call it.
```
  
[okapi_build_vfunc_class](https://amxx-bg.info/api/okapi/okapi_build_vfunc_class) | ```
Attaches okapi to a virtual function of an entity (using its class) so you can hook it and call it.
```
  
[okapi_build_vfunc_ptr](https://amxx-bg.info/api/okapi/okapi_build_vfunc_ptr) | ```
Attaches okapi to a virtual function of an object so you can hook it and call it.
```
  
[okapi_add_hook](https://amxx-bg.info/api/okapi/okapi_add_hook) | ```
Adds a hook to a previously attached function.
```
  
[okapi_del_hook](https://amxx-bg.info/api/okapi/okapi_del_hook) | ```
Removes a hook from the function.
```
  
[okapi_del_current_hook](https://amxx-bg.info/api/okapi/okapi_del_current_hook) | ```
Removes current hook from the function.
This is meant to be used inside a hook (when you want to remove it there).
```
  
[okapi_set_param](https://amxx-bg.info/api/okapi/okapi_set_param) | ```
Modifies a parameter that will be passed in the call to the original function.
```
  
[okapi_set_return](https://amxx-bg.info/api/okapi/okapi_set_return) | ```
Modifies the return of the function.
```
  
[okapi_get_orig_return](https://amxx-bg.info/api/okapi/okapi_get_orig_return) | ```
Retrieves the value that the hooked function retrieved.
```
  
[okapi_call](https://amxx-bg.info/api/okapi/okapi_call) | ```
Calls a function without calling its hooks.
```
  
[okapi_call_ex](https://amxx-bg.info/api/okapi/okapi_call_ex) | ```
Calls a function and its hooks
```
  
[okapi_current_hook](https://amxx-bg.info/api/okapi/okapi_current_hook) | ```
Gets the hook that is currently being called.
This is meant to be used inside a hook (when you want to remove it there).
```
  
[wl](https://amxx-bg.info/api/okapi/wl) | ```
Returns a if server is windows, returns b if server is linux.
```
  

This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.