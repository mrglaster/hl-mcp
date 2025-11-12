ormat
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
format - Format a string with a given format and parameters. 
Syntax
format ( output[], len, const format[], ... ) 
Type
Native 
Notes
Fills output for a maximum of length characters, with a string formatted by a list of parameters. Returns the number of copied characters.   
  
The available formatting codes are:   
%s - String   
%f - Floating point number   
%d - Integer   
  
This formatting code is found in many other functions, for example, [client_print](http://127.0.0.1:8000/content/client_print.htm):   
[client_print](http://127.0.0.1:8000/content/client_print.htm)(id, print_chat, "Message[%d]: %s", id, message)   
  
Example:   
` new dest[21]   
format(dest, 20, "Hello %s. You are %d years old", "Tom", 17)   
//Dest will contain "Hello Tom.  You are 17 years old.   
  `
User Contributed Notes
grimm at clanlad dot com | Nov-16-04 17:13:37  
---|---  
Actually it will only fill the string with the first 20 characters.   
  
jblaise dot cs at tele2 dot fr | Aug-27-04 04:29:12  
---|---  
Hmm I think there is an error... "//Dest will contain "Hello Tom. You are 17 years old." I think : "//Dest will contain "Hello Tom. You are 17 years old." This is a little error but now it s perfect ;)   
  

