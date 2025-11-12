# get_user_armor
#### Syntax
```
native get_user_armor(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the client's armor value.
```

#### Note
```
While this is mod-independent, the mod may track armor data differently,
so it can only be retrieved using another native or other methods.
```

#### Return
```
Amount of armor the client has. Also returns 0 if the client
is not connected or the index is not within the range of
1 to MaxClients
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

