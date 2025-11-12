# te_spray_blood
#### Syntax
```
stock te_spray_blood(position[3], direction[3] = {0, 0, 0}, color = 78, speed = 30, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position from where the blood will be sprayed```
---|---
direction | ```Blood spraying direction```
color | ```Blood color (https://wiki.alliedmods.net/images/Palette.png)```
speed | ```Speed at which the blood particles will be sprayed (0 - 255)```
receiver | ```Client index that will be able to see the particles or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Sprays blood particles from a given point.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=7m59s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.