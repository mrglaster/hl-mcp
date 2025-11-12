# SQL_QueryAndIgnore
#### Syntax
```
stock SQL_QueryAndIgnore(Handle:db, const queryfmt[], any:...)
```

#### Usage
db | ```A connection handle returned from SQL_Connect().```
---|---
queryfmt | ```The query string that can be formated with format specifiers.```
#### Description
```
Use this for executing a query and not caring about the error.
```

#### Pram
```
...            Additional arguments for formating the query.
```

#### Return
```
1 on error.
>= 0 on success (with the number of affected rows).
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

