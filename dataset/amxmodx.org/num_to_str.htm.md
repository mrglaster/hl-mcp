um_to_str
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
num_to_str - Converts a number to a string. 
Syntax
num_to_str ( num, string[], len ) 
Type
Native 
Notes
Fills string for a max length of len.   
  
This can be written as:   
[format](http://127.0.0.1:8000/content/format.htm)(string, len, "%d", num)
