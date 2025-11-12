# dbi_connect
#### Syntax
```
native Sql:dbi_connect(_host[], _user[], _pass[], _dbname[], _error[]="", _maxlength=0);
```

#### Description
```
This will return a number equal to or below 0 on failure.
If it does fail, the error will be mirrored in dbi_error()
The return value will otherwise be a resource handle, not an
OK code or cell pointer.
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

