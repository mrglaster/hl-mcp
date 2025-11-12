# te_create_particle_burst
#### Syntax
```
stock te_create_particle_burst(position[3], radius = 30, color = 106, duration = 5, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
radius | ```Effect radius```
color | ```Particle color (https://wiki.alliedmods.net/images/Palette.png)```
duration | ```Duration of the effect (will be randomized a bit) (0 - 255)```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a particle burst similar to te_create_lava_splash.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=10m55s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.