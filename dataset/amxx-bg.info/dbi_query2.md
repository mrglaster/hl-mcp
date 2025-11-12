# dbi_query2
#### Syntax
```
native Result:dbi_query2(Sql:_sql, &rows, _query[], any:...);
```

#### Description
```
Has the same usage as dbi_query, but this native returns by
reference the number of rows affected in the query. If the
query fails rows will be equal to -1.
```


This code is a part of dbi.inc. To use this code you should include dbi.inc as ```#include <dbi>```


  
  

