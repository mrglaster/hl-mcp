# client_changeteam
#### Syntax
```
forward client_changeteam(id, newteam, oldteam);
```

#### Usage
id | ```The id of the client.```
---|---
newteam | ```The team number of the new team.```
oldteam | ```The team number of the old team.```
#### Description
```
Triggered whenever a client's pev->team changes.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of ns.inc. To use this code you should include ns.inc as ```#include <ns>```


  
  

Warning: This include is compatible only with Natural Selection and will not function with other mods (e.g., Valve, Counter Strike 1.6, etc.).