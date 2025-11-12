egister_impulse
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
register_impulse - Registers a client impulse to a function. 
Syntax
register_impulse ( impulse, function[] ) 
Type
Forward 
Notes
When an impulse is started on a client, the client's id is forwarded to the named function.   
  
This is a blocking forward (PLUGIN_HANDLED will block the operation).
