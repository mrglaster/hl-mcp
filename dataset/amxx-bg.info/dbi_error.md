# dbi_error
#### Syntax
```
native dbi_error(Sql:_sql, _error[], _len);
```

#### Description
```
Returns an error message set.  For PGSQL and MySQL,
this is a direct error return from the database handle/API.
For MSSQL, it returns the last error message found from a
thrown exception.
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

