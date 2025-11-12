# SQL_ThreadQuery
#### Syntax
```
native SQL_ThreadQuery(Handle:db_tuple, const handler[], const query[], const data[]="", dataSize=0);
```

#### Usage
db_tuple | ```Tuple handle, returned from SQL_MakeDbTuple().```
---|---
handler | ```A function to be called when the query finishes. It has to be public.```
query | ```The query string.```
data | ```Additional data array that will be passed to the handler function.```
dataSize | ```The size of the additional data array.```
#### Description
```
Prepares and executes a threaded query.
```

#### Note
```
The handler should look like:
public QueryHandler(failstate, Handle:query, error[], errnum, data[], size, Float:queuetime)
failstate - One of the three TQUERY_ defines.
query     - Handle to the query, do not free it.
error     - An error message, if any.
errnum    - An error code, if any.
data      - Data array you passed in.
size      - Size of the data array you passed in.
queuetime - Amount of gametime that passed while the query was resolving.
```

#### Note
```
This will not interrupt gameplay in the event of a poor/lossed
connection, however, the interface is more complicated and
asynchronous. Furthermore, a new connection/disconnection is
made for each query to simplify driver support.
```

#### Note
```
The handle does not need to be freed.
```

#### Return
```
This function has no return value.
```

#### Error
```
Thread worker was unable to start.
Invalid info tuple handle.
Handler function not found.
```


This code is a part of sqlx.inc. To use this code you should include sqlx.inc as ```#include <sqlx>```


  
  

