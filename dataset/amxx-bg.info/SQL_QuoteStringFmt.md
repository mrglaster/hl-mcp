# SQL_QuoteStringFmt
#### Syntax
```
native SQL_QuoteStringFmt(Handle:db, buffer[], buflen, const fmt[], any:...);
```

#### Usage
db | ```Database handle for localization, or Empty_Handle for when a handle is not available.```
---|---
buffer | ```Buffer to copy to.```
buflen | ```Maximum size of the buffer.```
fmt | ```Format of string to backquote (should not overlap buffer).```
... | ```Format arguments.```
#### Description
```
Back-quotes characters in a string for database querying.
Note: The buffer's maximum size should be 2*strlen(string) to catch
all scenarios.
```

#### Return
```
Length of new string, or -1 on failure.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

