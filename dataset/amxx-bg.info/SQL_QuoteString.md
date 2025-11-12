# SQL_QuoteString
#### Syntax
```
native SQL_QuoteString(Handle:db, buffer[], buflen, const string[]);
```

#### Usage
db | ```Database handle for localization, or Empty_Handle for when a handle is not available.```
---|---
buffer | ```Buffer to copy to.```
buflen | ```Maximum size of the buffer.```
string | ```String to backquote (should not overlap buffer).```
#### Description
```
Back-quotes characters in a string for database querying.
```

#### Note
```
The buffer's maximum size should be 2*strlen(string) to catch all scenarios.
```

#### Return
```
Length of new string, or -1 on failure.
```

#### Error
```
Invalid database handle.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

