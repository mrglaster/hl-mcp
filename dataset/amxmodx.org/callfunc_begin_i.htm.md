allfunc_begin_i
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
callfunc_begin_i - Call a function in this / an another plugin by id. 
Syntax
callfunc_begin_i ( func, [ plugin ] ) 
Type
Native 
Notes
plugin - plugin id; the id you would pass to get_plugin   
If lower than 0, the caller plugin is taken   
func - function id   
  
Return value:   
1 - Success   
-1 - Plugin not found   
-2 - Function not executable   
  
Use get_func_id (amxmodx.inc) to get the func id and is_plugin_loaded (amxmodx.inc) or find_plugin_bydesc (amxmisc.inc) / find_plugin_byname (amxmisc.inc) to get plugin id.   

