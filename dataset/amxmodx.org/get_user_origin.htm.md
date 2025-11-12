et_user_origin
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_user_origin - Gets a player's origin. 
Syntax
get_user_origin ( index, origin[3], [ mode ] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
The origin is stored in the vector (3 member array) passed as the second parameter.   
origin[0] = X coordinate   
origin[1] = Y coordinate   
origin[2] = Z coordinate   
  
If mode is passed, the origin changes:   
1 - Position from eyes (weapon aiming)   
2 - End position from player position   
3 - End position from eyes (hit point for weapon)   
4 - Position from last bullet hit (only CS)   
  
` public MovePlayer(id)   
  
    new origin[3]   
    get_user_origin(id, origin, 0)  // Gets the current location the player is at   
    origin[2] = origin[2] + 10    // Adds + 10 to the player's height   
    set_user_origin(id, origin)   // Moves the player to the location stored in origin   
}   
  `   
  
  
  
  

