bi_query
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_query - Executes a query on an SQL resource handle. 
Syntax
dbi_query ( Sql:sql, query[], [ ... ] ) 
Type
Native 
Notes
Return type is Result, which means you have to declare your variable as Result:name, just as you declare a float as Float:name.   
  
Query can be formatted according to [format](http://127.0.0.1:8000/core/format.htm).   
  
**IMPORTANT**   
If the query FAILS, it will return a negative number.   
If the query SUCCEEDS, it will return 0.   
If the query SUCCEEDS and has a result set, it will return a result handle which is greater than 0.   
  
This is not backwards compatible with the old MySQL handlers. This is invalid:   
if (dbi_query(query)
