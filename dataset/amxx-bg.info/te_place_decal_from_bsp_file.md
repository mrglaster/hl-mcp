# te_place_decal_from_bsp_file
#### Syntax
```
stock te_place_decal_from_bsp_file(position[3], texture, entity = 0, entabove = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the decal (center of texture in world)```
---|---
texture | ```Texture index of precached decal texture name```
entity | ```Entity index or 0 for world```
entabove | ```Model index of the entity above (only available if the "entity" argument is non-zero)```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Places a decal from the .BSP file.
```

#### Note
```
Using a decal index that doesn't exist will crash the client.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=2m30s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.