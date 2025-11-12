# client_disconnected
#### Syntax
```
forward client_disconnected(id, bool:drop, message[], maxlen);
```

#### Usage
id | ```Client index```
---|---
drop | ```If true, the game has explicitly dropped the client```
message | ```If drop is true, a writable buffer containing the disconnect info message```
maxlen | ```Maximum size of buffer```
#### Description
```
Called when a client is disconnected from the server.
```

#### Note
```
This will be called in some additional cases that client_disconnect doesn't cover,
most notably when a client aborts the connection process. It is guaranteed to pair
with the client_connect() forward.
```

#### Note
```
When this fires the player entity is still valid (e.g. is_user_connected(id) will
return true), but no networked commands will reach the client.
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

