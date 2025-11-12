egister_logevent
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
register_logevent - Registers a function to be called on a log event 
Syntax
register_logevent ( const function[], argsnum, ... ) 
Type
Native 
Notes
function is the name of a public function to be called on the logged message.   
  
argsnum is the number of arguments to retrieve.   
  
You can filter the results by adding conditional parameters. Examples:   
"0=World triggered" "1=Game_Commencing"   
"1=say"   
"3=Terrorists_Win"   
"1=entered the game"   
"0=Server cvar"   
  
You can get the log data with the functions: [read_logdata](http://127.0.0.1:8000/content/read_logdata.htm), [read_logargc](http://127.0.0.1:8000/content/read_logargc.htm), [read_logargv](http://127.0.0.1:8000/content/read_logargv.htm).   
  
Example:   
` public plugin_init()   
  
    register_plugin("Logevent Example","0.1","SniperBeamer")   
    register_logevent("joined_team",3,"1=joined team","2=CT")   
}   
   
public joined_team()   
  
    new Arg1[64],Arg2[64]   
    read_logargv(0,Arg1,63) // [L] Arg0: SniperBeamer<1><4294967295><>   
    read_logargv(2,Arg2,63) // [L] Arg2: CT   
}   
  `
