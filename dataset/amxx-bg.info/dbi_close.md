# dbi_close
#### Syntax
```
native dbi_close(&Sql:_sql);
```

#### Description
```
Closes a database handle.  Internally, it will also
mark the handle as free, so this particular handle may
be re-used in the future to save time.
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

