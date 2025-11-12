# te_create_beam_ring
#### Syntax
```
stock te_create_beam_ring(position[3], sprite, axis[3] = {0, 0, 0}, startframe = 0, framerate = 30, life = 10, width = 10, noise = 0, r = 0, g = 0, b = 255, a = 75, speed = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Starting coordinates of the beam```
---|---
sprite | ```The sprite index to use in the beam```
axis | ```Beam axis```
startframe | ```The frame to start with in the sprite```
framerate | ```The frame rate to show the sprite at```
life | ```The length of time the beam shall remain```
width | ```The width of the beam```
noise | ```The noise amplitude of the beam, this controls the distorsion of the beam```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
a | ```Beam brightness (alpha) (0 - 255)```
speed | ```The scroll speed of the beam (0 - 255)```
receiver | ```Client index that will be able to see the beam or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a screen aligned beam ring that expands to the maximum radius
over lifetime.
```

#### Note
```
A common sprite to use is "sprites/laserbeam.spr"
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=3m40s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.