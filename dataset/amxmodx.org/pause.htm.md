ause
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
pause - Pauses function or plugin so it won't be executed. 
Syntax
pause ( flag[], const param1[]= ) 
Type
Native 
Notes
**Note:** As of AMX Mod X 1.1, the "b" flag has been deprecated and no longer works. The implementation was poor and a proper version would be a great performance hit. Instead, use your own internal variables to switch function bodies on and off.   
  
In most cases param1 is name of function and   
param2 name of plugin (all depends on flags).   
Flags:   
"a" - pause whole plugin.   
"b" - pause function.   
"c" - look outside the plugin (by given plugin name).   
"d" - set "stopped" status when pausing whole plugin.   
"e" - set "locked" status when pausing whole plugin.   
In this status plugin is unpauseable.   
Example: pause("ac","myplugin.amxx")   
pause("bc","myfunc","myplugin.amxx")   
  

