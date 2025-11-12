# get_user_team
#### Syntax
```
native get_user_team(index, team[] = "", len = 0);
```

#### Usage
index | ```Client index```
---|---
team | ```Buffer to copy team name to```
len | ```Maximum size of buffer```
#### Description
```
Returns the team id of the client, and optionally retrieves the name of
the team.
```

#### Return
```
Team index on success, -1 if client index is invalid or
the client is not connected
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

