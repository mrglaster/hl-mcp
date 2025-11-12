# SQL_Connect
#### Syntax
```
native Handle:SQL_Connect(Handle:cn_tuple, &errcode, error[], maxlength);
```

#### Usage
cn_tuple | ```Tuple handle, returned from SQL_MakeDbTuple().```
---|---
errcode | ```An error code set by reference.```
error | ```String where error string will be stored.```
maxlength | ```Maximum length of the error buffer.```
#### Description
```
Opens a database connection.
```

#### Return
```
Returns an SQL connection handle, which must be freed.
Returns Empty_Handle on failure.
```

#### Error
```
Invalid info tuple handle.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

