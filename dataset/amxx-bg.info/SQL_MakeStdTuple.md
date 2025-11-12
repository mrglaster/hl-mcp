# SQL_MakeStdTuple
#### Syntax
```
stock Handle:SQL_MakeStdTuple(timeout = 0)
```

#### Usage
timeout | ```Specifies how long connections should wait before giving up. If 0, the value is read from "amx_sql_timeout" cvar.```
---|---
#### Description
```
Use this for making a standard DB Tuple, using AMXX's database info cvars.
```

#### Return
```
A newly created tuple handle to be used in connection routines.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

