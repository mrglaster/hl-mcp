equire_module
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
require_module - Sets a requirement for a module - DEPRECATED 
Syntax
require_module ( const name[] ) 
Type
Native 
Notes
**Update** :   
This routine is deprecated in AMX Mod X 1.1. It does nothing and always returns 1.   
  
This function may only be called in [plugin_modules](http://127.0.0.1:8000/content/plugin_modules.htm). Do not call it anywhere else.   
  
The name is the name the module displays when you type "amxx modules". It is case insensitive. The only "magic" name is "DBI", which will detect any module that has "DBI" or "SQL" in its name.   
  
If no matching module is loaded for each require_module() line, the plugin will fail to load and an error message will instruct the user to check modules.ini.   

