# SQL_SetCharset
#### Syntax
```
native bool:SQL_SetCharset(Handle:h, const charset[]);
```

#### Usage
h | ```Database or connection tuple Handle.```
---|---
charset | ```The character set string to change to.```
#### Description
```
Sets the character set of the current connection.
Like SET NAMES .. in mysql, but stays after connection problems.
```

#### Note
```
If a connection tuple is supplied, this should be called before SQL_Connect or SQL_ThreadQuery.
```

#### Note
```
The change will remain until you call this function with another value.
```

#### Note
```
This native does nothing in SQLite.

Example: "utf8", "latin1"
```

#### Return
```
True, if character set was changed, false otherwise.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

