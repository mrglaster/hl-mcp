# SQL_FreeHandle
#### Syntax
```
native SQL_FreeHandle(Handle:h);
```

#### Usage
h | ```Handle to be freed.```
---|---
#### Description
```
Frees an SQL handle.
```

#### Note
```
The handle can be to anything (tuple, connection, query, results, etc).
```

#### Note
```
If you free the database connection handle, it closes the connection as well.
```

#### Return
```
This function has no return value.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

