ead_data
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
read_data - Gets arguments/values from client messages. 
Syntax
read_data ( value, [ ... ] ) 
Type
Native 
Notes
To get an array/string:   
` new string[32]   
read_data(argument, string, 31)  `   
  
To get a float:   
` new Float:fVal   
read_data(argument, fVal)  `   
  
To get an integer:   
` read_data(argument)  `
