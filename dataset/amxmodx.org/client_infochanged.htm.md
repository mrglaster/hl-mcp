lient_infochanged
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
client_infochanged - Called when a user's client info struct is changed 
Syntax
client_infochanged ( id ) 
Type
Forward 
Notes
This function is commenly used to catch when a player changes his nick.   
`    
public client_infochanged(id)   
      
    new newname[32],oldname[32]   
    get_user_info(id, "name", newname,31)   
    get_user_name(id,oldname,31)   
    client_print(0,3,"%s has changed his name to %s",oldname,newname)   
    }   
  `   
  
id,is a player index from 1 to 32.
