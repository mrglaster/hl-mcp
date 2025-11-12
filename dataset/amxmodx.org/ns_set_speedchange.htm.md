s_set_speedchange
[NS](http://127.0.0.1:8000/content/index.htm) (ns.inc) 
Description
ns_set_speedchange - Used to change a player's speed change. 
Syntax
ns_set_speedchange ( index, [ speedchange = 0 ] ) 
Type
Native 
Notes
Since this can vary, a static speed isn't set. Rather, the module will add the speedchange to the player's maxspeed every frame.   
  
Omit the second parameter to return to default .
