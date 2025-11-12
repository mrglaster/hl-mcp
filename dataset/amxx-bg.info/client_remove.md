# client_remove
#### Syntax
```
forward client_remove(id, bool:drop, const message[]);
```

#### Usage
id | ```Client index```
---|---
drop | ```If true, the game has explicitly dropped the client```
message | ```If drop is true, contains the disconnect info message```
#### Description
```
Called when a client entity has been removed from the server.
```

#### Note
```
This fires after the client_disconnected() forward, when the player entity has been
removed (e.g. is_user_connected(id) will return false).
```

#### Return
```
This forward ignores the return value.
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

