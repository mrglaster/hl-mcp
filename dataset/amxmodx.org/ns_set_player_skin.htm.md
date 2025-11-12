s_set_player_skin
[NS](http://127.0.0.1:8000/content/index.htm) (ns.inc) 
Description
ns_set_player_skin - Sets a player's skin. 
Syntax
ns_set_player_skin ( index, [ skin = -1 ] ) 
Type
Native 
Notes
Forces ns2amx to set the player's model/skin/body to the specified each frame. Note that the model will not go back to standard when the player dies/changes classes. Your plugin will have to tell the module to stop using the custom model.   
  
Leave the second parameter out of any of these commands to force the module to go back to standard.
