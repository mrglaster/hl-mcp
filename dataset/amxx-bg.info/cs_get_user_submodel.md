# cs_get_user_submodel
#### Syntax
```
native cs_get_user_submodel(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if a submodel is set on the client.
```

#### Note
```
In Counter-Strike the submodel setting determines whether the user has
a bomb backpack (if a Terrorist) or a defuse kit (if a CT) on their
model.
```

#### Return
```
1 if submodel is set, 0 otherwise
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).