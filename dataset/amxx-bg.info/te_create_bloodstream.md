# te_create_bloodstream
#### Syntax
```
stock te_create_bloodstream(position[3], direction[3] = {0, 0, 0}, color = 78, count = 1, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Starting position of the blood```
---|---
direction | ```Blood direction```
color | ```Blood color (https://wiki.alliedmods.net/images/Palette.png)```
count | ```Number of blood particles to generate (0 - 255)```
receiver | ```Client index that will be able to see the blood or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates dripping blood particles.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=7m35s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.