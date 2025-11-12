bi_free_result
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_free_result - Frees the memory used by a result handle. 
Syntax
dbi_free_result ( &Result:result ) 
Type
Native 
Notes
If you do not use this after a dbi_query() that returns a result handle, you risk having memory leaks!
