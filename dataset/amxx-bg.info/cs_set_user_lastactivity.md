# cs_set_user_lastactivity
#### Syntax
```
native cs_set_user_lastactivity(index, Float:value);
```

#### Usage
index | ```Client index```
---|---
value | ```New last activity time```
#### Description
```
Sets the client's last activity time.
```

#### Note
```
This is the time that the internal Counter-Strike afk kicker uses to
see who has been inactive too long.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).