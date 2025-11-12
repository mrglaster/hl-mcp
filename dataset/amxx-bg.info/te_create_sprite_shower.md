# te_create_sprite_shower
#### Syntax
```
stock te_create_sprite_shower(position[3], model, direction[3] = {0, 0, 0}, count = 1, speed = 0, noise = 0, rendermode = kRenderNormal, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
model | ```Model index that will be used for the effect```
direction | ```Effect direction```
count | ```Number of sprites/models to generate (0 - 255)```
speed | ```The scroll speed of the effect (0 - 255)```
noise | ```The noise amplitude of the effect - this controls the distorsion of the effect (0 - 255)```
rendermode | ```Render mode - one of kRender* constants```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a shower of sprites or models.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=10m27s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.