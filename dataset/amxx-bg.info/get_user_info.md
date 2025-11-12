# get_user_info
#### Syntax
```
native get_user_info(index, const info[], output[], len);
```

#### Usage
index | ```Client index```
---|---
info | ```Info key```
output | ```Buffer to copy value to```
len | ```Maximum size of the buffer```
#### Description
```
Gets info from the client.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If the index is not within the range of 1 to MaxClients or
the client is not connected, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

