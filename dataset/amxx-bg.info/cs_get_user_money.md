# cs_get_user_money
#### Syntax
```
native cs_get_user_money(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the client's amount of money.
```

#### Return
```
Amount of money
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).