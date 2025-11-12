aram_convert
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
param_convert - Converts a parameter's address space 
Syntax
param_convert ( param ) 
Type
Native 
Notes
This function is the same as "lib_convert" from dJeyL's "lib" module. It is only usable if you registered your native with style 1.   
  
param_convert is necessary to use any array, string, or by-reference parameter given to your native. For example:   
` public mynative(str[])   
  
   param_convert(1)   
}   
  `   
Arguments to natives begin at 1.
