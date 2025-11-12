s_get_spawn
[NS](http://127.0.0.1:8000/content/index.htm) (ns.inc) 
Description
ns_get_spawn - Gets spawn points for specified team. 
Syntax
ns_get_spawn ( team, [ number = 0 ], Float:ret[3] ) 
Type
Native 
Notes
If team is equal to 0: Ready room spawns are returned.   
  
If team is greater than 0: Spawns for the team are returned.   
  
If number is equal to 0 (default): Total number of spawns is returned.   
  
If number is greater than 0: The location of the specified spawn is passed into ret.
