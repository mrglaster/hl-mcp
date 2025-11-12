# is_user_alive
#### Syntax
```
native is_user_alive(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if the client is alive.
```

#### Note
```
This will never return true if a client is not connected. If you need
to know whether a client is alive, an additional call to
is_user_connected() is unnecessary.
```

#### Return
```
1 if client is alive, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

