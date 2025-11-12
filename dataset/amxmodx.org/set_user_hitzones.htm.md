et_user_hitzones
[Fun](http://127.0.0.1:8000/content/index.htm) (fun.inc) 
Description
set_user_hitzones - Sets hit zones for player. 
Syntax
set_user_hitzones ( [ index = 0, target = 0, body = 255 [ ) 
Type
Native 
Notes
Sets hit zones for player.   
Parts of body are as bits:   
1 - generic   
2 - head   
4 - chest   
8 - stomach   
16 - left arm   
32 - right arm   
64 - left leg   
128 - right leg   
  
Set index to a player's index and leave target at 0 to define what bodyparts this player can hit when he is firing.   
  
Set index to 0 and target to a player's index to define what bodyparts on player other players can hit when they are firing.   
  
Set both index and target to 0 to define globally what bodyparts people can hit and what bodyparts can be hit when firing.   
Example: ( Make a single player fire blanks )   
`    
set_user_hitzones(index, 0, 0)   
  `   
  
Remember that this funtion does NOT affect grenades and knives. 
User Contributed Notes
storm at stormwc3 dot com | Jul-21-04 09:55:46  
---|---  
there seems to be a bug with the set_user_hitzones in the amxmodx. i have a blanks plugin, but instead of giving the player blanks, it sets them to godmode (giving everyone blanks when shooting at that player). code: new player = cmd_target(id, arg, 5) if(!player) return PLUGIN_HANDLED set_user_hitzones(player, 0, 0) seems to be looking at the code like set_user_hitzones(0, player, 0) this plugin worked perfect under amx mod   
  

