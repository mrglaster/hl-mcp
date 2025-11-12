og_error
[Core](http://127.0.0.1:8000/content/index.htm) (amxmodx.inc) 
Description
log_error - Logs an error from a dynamic native. 
Syntax
log_error ( error, const fmt[], [ ... ] ) 
Type
Native 
Notes
You can only use this in a function registered as a dynamic native.   
  
It will log the error as if the plugin using your native was faulty. This function also forces a backtrace output for the parent plugin (the debugger).   
  
A list of error codes are available in amxconst.inc.
