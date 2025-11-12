et_user_maxspeed
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
set_user_maxspeed - Sets a user's maxspeed 
Syntax
Float: set_user_maxspeed ( index, [ Float:speed = - 1.0 ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Speed defaults to -1.0.   
  
If you set a user's maxspeed to 0.0 they will be able to run normal speed. Set it to 0.1 if you wish to stop them from moving completely. 
User Contributed Notes
Freeecode at hotmail dot com | Jun-24-04 20:43:26  
---|---  
Note that the speed is reset once you change your weapon and on New Round. So the best way to keep the speed that you want is set it in the Weapon Event.   
  

