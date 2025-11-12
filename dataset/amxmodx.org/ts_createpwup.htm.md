s_createpwup
[TSX](http://127.0.0.1:8000/content/index.htm) (tsx.inc) 
Description
ts_createpwup - Creates a powerup entity and returns its index. 
Syntax
ts_createpwup ( pwup ) 
Type
Native 
Notes
Use ts_givepwup(index,powerupid) to give this powerup to a player, where powerupid is the return value of this function.   
  
Otherwise, give this entity an origin, or it will cause severe errors such as lag.
