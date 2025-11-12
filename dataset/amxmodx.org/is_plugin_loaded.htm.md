s_plugin_loaded
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
is_plugin_loaded - Checks whether a plugin is loaded. 
Syntax
is_plugin_loaded ( const name[] ) 
Type
Native 
Notes
Checks whether a plugin is loaded.   
If it is not, the return value is -1, otherwise the return value is the plugin id.   
The function is case insensitive. 
User Contributed Notes
jtp at jtpage dot net | Dec-04-04 14:51:28  
---|---  
Just wanted to add that this function requires the plugins name as used in register_plugin. I thought it was unclear if I should use the filename or the actual "name" of the plugin. Using the filename will not work.   
  

