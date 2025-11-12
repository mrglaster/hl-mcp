# send_geiger_signal
#### Syntax
```
stock send_geiger_signal(id, distance, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
distance | ```Signal distance```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Sends the geiger signal that notifies the player of nearby radiation level.
```

#### Note
```
This stock isn't available in Day of Defeat.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.