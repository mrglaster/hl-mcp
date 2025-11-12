# SQL_PrepareQuery
#### Syntax
```
native Handle:SQL_PrepareQuery(Handle:db, const fmt[], any:...);
```

#### Usage
db | ```Connection handle, returned from SQL_Connect().```
---|---
fmt | ```Query string. Can be formated with format specifiers.```
... | ```Additional format specifiers used to format the query.```
#### Description
```
Prepares a query.
```

#### Note
```
This does not actually do a query!
```

#### Return
```
Returns an SQL query handle, which must always be freed.
Returns Empty_Handle on failure.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

