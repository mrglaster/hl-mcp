# te_create_smoke
#### Syntax
```
stock te_create_smoke(position[3], sprite, scale = 10, framerate = 30, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the smoke effect```
---|---
sprite | ```The alphablend sprite index to use for the smoke```
scale | ```The scale of the smoke (0 - 255)```
framerate | ```The frame rate to show the sprite at (0 - 255)```
receiver | ```Client index that will be able to see the smoke or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates smoke (a rising alphablend sprite at 30 pps).
```

#### Note
```
A common sprite to use is "sprites/steam1.spr"
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=1m2s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.