# set_user_info
#### Syntax
```
native set_user_info(index, const info[], const value[]);
```

#### Usage
index | ```Client index```
---|---
info | ```Info key```
value | ```New value```
#### Description
```
Sets info on the client.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the index is not within the range of 1 to MaxClients or
the client is not connected, an error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

