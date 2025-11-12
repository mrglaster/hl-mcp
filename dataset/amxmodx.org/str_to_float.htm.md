tr_to_float
[Core](http://127.0.0.1:8000/content/index.htm) (string.inc) 
Description
str_to_float - Converts a string to a float 
Syntax
Float: str_to_float ( const string[] ) 
Type
Native 
Notes
The function takes a string, parses a float, and returns it.   
  
Example:   
`    
Float:fl = str_to_float("-5.06"); // fl will be -5.06   
  `   
  
A leading + sign is accepted (but optional).   
When the function finds a character that is not a digit and not a period, it stops parsing and returns.   
  
More examples:   
`    
str_to_float(""); // returns 0.0   
str_to_float("2"); // returns 2.0   
str_to_float("+7"); // returns 7.0   
str_to_float("+"); // returns 0.0   
str_to_float("089.1.3"); // returns 89.1   
str_to_float("-.2gaben1"); // returns -0.2   
str_to_float("gab2"); // returns 0.0   
  `   

