loat_to_str
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
float_to_str - Converts float to string 
Syntax
float_to_str ( Float:fl, string[], len ) 
Type
Native 
Notes
The native has the same effect as calling   
`    
format(string, len, "%f", fl);   
  `   
(but should have a slightly higher performance)   
  
Example:   
`    
new str[16];   
float_to_str(1337.0987654321, str, 15);   
   
// str will be "1337.098755" (it will have a higher precision when running on amd64,   
// this was tested on a 32 bit system)   
  `
