# te_create_tracer
#### Syntax
```
stock te_create_tracer(startpos[3], endpos[3], receiver = 0, bool:reliable = true)
```

#### Usage
startpos | ```Starting position of the tracer```
---|---
endpos | ```Ending position of the tracer```
receiver | ```Client index that will be able to see the tracer or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a tracer effect from one point to another.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=1m12s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.