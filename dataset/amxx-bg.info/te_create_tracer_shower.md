# te_create_tracer_shower
#### Syntax
```
stock te_create_tracer_shower(position[3], direction[3] = {0, 0, 0}, color = 12, count = 1, speed = 0, velocity = 10, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the effect```
---|---
direction | ```Effect direction```
color | ```Effect color (https://wiki.alliedmods.net/images/Palette.png)```
count | ```Number of tracers to create```
speed | ```The scroll speed of the effect```
velocity | ```Random velocity```
receiver | ```Client index that will be able to see the tracers or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates an oriented shower of tracers.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=5m34s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.