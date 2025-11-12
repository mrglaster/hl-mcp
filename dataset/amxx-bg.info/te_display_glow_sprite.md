# te_display_glow_sprite
#### Syntax
```
stock te_display_glow_sprite(position[3], sprite, scale = 10, size = 10, brightness = 150, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Sprite position```
---|---
sprite | ```Sprite index```
scale | ```Sprite scale (0 - 255)```
size | ```Sprite size (0 - 255)```
brightness | ```Sprite brightness (0 - 255)```
receiver | ```Client index that will be able to see the sprite or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Displays a glowing sprite.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=4m43s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.