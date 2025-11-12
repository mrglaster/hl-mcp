# te_create_explosion
#### Syntax
```
stock te_create_explosion(position[3], sprite, scale = 10, framerate = 30, flags = TE_EXPLFLAG_NONE, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the explosion```
---|---
sprite | ```The additive sprite index to use in the explosion```
scale | ```The scale of the sprite in the explosion (0 - 255)```
framerate | ```The frame rate to show the sprite at (0 - 255)```
flags | ```Explosion flags:   TE_EXPLFLAG_NONE               - default Half-Life explosion   TE_EXPLFLAG_NOADDITIVE         - sprite will be drawn opaque   TE_EXPLFLAG_NODLIGHTS          - don't render the dynamic lights   TE_EXPLFLAG_NOSOUND            - don't play the explosion sound   TE_EXPLFLAG_NOPARTICLES        - don't draw the particles```
receiver | ```Client index that will be able to see the explosion or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates an explosion.
```

#### Note
```
A common sprite to use is "sprites/zerogxplode.spr"
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=43s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.