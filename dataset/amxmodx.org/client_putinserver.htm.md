lient_putinserver
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
client_putinserver - Called when a player is initialized into the game. 
Syntax
client_putinserver ( id ) 
Type
Forward 
Notes
id is a player index from 1 to 32.   
  
The pvPrivateData structure is not initialized until this ClientPutInServer() forward is called, so many "hack" commands like cs_get_user_money or anything that modified private offsets will crash or do nothing before this point.   
  
You should never toy with private client variables before a player or entity is put in game.
