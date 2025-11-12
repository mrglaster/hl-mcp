allfunc_begin
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
callfunc_begin - Call a function in this / an another plugin by name. 
Syntax
callfunc_begin ( const function[], [ const plugin[] ] ) 
Type
Native 
Notes
This function works by pushing parameters onto a stack and then executing the target - like the message functions.   
  
Parameters:   
plugin - plugin name; if "", the caller plugin is used.   
If specified, it has to be the exact name (for example stats.amxx)   
func - function name   
Return value:   
1 - Success   
0 - Runtime error (=never)   
-1 - Plugin not found   
-2 - Function not found   
  
This function uses the following functions: [callfunc_end](http://127.0.0.1:8000/content/callfunc_end.htm), [callfunc_push_float](http://127.0.0.1:8000/content/callfunc_push_float.htm), [callfunc_push_floatrf](http://127.0.0.1:8000/content/callfunc_push_floatrf.htm), [callfunc_push_int](http://127.0.0.1:8000/content/callfunc_push_int.htm), [callfunc_push_intrf](http://127.0.0.1:8000/content/callfunc_push_intrf.htm), [callfunc_push_str](http://127.0.0.1:8000/content/callfunc_push_str.htm)   
  
This function must be ended with callfunc_end before being used again, and the function must be public.   
  
If plugin is not specified, the current plugin is used.   
  

User Contributed Notes
pavolmarko at pobox dot sk | Sep-12-04 21:18:32  
---|---  
Some notes: 1) Don't forget to make the funcs that should be called public 2) In previous versions of the inc files, the function and plugin parameters were swapped, it's right the way it is here.   
  

