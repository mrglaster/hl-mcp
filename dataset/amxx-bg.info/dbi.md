# Functions in dbi.inc
Function | Description  
---|---  
[dbi_connect](https://amxx-bg.info/api/dbi/dbi_connect) | ```
This will return a number equal to or below 0 on failure.
If it does fail, the error will be mirrored in dbi_error()
The return value will otherwise be a resource handle, not an
OK code or cell pointer.
```
  
[dbi_query](https://amxx-bg.info/api/dbi/dbi_query) | ```
This will do a simple query execution on the SQL server.
If it fails, it will return a number BELOW ZERO (0)
If zero, it succeeded with NO RETURN RESULT.
If greater than zero, make sure to call dbi_free_result() on it!
 The return is a handle to the result set
```
  
[dbi_query2](https://amxx-bg.info/api/dbi/dbi_query2) | ```
Has the same usage as dbi_query, but this native returns by
reference the number of rows affected in the query. If the
query fails rows will be equal to -1.
```
  
[dbi_nextrow](https://amxx-bg.info/api/dbi/dbi_nextrow) | ```
Returns 0 on failure or End of Results.
Advances result pointer by one row.
```
  
[dbi_field](https://amxx-bg.info/api/dbi/dbi_field) | ```
Gets a field by number.  Returns 0 on failure.
Although internally fields always start from 0,
This function takes fieldnum starting from 1.
No extra params: returns int
One extra param: returns Float: byref
Two extra param: Stores string with length
```
  
[dbi_result](https://amxx-bg.info/api/dbi/dbi_result) | ```
Gets a field by name.  Returns 0 on failure.
One extra param: returns Float: byref
Two extra param: Stores string with length
```
  
[dbi_num_rows](https://amxx-bg.info/api/dbi/dbi_num_rows) | ```
Returns the number of rows returned from a query
```
  
[dbi_free_result](https://amxx-bg.info/api/dbi/dbi_free_result) | ```
Frees memory used by a result handle.  Do this or get memory leaks.
```
  
[dbi_close](https://amxx-bg.info/api/dbi/dbi_close) | ```
Closes a database handle.  Internally, it will also
mark the handle as free, so this particular handle may
be re-used in the future to save time.
```
  
[dbi_error](https://amxx-bg.info/api/dbi/dbi_error) | ```
Returns an error message set.  For PGSQL and MySQL,
this is a direct error return from the database handle/API.
For MSSQL, it returns the last error message found from a
thrown exception.
```
  
[dbi_type](https://amxx-bg.info/api/dbi/dbi_type) | ```
Returns the type of database being used.  So far:
"mysql", "pgsql", "mssql", "sqlite"
```
  
[dbi_num_fields](https://amxx-bg.info/api/dbi/dbi_num_fields) | ```
Returns the number of fields/colums in a result set.
Unlike dbi_nextrow, you must pass a valid result handle.
```
  
[dbi_field_name](https://amxx-bg.info/api/dbi/dbi_field_name) | ```
Retrieves the name of a field/column in a result set.
Requires a valid result handle, and columns are numbered 1 to n.
```
  
[sqlite_table_exists](https://amxx-bg.info/api/dbi/sqlite_table_exists) | ```
This function can be used to find out if a table in a Sqlite database exists.
```
  

This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

