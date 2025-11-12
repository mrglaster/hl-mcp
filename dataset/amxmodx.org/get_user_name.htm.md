et_user_name
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_name - Finds the name of a player. 
Syntax
get_user_name ( index, name[], len ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Stores the name for a maximum of len characters. 
User Contributed Notes
weecka at stablebeast dot com | Aug-28-05 19:54:11  
---|---  
example of using it: `    
new name[18]   
get_user_name(id, name, 17)   
client_print(id, print_chat, "Your name is: %s", name)   
  `  
  

