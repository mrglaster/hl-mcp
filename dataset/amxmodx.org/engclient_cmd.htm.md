ngclient_cmd
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
engclient_cmd - This is an emulation of a client command (commands aren't send to client!). 
Syntax
engclient_cmd ( index,const command[],arg1[]= ) 
Type
Native 
Notes
It allows to execute some commands on players and bots. Function is excellent for forcing to do an action related to a game (not settings!). The command must stand alone but in arguments you can use spaces.   
  
index is a player index from 1 to 32.   

User Contributed Notes
pavolmarko at pobox dot sk | Sep-12-04 21:21:08  
---|---  
This actually tells the server (the gamedll) that the client has issued a command. This is the reason why it won't work on stuff like "bind a xD". For normal players, only use it for game-specific server-handled commands (=also won't work with +attack because that is handled clientside).   
  

