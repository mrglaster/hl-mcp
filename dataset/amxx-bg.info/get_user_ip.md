# get_user_ip
#### Syntax
```
native get_user_ip(index, ip[], len, without_port = 0);
```

#### Usage
index | ```Client index, use 0 to retrieve the server IP```
---|---
ip | ```Buffer to copy IP to```
len | ```Maximum buffer size```
without_port | ```Remove the port from the IP if nonzero```
#### Description
```
Retrieves the IP of a client or the server.
```

#### Return
```
Number of cells written to the buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

