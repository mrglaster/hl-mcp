# rg_hint_message
#### Syntax
```
native bool:rg_hint_message(const index, const message[], Float:duration = 6.0, bool:bDisplayIfPlayerDead = false, bool:bOverride = false);
```

#### Usage
index | ```Client index```
---|---
message | ```The message hint```
duration | ```The time duration in seconds stays on screen```
bDisplayIfPlayerDead | ```Whether to print hint for dead players?```
bOverride | ```Whether to override previous messages?```
#### Description
```
Adds hint message to the queue.
```

#### Return
```
true if prints, false otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.