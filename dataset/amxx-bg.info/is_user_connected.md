# is_user_connected
#### Syntax
```
native is_user_connected(index);
```

#### Usage
index | ```Client index```
---|---
#### Description
```
Returns if the client is connected.
```

#### Note
```
This does not throw an error if the provided index is out of the
1 to MaxClients range. That means you can safely use this native
without manually verifying that the index is a valid client index.
```

#### Return
```
1 if client is connected, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

