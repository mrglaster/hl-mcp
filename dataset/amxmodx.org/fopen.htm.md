open
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
fopen - Returns a file handle for advanced file functions. 
Syntax
fopen ( filename[], mode[] ) 
Type
Native 
Notes
Returns 0 on failure.   
  
Mode uses the standard C library of mode types.   
The first character can be:   
"a" - append   
"r" - read   
"w" - write   
  
The second character can be:   
"t" - text   
"b" - binary   
  
You can also append a "+" to specify both read and write.
