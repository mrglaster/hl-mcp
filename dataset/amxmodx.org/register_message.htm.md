egister_message
[Engine](http://127.0.0.1:8000/content/index.htm) (engine.inc) 
Description
register_message - Hooks a message to a single function. 
Syntax
register_message ( msgId, function[] ) 
Type
Native 
Notes
This is like an advanced register_event.   
The function you create should have the following arguments passed to it: msg_id, msg_dest, and msg_entity. You should **NEVER** send a message or use a command which sends a message while in a register_message hook.   
  
Returning PLUGIN_CONTINUE will send the message on the stack, PLUGIN_HANDLED will block the message.   
  
See the following commands for using message commands:   
  
[get_msg_args](http://127.0.0.1:8000/content/get_msg_args.htm)   
[get_msg_argtype](http://127.0.0.1:8000/content/get_msg_argtype.htm)   
[get_msg_arg_int](http://127.0.0.1:8000/content/get_msg_arg_int.htm)   
[get_msg_arg_float](http://127.0.0.1:8000/content/get_msg_arg_float.htm)   
[get_msg_arg_string](http://127.0.0.1:8000/content/get_msg_arg_string.htm)   
[set_msg_arg_int](http://127.0.0.1:8000/content/set_msg_arg_int.htm)   
[set_msg_arg_float](http://127.0.0.1:8000/content/set_msg_arg_float.htm)   
[set_msg_arg_string](http://127.0.0.1:8000/content/set_msg_arg_string.htm)   
[get_msg_origin](http://127.0.0.1:8000/content/get_msg_origin.htm)   
  

