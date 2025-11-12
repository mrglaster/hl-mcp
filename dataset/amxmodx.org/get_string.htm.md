et_string
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
get_string - Retrieves a string from a calling plugin 
Syntax
get_string ( param, string[], maxlen ) 
Type
Native 
Notes
This can only be used in a dynamic native function registered with style 0 (default). Arguments start at 1.   
  
It will copy the argument passed by the calling plugin into your buffer, as a string.
