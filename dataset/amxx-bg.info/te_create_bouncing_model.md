# te_create_bouncing_model
#### Syntax
```
stock te_create_bouncing_model(position[3], modelid, velocity[3] = {0, 0, 0}, yaw = 0, BounceSounds:bouncesound = BounceSound_Null, life = 10, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the model```
---|---
modelid | ```Model index```
velocity | ```Model velocity```
yaw | ```Initial yaw```
bouncesound | ```Bounce sound type:   BounceSound_Null   BounceSound_Shell   BounceSound_ShotShell```
life | ```The length of time the model shall remain (0 - 255)```
receiver | ```Client index that will be able to see the model or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a moving model or sprite that bounces and makes a sound when it hits.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=8m16s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.