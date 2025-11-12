# client_connectex
#### Syntax
```
forward client_connectex(id, const name[], const ip[], reason[128]);
```

#### Usage
id | ```Client index```
---|---
name | ```Client name```
ip | ```Client ip address with port```
reason | ```A reason that will be displayed when player gets rejected (can be overwritten)```
#### Description
```
Called when a client is connecting.
```

#### Note
```
This forward is called too early to do anything that directly affects
the client.
```

#### Return
```
PLUGIN_CONTINUE to let a client join to the server
PLUGIN_HANDLED or higher to prevent a client to join
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

