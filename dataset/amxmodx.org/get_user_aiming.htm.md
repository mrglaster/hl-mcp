et_user_aiming
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_aiming - Traces where a player is aiming for a maximum distance defaulted to 9999. 
Syntax
Float: get_user_aiming ( index, &id, &body, [ distance ] ) 
Type
Native 
Notes
If the player's aim doesn't hit anything, 0.0 is returned.   
  
If the player is aiming at another player, then the id and part of the body is set into the second and third parameters (passed by reference).   
  
Otherwise, the distance between the hit point and the player is returned.   
  
index,is a player index from 1 to 32.
