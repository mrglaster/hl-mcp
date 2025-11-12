race_forward
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
trace_forward - Read Below 
Syntax
trace_forward ( Float:start[3], Float:angles[3], Float:give, ignoreEnt, &Float:hitX, &Float:hitY, &Float:shortestDistance, &Float:shortestDistLow, &Float:shortestDistHigh ) 
Type
Native 
Notes
Will be added for AMX Mod X 1.1   
  
trace_forward takes an origin from the center of a player (Float:start[3]) and an angle vector (use entity_get_vector(player,EV_VEC_angles,vec). It traces in front of the player, returning the distance to the closest obtrusion, the lowest height (min 0.0, meaning on the ground) of the obtrusion and the highest point of the obtrusion (max 72.0, meaning above the players head). Give is how much the distance to the obtrusion may very to still be considered the same obtrusion, if you pass a value less than zero it is automatically set to 20.0. ignoreEnt if 0 ignores entities, if greater than zero, it ignores the passed entity index. The closer the passed origin is to the obtrusion, the more accurate it is.   

