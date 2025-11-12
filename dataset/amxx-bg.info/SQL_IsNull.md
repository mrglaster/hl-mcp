# SQL_IsNull
#### Syntax
```
native SQL_IsNull(Handle:query, column);
```

#### Usage
query | ```Handle of a query to check.```
---|---
column | ```Which column to check for NULL.```
#### Description
```
Tells whether a specific column in the current row is NULL or not.
```

#### Return
```
1 if the column is NULL, 0 otherwise.
```

#### Error
```
Invalid query handle.
No result set in this query.
Invalid column.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

