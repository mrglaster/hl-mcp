# SQL_FieldNameToNum
#### Syntax
```
native SQL_FieldNameToNum(Handle:query, const name[]);
```

#### Usage
query | ```Handle of a query.```
---|---
name | ```Name to search for.```
#### Description
```
Retrieves the number of a named column.
```

#### Return
```
Column index if found (>= 0); -1 otherwise.
```

#### Error
```
Invalid query handle.
No result set in this query.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

