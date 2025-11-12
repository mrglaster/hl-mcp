et_func_id
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_func_id - Returns the id of {funcName} in {plugin} 
Syntax
get_func_id ( const funcName[], [ pluginId ] ) 
Type
Native 
Notes
Parameters:   
* funcName: function name   
* pluginId: id of the plugin; if lower than 0, the caller plugin is taken (=> the function behaves exactly like funcidx (core.inc))   
  
Return value is -1 when the function / the plugin could not be found.
