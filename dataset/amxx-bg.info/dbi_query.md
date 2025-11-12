# dbi_query
#### Syntax
```
native Result:dbi_query(Sql:_sql, _query[], any:...);
```

#### Description
```
This will do a simple query execution on the SQL server.
If it fails, it will return a number BELOW ZERO (0)
If zero, it succeeded with NO RETURN RESULT.
If greater than zero, make sure to call dbi_free_result() on it!
 The return is a handle to the result set
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

