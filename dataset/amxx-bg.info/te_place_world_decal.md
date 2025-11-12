# te_place_world_decal
#### Syntax
```
stock te_place_world_decal(position[3], texture, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Decal position (center of texture in world)```
---|---
texture | ```Texture index of precached decal texture name (0 - 511)```
receiver | ```Client index that will be able to see the decal or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Applies a decal to the world brush.
```

#### Note
```
Using a decal index that doesn't exist will crash the client.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=9m56s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.