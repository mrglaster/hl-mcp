# SQL_SimpleQuery
#### Syntax
```
stock SQL_SimpleQuery(Handle:db, const query[], error[]="", maxlength=0, &rows=0)
```

#### Usage
db | ```Connection handle returned from SQL_Connect().```
---|---
query | ```The query string.```
error | ```If an error occurs, it will be placed into this buffer.```
maxlength | ```Maximum length of the error buffer.```
rows | ```Optional. If put, retrieves the number of rows the query returned.```
#### Description
```
Use this for executing a query where you don't care about the result.
```

#### Return
```
1 on success, 0 on failure.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

