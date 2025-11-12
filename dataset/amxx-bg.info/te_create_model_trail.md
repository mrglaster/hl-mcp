# te_create_model_trail
#### Syntax
```
stock te_create_model_trail(startpos[3], endpos[3], sprite, count = 1, life = 10, scale = 10, velocity = 10, randomness = 10, receiver = 0, bool:reliable = true)
```

#### Usage
startpos | ```Starting position of the effect```
---|---
endpos | ```Ending position of the effect```
sprite | ```Sprite index```
count | ```Number of models/sprites to generate```
life | ```The length of time the effect shall remain```
scale | ```Scale of the effect```
velocity | ```Velocity along vector```
randomness | ```Randomness of the velocity```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a line of moving glow sprites or models with gravity, fadeout,
and collisions.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=2m58s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.