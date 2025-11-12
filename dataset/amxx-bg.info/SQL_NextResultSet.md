# SQL_NextResultSet
#### Syntax
```
native bool:SQL_NextResultSet(Handle:query);
```

#### Usage
query | ```Query Handle.```
---|---
#### Description
```
For queries which return multiple result sets, this advances to the next
result set if one is available.  Otherwise, the current result set is
destroyed and will no longer be accessible.
```

#### Note
```
This function will always return false on SQLite, and when using threaded
queries in MySQL.  Nonetheless, it has the same effect of removing the last
result set.
```

#### Return
```
True on success, false on failure.
```

#### Error
```
Invalid query handle.
No result set in this query.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

