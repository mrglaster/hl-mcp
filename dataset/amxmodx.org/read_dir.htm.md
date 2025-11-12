ead_dir
[Core](http://127.0.0.1:8000/content/index.htm) (file.inc) 
Description
read_dir - Reads content from a directory. 
Syntax
read_dir ( const dirname[], pos, output[], len, &outLen ) 
Type
Native 
Notes
Returns index of next element or 0 when the end of the directory is reached.   
  
This function has been deprecated because it is very slow. The correct usage of this function is to not advance pos, but to set pos equal to the return value. Since most users did not do this, a more optimized version is now recommended. See [open_dir](http://127.0.0.1:8000/content/open_dir.htm).
