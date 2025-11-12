s_set_user_vip
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_set_user_vip - Sets whether a user is the VIP. 
Syntax
cs_set_user_vip ( index, [ vip = 1] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
The model will be changed to VIP model if 1, else it will be changed to a random CT model.   
  
This shouldn't be used for players on teams other than CT.   
  
This is mostly useful for unsetting vips, so they can change teams and/or buy items properly. It does not alter game play; the one being VIP at start of round will retain internal status as VIP; terrorists can terminate him and accomplish their objective, etc.   

