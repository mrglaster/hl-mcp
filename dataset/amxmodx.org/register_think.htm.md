egister_think
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
register_think - Registers a think action to a function. 
Syntax
register_think ( Classname[], function[] ) 
Type
Forward 
Notes
If an entity of Classname[] thinks, its entity ID is forwarded to the named function.   
  
This is not a blocking function, PLUGIN_HANDLED and PLUGIN_CONTINUE will have no effect.
