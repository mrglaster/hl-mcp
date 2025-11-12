# te_create_bubble_line
#### Syntax
```
stock te_create_bubble_line(startpos[3], endpos[3], sprite, count = 3, randomness = 0, height = 50, receiver = 0, bool:reliable = true)
```

#### Usage
startpos | ```Start position```
---|---
endpos | ```End position```
sprite | ```Sprite index```
count | ```Number of sprites to generate (0 - 255)```
randomness | ```Randoness of the floating direction```
height | ```Float height```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates alpha sprites or models along a line that float upwards.
```

#### Note
```
A common sprite to use is "sprites/bubble.spr"
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=9m37s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.