# parse_loguser
#### Syntax
```
native parse_loguser(const text[], name[], nlen, &userid =-2, authid[] = "", alen = 0, team[] = "", tlen = 0);
```

#### Usage
text | ```String to process```
---|---
name | ```Buffer to copy client name to```
nlen | ```Maximum name buffer size```
userid | ```Variable to store userid in```
authid | ```Buffer to copy client authid to```
alen | ```Maximum auth buffer size```
team | ```Buffer to copy client team to```
tlen | ```Maximum team buffer size```
#### Description
```
Parse log data about client.
```

#### Note
```
When client actions are logged, they appear in the the format
"Name<#userid><SteamID><teamname>", this native extracts the individual
pieces of information.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the provided string is not valid client log data, an
error will be thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

