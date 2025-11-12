# get_user_time
#### Syntax
```
native get_user_time(index, flag = 0);
```

#### Usage
index | ```Client index```
---|---
flag | ```If nonzero, the result will not include the time it took the client to connect.```
#### Description
```
Returns client's playing time in seconds.
```

#### Return
```
Connection time in seconds, 0 if client index is invalid or
client is not connected
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

