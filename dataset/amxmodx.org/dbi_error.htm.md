bi_error
[SQL](http://127.0.0.1:8000/content/index.htm) (dbi.inc) 
Description
dbi_error - Returns an error message set on an SQL connection handle. 
Syntax
dbi_error ( Sql:sql, error[], maxLength ) 
Type
Native 
Notes
For MSSQL, this is the last error found from a thrown exception. For PgSQL and MySQL, it is from the direct API.
