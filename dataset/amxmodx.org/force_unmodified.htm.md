orce_unmodified
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
force_unmodified - Forces the client and server to be running with the same version of the specified file ( e.g., a player model ) 
Syntax
force_unmodified ( force_type, mins[3] , maxs[3], const filename[] ) 
Type
Native 
Notes
The force_type is one of three types:   
force_exactfile - File on client must exactly match server's file   
force_model_samebounds - For model files only, the geometry must fit in the same bbox   
force_model_specifybounds - For model files only, the geometry must fit in the specified bbox
