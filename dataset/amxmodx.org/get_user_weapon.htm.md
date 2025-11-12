et_user_weapon
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_weapon - Returns id of a player's currently carried weapon. 
Syntax
get_user_weapon ( index, &clip, &ammo ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
clip and ammo will contain the amount of ammo in the clip and backpack (passed byref).
