# te_place_gunshot_decal
#### Syntax
```
stock te_place_gunshot_decal(position[3], decal = 41, entity = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the decal```
---|---
decal | ```Decal index (0 - 255)```
entity | ```Entity to apply the decal to or 0 for world```
receiver | ```Client index that will be able to see the model or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Places a gunshot decal on an entity or the world and plays a ricochet sound.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=8m41s
```

#### Return
```
This function has no return value.
```

#### Error
```
If "receiver" is non-zero and the client isn't
connected, an error will be thrown.
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.