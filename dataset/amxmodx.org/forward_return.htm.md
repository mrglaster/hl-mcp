orward_return
[Fakemeta](http://127.0.0.1:8000/content/index.htm) (fakemeta.inc) 
Description
forward_return - Returns data for a hook. 
Syntax
forward_return ( type, [ ... ] ) 
Type
Native 
Notes
forward_return can only be called inside a public function called by register_forward.   
  
Type is one of three types:   
#define FMV_STRING 1   
#define FMV_FLOAT 2   
#define FMV_CELL 3   
  
The second parameter must correspondingly be a string, float, or number.   
  
This is similar to RETURN_META_VALUE(..., value);
