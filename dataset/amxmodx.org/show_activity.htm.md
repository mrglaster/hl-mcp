how_activity
[Core](http://127.0.0.1:8000/content/index.htm) (amxmisc.inc) 
Description
show_activity - Shows admin activity. 
Syntax
show_activity ( id, const name[], ... ) 
Type
Stock 
Notes
index is the index of the player running the command. name is the name of the player running the command. The other parameters are the description of the command.   
  
Example:   
show_activity(id,playername,"slapped player");   
  
If amx_show_activity is 2, will appear as: "ADMIN PlayerName: slapped player". If it is 1, it will appear as: "ADMIN: slapped player". 
User Contributed Notes
slayerized at gmail dot com | Apr-10-05 07:20:45  
---|---  
Isn't this kind of pointless when you could just do a switch statement like so: --- ` switch(get_cvar_num("amx_show_activity")) {   
        case 1: client_print(0,print_chat,"ADMIN: Slapped player")   
        case 2: client_print(0,print_chat,"ADMIN %s: Slapped player",szUsername)   
    }  ` --- .. ?   
  

