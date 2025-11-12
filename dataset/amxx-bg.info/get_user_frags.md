# get_user_frags
#### Syntax
```
native get_user_frags(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns the client's frags.
```

#### Note
```
While this is mod-independent, the mod may track frag count differently,
so it can only be retrieved using another native or other methods.
```

#### Note
```
This will actually return the client's overall score, which may or may
not be equal to their scored frags depending on the mod.
```

#### Return
```
Frags/Score of the client. Also returns 0 if the client is
not connected or the index is not within the range of
1 to MaxClients
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

