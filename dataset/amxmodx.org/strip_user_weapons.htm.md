trip_user_weapons
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
strip_user_weapons - Strips all weapons from user 
Syntax
strip_user_weapons ( index ) 
Type
Native 
Notes
Warning ! Don't use this function IN ResetHUD event. This will probably crash server. To fix this use set_task with time more or equal to 0.1 sec.   
  

User Contributed Notes
Radical_mel at hotmail dot com | Sep-17-04 00:49:16  
---|---  
Never ever use it in server_frame()   
  

