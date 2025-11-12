# cs_get_user_model
#### Syntax
```
native cs_get_user_model(index, model[], len);
```

#### Usage
index | ```Client index```
---|---
model | ```Buffer to copy model to```
len | ```Maximum buffer size```
#### Description
```
Retrieves the client's player model.
```

#### Return
```
Number of cells written to buffer
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).