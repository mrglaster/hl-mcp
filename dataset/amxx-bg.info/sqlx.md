# Functions in sqlx.inc
Function | Description  
---|---  
[SQL_MakeDbTuple](https://amxx-bg.info/api/sqlx/SQL_MakeDbTuple) | ```
Creates a connection information tuple. This tuple must be passed
into connection routines.
```
  
[SQL_FreeHandle](https://amxx-bg.info/api/sqlx/SQL_FreeHandle) | ```
Frees an SQL handle.
```
  
[SQL_Connect](https://amxx-bg.info/api/sqlx/SQL_Connect) | ```
Opens a database connection.
```
  
[SQL_SetCharset](https://amxx-bg.info/api/sqlx/SQL_SetCharset) | ```
Sets the character set of the current connection.
Like SET NAMES .. in mysql, but stays after connection problems.
```
  
[SQL_PrepareQuery](https://amxx-bg.info/api/sqlx/SQL_PrepareQuery) | ```
Prepares a query.
```
  
[SQL_QuoteString](https://amxx-bg.info/api/sqlx/SQL_QuoteString) | ```
Back-quotes characters in a string for database querying.
```
  
[SQL_QuoteStringFmt](https://amxx-bg.info/api/sqlx/SQL_QuoteStringFmt) | ```
Back-quotes characters in a string for database querying.
Note: The buffer's maximum size should be 2*strlen(string) to catch
all scenarios.
```
  
[SQL_ThreadQuery](https://amxx-bg.info/api/sqlx/SQL_ThreadQuery) | ```
Prepares and executes a threaded query.
```
  
[SQL_Execute](https://amxx-bg.info/api/sqlx/SQL_Execute) | ```
Executes an already prepared query.
```
  
[SQL_QueryError](https://amxx-bg.info/api/sqlx/SQL_QueryError) | ```
Gets information about a failed query error.
```
  
[SQL_MoreResults](https://amxx-bg.info/api/sqlx/SQL_MoreResults) | ```
Checks whether there are more results to be read.
```
  
[SQL_IsNull](https://amxx-bg.info/api/sqlx/SQL_IsNull) | ```
Tells whether a specific column in the current row is NULL or not.
```
  
[SQL_ReadResult](https://amxx-bg.info/api/sqlx/SQL_ReadResult) | ```
Retrieves the current result.
```
  
[SQL_NextRow](https://amxx-bg.info/api/sqlx/SQL_NextRow) | ```
Advances to the next result (row).
```
  
[SQL_AffectedRows](https://amxx-bg.info/api/sqlx/SQL_AffectedRows) | ```
Returns the number of affected rows by a query.
```
  
[SQL_NumResults](https://amxx-bg.info/api/sqlx/SQL_NumResults) | ```
The number of retrieved rows (results) after a query.
```
  
[SQL_NumColumns](https://amxx-bg.info/api/sqlx/SQL_NumColumns) | ```
Returns the total number of columns.
```
  
[SQL_FieldNumToName](https://amxx-bg.info/api/sqlx/SQL_FieldNumToName) | ```
Retrieves the name of a column by its index.
```
  
[SQL_FieldNameToNum](https://amxx-bg.info/api/sqlx/SQL_FieldNameToNum) | ```
Retrieves the number of a named column.
```
  
[SQL_Rewind](https://amxx-bg.info/api/sqlx/SQL_Rewind) | ```
Rewinds a result set to the first row.
```
  
[SQL_GetInsertId](https://amxx-bg.info/api/sqlx/SQL_GetInsertId) | ```
Retrieves the instert ID of the latest INSERT query.
```
  
[SQL_GetAffinity](https://amxx-bg.info/api/sqlx/SQL_GetAffinity) | ```
Retrieves which driver is this plugin currently bound to.
```
  
[SQL_SetAffinity](https://amxx-bg.info/api/sqlx/SQL_SetAffinity) | ```
Sets driver affinity. You can use this to force a particular driver implementation.
This will automatically change all SQL natives in your plugin to be "bound" to
the module in question.
```
  
[SQL_GetQueryString](https://amxx-bg.info/api/sqlx/SQL_GetQueryString) | ```
Returns the original query string that a query handle used.
```
  
[SQL_NextResultSet](https://amxx-bg.info/api/sqlx/SQL_NextResultSet) | ```
For queries which return multiple result sets, this advances to the next
result set if one is available.  Otherwise, the current result set is
destroyed and will no longer be accessible.
```
  
[sqlite_TableExists](https://amxx-bg.info/api/sqlx/sqlite_TableExists) | ```
This function can be used to find out if a table in a SQLite database exists.
```
  
[SQL_SimpleQuery](https://amxx-bg.info/api/sqlx/SQL_SimpleQuery) | ```
Use this for executing a query where you don't care about the result.
```
  
[SQL_SimpleQueryFmt](https://amxx-bg.info/api/sqlx/SQL_SimpleQueryFmt) | ```
Use this for executing a query where you don't care about the result.
```
  
[SQL_QueryAndIgnore](https://amxx-bg.info/api/sqlx/SQL_QueryAndIgnore) | ```
Use this for executing a query and not caring about the error.
```
  
[SQL_MakeStdTuple](https://amxx-bg.info/api/sqlx/SQL_MakeStdTuple) | ```
Use this for making a standard DB Tuple, using AMXX's database info cvars.
```
  

This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

