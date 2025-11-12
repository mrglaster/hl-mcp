s_spawn_player
[NS](http://127.0.0.1:8000/content/index.htm) (ns.inc) 
Description
ns_spawn_player - DEPRECATED. Forces a player to spawn. 
Syntax
ns_spawn_player ( player, [ class=1, health=100, armor=25 ] ) 
Type
Native 
Notes
This native is DEPRECATED and no longer available for use.   
  
I would not use this while the player's deadflags is 1 or 0. Only use when the player is dead with deadflags of 2 or higher. For class, use the fields specified in the NS Mini SDK (1=marine,3=skulk,4=gorge,5=lerk,6=fade,7=onos).
