# SQL_Execute
#### Syntax
```
native SQL_Execute(Handle:query);
```

#### Usage
query | ```Handle of a prepared query to be executed.```
---|---
#### Description
```
Executes an already prepared query.
```

#### Note
```
You can call this multiple times as long as its parent connection is kept open.
Each time the result set from the previous call will be freed.
```

#### Return
```
1 if the query succeeded, 0 if the query failed.
```

#### Error
```
Invalid query handle.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

