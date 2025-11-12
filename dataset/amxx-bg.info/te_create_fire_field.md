# te_create_fire_field
#### Syntax
```
stock te_create_fire_field(position[3], sprite, radius = 5, count = 1, duration = 10, flags = TEFIRE_FLAG_ALLFLOAT, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
sprite | ```Sprite or model index to use for the fire```
radius | ```Effect radius```
count | ```Number of fields to generate (0 - 255)```
duration | ```Duration of the effect (will be randomized a bit) (0 - 255)```
flags | ```Available flags:   TEFIRE_FLAG_ALLFLOAT    - all sprites will drift upwards as they animate   TEFIRE_FLAG_SOMEFLOAT   - some of the sprites will drift upwards (50% chance)   TEFIRE_FLAG_LOOP        - if set, sprite plays at 15 fps, otherwise plays at whatever rate stretches the animation over the sprite's duration   TEFIRE_FLAG_ALPHA       - if set, sprite is rendered alpha blended at 50% else, opaque   TEFIRE_FLAG_PLANAR      - if set, all fire sprites have same initial Z instead of randomly filling a cube```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a field of fire.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=11m7s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.