et_user_userid
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_userid - Returns a player's userid. 
Syntax
get_user_userid ( index ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
A userid is incremented on each connect to the server. It's not an index into an edict list, like a player index (from 1-32).   
  
Example:   
`    
new userid = get_user_userid(index)    
server_cmd("kick #%d Follow the server rules",userid)    
  `
