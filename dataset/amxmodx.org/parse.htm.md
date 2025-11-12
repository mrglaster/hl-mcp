arse
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
parse - Splits parameters into strings. 
Syntax
parse ( const text[], ... ) 
Type
Native 
Notes
Example: to split text: "^"This is^" the best year",   
parse(text,arg1,len1,arg2,len2,arg3,len3,arg4,len4)   
You will get: "This is", "the", "best", "year"   
Function returns number of parsed parameters.   
  
For a more advanced version, see [strbreak](http://127.0.0.1:8000/content/strbreak.htm).
