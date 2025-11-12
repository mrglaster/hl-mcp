essage_begin
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
message_begin - These functinos are used to generate client messages. 
Syntax
message_begin ( dest, msg_type, origin[3]={0,0,0},player=0 ) 
Type
Native 
Notes
You may generate menu, smoke, shockwaves, thunderlights, intermission and many many others messages. See HL SDK for more examples.   
  
Other function related: [message_end](http://127.0.0.1:8000/content/message_end.htm), [write_byte](http://127.0.0.1:8000/content/write_byte.htm), [write_char](http://127.0.0.1:8000/content/write_char.htm), [write_short](http://127.0.0.1:8000/content/write_short.htm), [write_long](http://127.0.0.1:8000/content/write_long.htm), [write_entity](http://127.0.0.1:8000/content/write_entity.htm), [write_angle](http://127.0.0.1:8000/content/write_angle.htm), [write_coord](http://127.0.0.1:8000/content/write_coord.htm), [write_string](http://127.0.0.1:8000/content/write_string.htm)   
  
Before calling another message_begin you must call message_end(). Sending a new message before another is complete or sending an invalid message number (such as 0) will cause the server to crash.
