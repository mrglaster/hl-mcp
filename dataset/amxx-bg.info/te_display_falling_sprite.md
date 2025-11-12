# te_display_falling_sprite
#### Syntax
```
stock te_display_falling_sprite(position[3], sprite1id, sprite2id, color = 78, scale = 10, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
sprite1id | ```Primary sprite index```
sprite2id | ```Secondary sprite index```
color | ```Sprite color (https://wiki.alliedmods.net/images/Palette.png)```
scale | ```Sprite scale (0 - 255)```
receiver | ```Client index that will be able to see the sprite or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates an spray of opaque sprites or models that fall to another sprite or model.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=9m44s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.