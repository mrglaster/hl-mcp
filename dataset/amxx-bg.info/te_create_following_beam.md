# te_create_following_beam
#### Syntax
```
stock te_create_following_beam(entity, sprite, life = 10, width = 10, r = 0, g = 0, b = 255, a = 75, receiver = 0, bool:reliable = true)
```

#### Usage
entity | ```Entity that the beam will follow```
---|---
sprite | ```The sprite index to use in the beam```
life | ```The length of time the beam shall remain (0 - 255)```
width | ```The width of the beam (0 - 255)```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
a | ```Beam brightness (alpha) (0 - 255)```
receiver | ```Client index that will be able to see the beam or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a decaying beam that follows the entity until it stops moving.
```

#### Note
```
A common sprite to use is "sprites/laserbeam.spr"
```

#### Note
```
When the entity stops moving, the beam will become visible again
once the entity starts moving.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=4m31s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.