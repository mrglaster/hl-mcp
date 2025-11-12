lient_authorized
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
client_authorized - Called when a player has authenticated with Steam 
Syntax
client_authorized ( id ) 
Type
Forward 
Notes
Until a player has authenticated on Steam, their authid from [get_user_authid](http://127.0.0.1:8000/content/get_user_authid.htm) will be STEAM_ID_PENDING.   
  
id is a player index from 1 to 32.
