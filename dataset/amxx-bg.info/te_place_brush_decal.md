# te_place_brush_decal
#### Syntax
```
stock te_place_brush_decal(position[3], texture, entity = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the decal (center of texture in world)```
---|---
texture | ```Texture index of precached decal texture name (0 - 511)```
entity | ```Entity index to apply the decal to```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Applies a decal to a brush entity (not the world).
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=8m12s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.