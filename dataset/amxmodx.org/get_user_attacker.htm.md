et_user_attacker
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_attacker - Returns the index of an attacking player. 
Syntax
get_user_attacker ( index, [ &weapon, &hitzone ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
If a second or third parameter is supplied, information about the weapon and hitzone is stored in the variables (passed byref).   
  
If no player is attacking the indexed player, get_user_attacker will return 0.
