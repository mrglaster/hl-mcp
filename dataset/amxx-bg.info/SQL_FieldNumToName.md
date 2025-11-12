# SQL_FieldNumToName
#### Syntax
```
native SQL_FieldNumToName(Handle:query, num, name[], maxlength);
```

#### Usage
query | ```Handle of a query.```
---|---
num | ```The number (index) of a column to retrieve the name from.```
name | ```Buffer where to store the column's name.```
maxlength | ```Maximum length of the output buffer.```
#### Description
```
Retrieves the name of a column by its index.
```

#### Return
```
This function has no return value.
```

#### Error
```
Invalid query handle.
No result set in this query.
Invalid column index.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

