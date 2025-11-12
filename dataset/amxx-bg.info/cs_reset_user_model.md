# cs_reset_user_model
#### Syntax
```
native cs_reset_user_model(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Resets the client's model.
```

#### Note
```
This lifts the model-lock set by a previous cs_set_user_model() call.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).