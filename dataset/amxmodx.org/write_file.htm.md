rite_file
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
write_file - Writes a line to a file. 
Syntax
write_file ( const file[], const text[], [ line ] ) 
Type
Native 
Notes
Returns 0 on failure.   
  
The line parameter defaults to -1, which appends to the end of the file. Otherwise, a specific line is overwritten.
