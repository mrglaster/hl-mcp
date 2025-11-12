# te_create_entity_light
#### Syntax
```
stock te_create_entity_light(entity, position[3] = {0, 0, 0}, radius = 50, r = 255, g = 255, b = 255, life = 10, decay = 10, receiver = 0, bool:reliable = true)
```

#### Usage
entity | ```Entity or client to apply the light on```
---|---
position | ```Position of the light```
radius | ```Light radius```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
life | ```The length of time the light shall remain (0 - 255)```
decay | ```Light decay rate```
receiver | ```Client index that will be able to see the light or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a point entity light with no world effect.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=6m7s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.