ungFoo_Attack
[TSFUN](http://127.0.0.1:8000/content/index.htm) (tsfun.inc) 
Description
KungFoo_Attack - Called when someone executes a kung foo move 
Syntax
KungFoo_Attack ( id, Float:time, Float:damage ) 
Type
Forward 
Notes
**Depreciated, use Melee_Attack forward.**   
returns the id of the player attempting to attack, along with the time the attack lasts, and the damage it deals (if it hits)   
  
Use ts_set_fuattack to alter, and return PLUGIN_HANDLED to block.   

