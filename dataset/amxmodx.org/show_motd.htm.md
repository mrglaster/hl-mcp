how_motd
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
show_motd - Displays an MOTD style window to a user. 
Syntax
show_motd ( player, const message[], [ const header[] ] ) 
Type
Native 
Notes
player is a player index from 1 to 32.   
  
message can either be a filename or a string formatted message. With VGUI2, the message can be HTML formatted.   
  
You can supply an optional title bar for the window. If not supplied, it will default to the server name.   
  
The length of the message should not be more than around 1,200 characters - going over this limit could potentially crash the client.   

