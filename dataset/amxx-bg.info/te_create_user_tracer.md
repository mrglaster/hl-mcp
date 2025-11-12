# te_create_user_tracer
#### Syntax
```
stock te_create_user_tracer(position[3], velocity[3], life = 1, color = 106, length = 1, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
velocity | ```Effect velocity```
life | ```The length of time the effect shall remain, multiplied by 10 (0 - 255)```
color | ```Tracer color (0 - 12)```
length | ```Length of the tracer (0 - 255)```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a tracer effect and allows more customization than te_create_tracer.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=11m36s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.