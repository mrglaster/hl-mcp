# SQL_QueryError
#### Syntax
```
native SQL_QueryError(Handle:query, error[], maxlength);
```

#### Usage
query | ```Handle of a query to extract the error from.```
---|---
error | ```Buffer where to store the error string.```
maxlength | ```The maximum length of the output buffer.```
#### Description
```
Gets information about a failed query error.
```

#### Return
```
The error code.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

