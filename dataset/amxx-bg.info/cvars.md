# Functions in cvars.inc
Function | Description  
---|---  
[create_cvar](https://amxx-bg.info/api/cvars/create_cvar) | ```
Creates a new cvar for the engine.
```
  
[register_cvar](https://amxx-bg.info/api/cvars/register_cvar) | ```
Registers a new cvar for the engine.
```
  
[cvar_exists](https://amxx-bg.info/api/cvars/cvar_exists) | ```
Returns if a cvar is registered on the server.
```
  
[get_cvar_pointer](https://amxx-bg.info/api/cvars/get_cvar_pointer) | ```
Returns the cvar pointer of the specified cvar.
```
  
[hook_cvar_change](https://amxx-bg.info/api/cvars/hook_cvar_change) | ```
Creates a hook for when a cvar's value is changed.
```
  
[disable_cvar_hook](https://amxx-bg.info/api/cvars/disable_cvar_hook) | ```
Disables a cvar hook, stopping it from being called.
```
  
[enable_cvar_hook](https://amxx-bg.info/api/cvars/enable_cvar_hook) | ```
Enables a cvar hook, restoring it to being called.
```
  
[get_cvar_flags](https://amxx-bg.info/api/cvars/get_cvar_flags) | ```
Returns flags of a cvar. The cvar is accessed by name.
```
  
[set_cvar_flags](https://amxx-bg.info/api/cvars/set_cvar_flags) | ```
Sets specified flags to a cvar. The cvar is accessed by name.
```
  
[remove_cvar_flags](https://amxx-bg.info/api/cvars/remove_cvar_flags) | ```
Removes specified flags from a cvar. The cvar is accessed by name.
```
  
[get_cvar_string](https://amxx-bg.info/api/cvars/get_cvar_string) | ```
Gets a string value from a cvar. The cvar is accessed by name.
```
  
[set_cvar_string](https://amxx-bg.info/api/cvars/set_cvar_string) | ```
Sets a cvar to a given string value. The cvar is accessed by name.
```
  
[get_cvar_float](https://amxx-bg.info/api/cvars/get_cvar_float) | ```
Returns a floating value from a cvar. The cvar is accessed by name.
```
  
[set_cvar_float](https://amxx-bg.info/api/cvars/set_cvar_float) | ```
Sets a cvar to a given float value. The cvar is accessed by name.
```
  
[get_cvar_num](https://amxx-bg.info/api/cvars/get_cvar_num) | ```
Returns an integer value from a cvar. The cvar is accessed by name.
```
  
[set_cvar_num](https://amxx-bg.info/api/cvars/set_cvar_num) | ```
Sets a cvar to a given integer value. The cvar is accessed by name.
```
  
[get_pcvar_flags](https://amxx-bg.info/api/cvars/get_pcvar_flags) | ```
Returns flags of a cvar via direct pointer access.
```
  
[set_pcvar_flags](https://amxx-bg.info/api/cvars/set_pcvar_flags) | ```
Sets specified flags to a cvar via direct pointer access.
```
  
[get_pcvar_num](https://amxx-bg.info/api/cvars/get_pcvar_num) | ```
Returns an integer value from a cvar via direct pointer access.
```
  
[get_pcvar_bool](https://amxx-bg.info/api/cvars/get_pcvar_bool) | ```
Returns an boolean value from a cvar via direct pointer access.
```
  
[set_pcvar_num](https://amxx-bg.info/api/cvars/set_pcvar_num) | ```
Sets an integer value to a cvar via direct pointer access.
```
  
[set_pcvar_bool](https://amxx-bg.info/api/cvars/set_pcvar_bool) | ```
Sets a boolean value to a cvar via direct pointer access.
```
  
[get_pcvar_float](https://amxx-bg.info/api/cvars/get_pcvar_float) | ```
Returns a float value from a cvar via direct pointer access.
```
  
[set_pcvar_float](https://amxx-bg.info/api/cvars/set_pcvar_float) | ```
Sets a float value to a cvar via direct pointer access.
```
  
[get_pcvar_string](https://amxx-bg.info/api/cvars/get_pcvar_string) | ```
Returns a string value from a cvar via direct pointer access.
```
  
[set_pcvar_string](https://amxx-bg.info/api/cvars/set_pcvar_string) | ```
Sets a string value to a cvar via direct pointer access.
```
  
[get_pcvar_bounds](https://amxx-bg.info/api/cvars/get_pcvar_bounds) | ```
Retrieves the specified value boundary of a cvar.
```
  
[set_pcvar_bounds](https://amxx-bg.info/api/cvars/set_pcvar_bounds) | ```
Sets the specified boundary of a cvar.
```
  
[bind_pcvar_num](https://amxx-bg.info/api/cvars/bind_pcvar_num) | ```
Binds a cvar's integer value to a global variable. The variable will then
always contain the current cvar value as it is automatically kept up to date.
```
  
[bind_pcvar_float](https://amxx-bg.info/api/cvars/bind_pcvar_float) | ```
Binds a cvar's float value to a global variable. The variable will then
always contain the current cvar value as it is automatically kept up to date.
```
  
[bind_pcvar_string](https://amxx-bg.info/api/cvars/bind_pcvar_string) | ```
Binds a cvar's string value to a global array. The array will then
always contain the current cvar value as it is automatically kept up to date.
```
  
[get_plugins_cvarsnum](https://amxx-bg.info/api/cvars/get_plugins_cvarsnum) | ```
Returns the number of plugin-registered cvars.
```
  
[get_plugins_cvar](https://amxx-bg.info/api/cvars/get_plugins_cvar) | ```
Retrieves information about a plugin-registered cvar via iterative access.
```
  
[query_client_cvar](https://amxx-bg.info/api/cvars/query_client_cvar) | ```
Dispatches a client cvar query, allowing the plugin to query for its value on
the client.
```
  

This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

