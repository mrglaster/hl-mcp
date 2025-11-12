# te_emit_sprite_from_player
#### Syntax
```
stock te_emit_sprite_from_player(player, sprite, count = 1, variance = 0, receiver = 0, bool:reliable = true)
```

#### Usage
player | ```Client index to emit the sprites from (can't be 0)```
---|---
sprite | ```Sprite index```
count | ```Number of sprites to generate (0 - 255)```
variance | ```Variance in size (0 = no variance; 10 = 10% variance) (0 - 255)```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Emits sprites or models from a player's bounding box.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=10m39s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.