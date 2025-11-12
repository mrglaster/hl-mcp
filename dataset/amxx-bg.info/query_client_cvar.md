# query_client_cvar
#### Syntax
```
native query_client_cvar(id, const cvar[], const resultFunc[], paramlen = 0, const params[] = "");
```

#### Usage
id | ```Client index```
---|---
cvar | ```Cvar to query```
resultFunc | ```Callback function```
paramlen | ```Size of extra data```
params | ```Extra data to pass through to callback```
#### Description
```
Dispatches a client cvar query, allowing the plugin to query for its value on
the client.
```

#### Note
```
The callback will be called in the following manner:

public cvar_query_callback(id, const cvar[], const value[], const param[])

  id      - Client index
  cvar    - Cvar queried
  value   - Cvar value on the client
  param   - Optional extra data
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, the client is not connected, the callback
function is invalid or the querying process encounters
a problem, an error will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

