# SQL_GetQueryString
#### Syntax
```
native SQL_GetQueryString(Handle:query, buffer[], maxlength);
```

#### Usage
query | ```Handle of a query.```
---|---
buffer | ```Buffer where to put the query string in.```
maxlength | ```The maximum length of the output buffer.```
#### Description
```
Returns the original query string that a query handle used.
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid query handle.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

