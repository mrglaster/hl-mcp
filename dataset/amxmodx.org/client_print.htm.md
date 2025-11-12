lient_print
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
client_print - Sends a message to a player. 
Syntax
client_print ( index, type, const message[], ... ) 
Type
Native 
Notes
id is a player index from 1 to 32. If 0, the message will be sent to all players.   
  
The type is one of three types:   
print_chat - chat text   
print_console - console message   
print_notify - console in dev mode   
print_center - center say   
  
message can be a formatted string in the style of [format](http://127.0.0.1:8000/content/format.htm).
