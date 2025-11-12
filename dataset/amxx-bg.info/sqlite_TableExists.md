# sqlite_TableExists
#### Syntax
```
stock bool:sqlite_TableExists(Handle:db, const table[])
```

#### Usage
db | ```Connection handle returned from SQL_Connect().```
---|---
table | ```The table name to check for.```
#### Description
```
This function can be used to find out if a table in a SQLite database exists.
```

#### Return
```
True if it exists, false otherwise.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

