trbreak
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
strbreak - Gets parameters from text one at a time. 
Syntax
strbreak ( const text[], left[], leftLen, right[], rightLen ) 
Type
Native 
Notes
It breaks a string into the first parameter and the rest of the parameters (A left side and right side of the string).   
Example: to split text: "^"This is^" the best year",   
  
split(text, arg1, len1, arg2, len2)   
arg1="This is", arg2=the best year   
  
This is more useful than parse() because you can keep breaking any number of arguments. 
User Contributed Notes
anonymous | Feb-22-05 01:27:03  
---|---  
Actually, shouldn't it be: arg1="^"This is^"" arg2="the best year"  
  
anonymous | Feb-22-05 01:26:09  
---|---  
Add quotes around "the best year"   
  
bailopan at gmail dot com | Sep-03-04 04:41:27  
---|---  
It exists in AMX Mod X 0.20.   
  

