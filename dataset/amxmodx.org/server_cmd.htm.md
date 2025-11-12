erver_cmd
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
server_cmd - Executes command on a server console 
Syntax
server_cmd ( const command[],{Float,_}:... ) 
Type
Native 
Notes
Example:   
`    
server_cmd("echo The maxplayers on this server is: %d",get_maxplayers())   
  `   
  
Please do not use this function to set cvars, use: [set_cvar_string](http://127.0.0.1:8000/content/set_cvar_string.htm),[set_cvar_float](http://127.0.0.1:8000/content/set_cvar_float.htm),[set_cvar_num](http://127.0.0.1:8000/content/set_cvar_num.htm)   
  

User Contributed Notes
rh at pdc dot ru | Oct-10-04 14:34:07  
---|---  
Keep in mind that actual execution of command is delayed until last forward function of last plugin is executed or until you call [server_exec](http://127.0.0.1:8000/content/funcwiki.php?go=func&id=281). For example server_cmd called in plugin_init will be executed **after** completion of plugin_init of last pluging listed in plugins.ini   
  

