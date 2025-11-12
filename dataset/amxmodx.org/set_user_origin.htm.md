et_user_origin
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
set_user_origin - Move player to origin 
Syntax
set_user_origin ( index, origin[3] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
Example:   
` public MovePlayer(id)   
  
    new origin[3]   
    get_user_origin(id,origin,0)  // Gets the current location the player is at   
    origin[2] = origin[2] + 10    // Adds + 10 to the players hight   
    set_user_origin(id,origin)   // Moves the player to the location stored in origin   
}   
  `   

