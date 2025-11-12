et_module
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_module - Gets info about a module. 
Syntax
get_module ( id, name[], nameLen, author[], authorLen, version[], versionLen, &status ) 
Type
Native 
Notes
Parameters:   
id - the id of the module   
name[] - The name of the module will be stored here   
nameLen - maximal length of the name   
author[] - the author will be stored here   
authorLen - maximal length of the author   
version[] - the version of the module will be stored here   
versionLen - maximal length of the version   
status - the status of the module will be stored here   
Return value:   
id - success   
-1 - module not found   
  
status can be:   
module_none   
module_query   
module_badload   
module_loaded   
module_noinfo   
module_noquery   
module_noattach   
module_old
