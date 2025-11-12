et_user_gravity
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
set_user_gravity - Sets users gravity 
Syntax
Float: set_user_gravity ( index, [ Float:gravity = 1.0 ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Gravity is a float which defaults to 1.0. Since sv_gravity defaults to 800, you should proportion input right to get the correct results. IE: 1.0 is 800, 2.0 is 1600, 0.5 is 400, and so on.
