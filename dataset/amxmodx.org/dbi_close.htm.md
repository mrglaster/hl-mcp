bi_close
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_close - Closes a database connection handle. 
Syntax
dbi_close ( &Sql:sql ) 
Type
Native 
Notes
Internally, it will also mark the handle as free, so this particular handle may be re-used in the future to save time.
