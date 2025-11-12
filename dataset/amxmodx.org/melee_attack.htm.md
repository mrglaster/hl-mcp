elee_Attack
[TSFUN](http://127.0.0.1:8000/content/index.htm) (tsfun.inc) 
Description
Melee_Attack - Called on any melee attack 
Syntax
Melee_Attack ( id, Float:time, Float:damage ) 
Type
Forward 
Notes
**Use this instead of KungFoo_Attack**   
  
Returns the id of the player attempting to attack, along with the time the attack lasts, and the damage it deals (if it hits)   
  
Use ts_set_fuattack to alter, and return PLUGIN_HANDLED to block.
