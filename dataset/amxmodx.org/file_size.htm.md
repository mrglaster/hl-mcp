ile_size
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
file_size - Returns the size of a file. 
Syntax
file_size ( const file[], [ flag ] ) 
Type
Native 
Notes
If flag is 0, size is returned in bytes.   
If flag is 1, the number of lines is returned.   
If flag is 2, 1 is returned if the file ends in a line feed.   
If the file doesn't exist, -1 is returned.
