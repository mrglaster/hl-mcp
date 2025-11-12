# cs_get_user_lastactivity
#### Syntax
```
native Float:cs_get_user_lastactivity(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the client's last activity time.
```

#### Note
```
This is the time that the internal Counter-Strike afk kicker uses to
see who has been inactive too long.
```

#### Return
```
Last activity time
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).