bi_nextrow
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_nextrow - Advances the row pointer for an SQL result handle. 
Syntax
dbi_nextrow ( Result:result ) 
Type
Native 
Notes
Unlike the AMX Mod SQL interfaces, you pass a result handle instead of an SQL handle.   
  
For backwards compatibility, if nothing is specifed, it will default to a global pointer.   
  
Returns 0 on failure or end of result list.
