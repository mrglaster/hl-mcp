pen_dir
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
open_dir - Opens a directory for reading. 
Syntax
open_dir ( dir[], buffer[], length ) 
Type
Native 
Notes
Returns a handle to read the directory. Stores the first file found in the buffer.   
  
Returns 0 on failure. If successful, you must call [close_dir](http://127.0.0.1:8000/content/close_dir.htm) on the handle when done.
