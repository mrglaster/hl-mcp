s_set_user_model
[Cstrike](http://127.0.0.1:8000/content/index.htm) (cstrike.inc) 
Description
cs_set_user_model - Sets a player's model (CS only). 
Syntax
cs_set_user_model ( index, const model[] ) 
Type
Native 
Notes
index is a player index from 1 to 32.   
  
model is set as "gign" or "leet", for example, NOT "models/player/gign/gign.mdl". 
User Contributed Notes
mattemarklund at msn dot com | Feb-18-05 18:53:41  
---|---  
how do I change model for someone who types f.e. /gign to a CT>gign model? I've tried everything, it just says "No such command" or something, when I remove cs_set_user_model(id,"gign") the command works again, and my includes are: amxmisc, amxmodx, fun, engine   
  

