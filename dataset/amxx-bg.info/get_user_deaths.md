# get_user_deaths
#### Syntax
```
native get_user_deaths(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the client's death count.
```

#### Note
```
While this is mod-independent, the mod may track death count differently,
so it can only be retrieved using another native or other methods.
```

#### Return
```
Amount of deaths the client has. Also returns 0 if the
client is not connected or the index is not within the range
of 1 to MaxClients
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

