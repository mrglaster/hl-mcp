# get_user_ping
#### Syntax
```
native get_user_ping(index, &ping, &loss);
```

#### Usage
index | ```Client index```
---|---
ping | ```Variable to store ping in```
loss | ```Variable to store loss in```
#### Description
```
Retrieves the ping and loss of a client.
```

#### Return
```
1 on success, 0 if client index is invalid or the client
is not connected
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

