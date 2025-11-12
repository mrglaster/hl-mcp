# get_user_msgname
#### Syntax
```
native get_user_msgname(msgid, name[], len);
```

#### Usage
msgid | ```Client message id```
---|---
name | ```Buffer to copy message name to```
len | ```Maximum buffer size```
#### Description
```
Retrieves the client message name from a message id.
```

#### Return
```
Number of cells written to buffer, 0 on invalid message id
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

