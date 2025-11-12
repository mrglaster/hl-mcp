lugin_modules
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
plugin_modules - Module check routine - DEPRECATED 
Syntax
plugin_modules ( ) 
Type
Forward 
Notes
**Update** :   
This routine is deprecated and is never called as of AMX Mod X 1.1.   
  
This routine is called before anything else - even plugin_init. For this reason most natives will be unitialized and using them will crash. The only function you are allowed to use here is [require_module](http://127.0.0.1:8000/content/require_module.htm).   

