uery_client_cvar
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
query_client_cvar - Dispatches a client cvar query 
Syntax
query_client_cvar ( id, const cvar[], const resultFunc[], paramlen=0, const params[] = "" ) 
Type
Native 
Notes
* id is a player entid from 1 to 32. Must be connected and may not be a bot   
* cvar is the cvar name   
* resultFunc is the name of the public function in your plugin that will be called when the response arrives   
* paramlen cells from the params array will be passed to the result function as its fourth parameter if paramlen is specified.   
  
The result function has the following form:   
`    
public callbackCvarValue(id, const cvar[], const value[])   
  `   
or, if you use the optional array parameter (paramlen + params):   
`    
public callbackCvarValue(id, const cvar[], const value[], const param[])   
  `   
  
* id is the player id   
* cvar and value are self explaining   
  
The function uses a pretty new engine function (added around Aug 11, 2005). Therefore it may cause a native error on out-of-date servers.   
It also uses newdll functions; metamod (at least 1.18) doesn't provide newdll function table hooking for plugins if the mod gamedll doesn't export newdll functions.   
This is fixed in metamod-1.18p26 by ghost_of_evilspy (hullu). [ http://sourceforge.net/projects/metamod-p ]   
  
! This function is only available in the CVS at the moment; it will be available in the next official AMX Mod X release.   
  
**********************************   
Example plugin:   
Log the value of the rate cvar of all connecting users   
`    
#include <amxmodx>   
   
public plugin_init()   
  
    register_plugin("test", "1", "PM");   
}   
   
public client_connect(id)   
  
    if (!is_user_bot(id))   
        query_client_cvar(id, "rate", "cvar_result_func");   
}   
   
public cvar_result_func(id, const cvar[], const value[])   
  
    new name[32];   
    get_user_name(id, name, 31);   
       
    log_amx("Client %d(%s)'s rate is ^"%s^"", id, name, value);   
}   
  `   
  
Logged output:   
L 09/07/2005 - 11:42:25: [test.amxx] Client 1(psychedelic hampster)'s rate is "15000"   

