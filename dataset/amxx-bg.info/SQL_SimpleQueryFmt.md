# SQL_SimpleQueryFmt
#### Syntax
```
stock SQL_SimpleQueryFmt(Handle:db, error[]="", maxlength=0, &rows=0, const fmt[], any:...)
```

#### Usage
db | ```Connection handle returned from SQL_Connect().```
---|---
error | ```If an error occurs, it will be placed into this buffer.```
maxlength | ```The maximum length of the error buffer.```
rows | ```Optional. If put, retrieves the number of rows the query returned.```
fmt | ```The query string that can be formated with format specifiers.```
... | ```Additional arguments for formating the query.```
#### Description
```
Use this for executing a query where you don't care about the result.
```

#### Note
```
Differs from SQL_SimpleQuery() because the query can be formated.
```

#### Return
```
1 on success, 0 on failure.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

