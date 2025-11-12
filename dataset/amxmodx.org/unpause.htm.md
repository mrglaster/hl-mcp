npause
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
unpause - Unpauses function or plugin. 
Syntax
unpause ( flag[], const param1[]= ) 
Type
Native 
Notes
**Note:** As of AMX Mod X 1.1, the "b" flag has been deprecated and no longer works. The implementation was poor and a proper version would be a great performance hit. Instead, use your own internal variables to switch function bodies on and off.   
  
Flags:   
"a" - unpause whole plugin.   
"b" - unpause function.   
"c" - look outside the plugin (by given plugin name).   

