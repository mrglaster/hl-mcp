# SQL_MakeDbTuple
#### Syntax
```
native Handle:SQL_MakeDbTuple(const host[], const user[], const pass[], const db[], timeout=0);
```

#### Usage
host | ```Database host```
---|---
user | ```Database user```
pass | ```Database password```
db | ```Database name to use```
timeout | ```Specifies how long connections should wait before giving up. If <= 0, the default of 60s is used.```
#### Description
```
Creates a connection information tuple. This tuple must be passed
into connection routines.
```

#### Note
```
Freeing the tuple is not necessary, but is a good idea if you create
many of them. You can cache these handles globally.
```

#### Note
```
This does not connect to the DB; it only caches the connection information.
```

#### Return
```
A newly created tuple handle to be used in connection routines.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

