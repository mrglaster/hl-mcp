et_user_ip
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_ip - Returns a player's IP. 
Syntax
get_user_ip ( index, ip[], len, [ without_port ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
The result is stored in ip for a maximum length of len characters.   
  
If without_port is set to 1, the port is not included in the string (defaults to 0).
