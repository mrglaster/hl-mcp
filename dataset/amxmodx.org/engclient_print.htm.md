ngclient_print
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
engclient_print - Sends a message to a player through the engine. 
Syntax
engclient_print ( index, type, const message[], ... ) 
Type
Native 
Notes
index is a player index from 1 to 32. If 0, the message will be sent to all players.   
  
The type is one of three types:   
engprint_chat - chat text   
engprint_console - console message   
engprint_center - center say   
  
message can be a formatted string in the style of [format](http://127.0.0.1:8000/content/format.htm).   

