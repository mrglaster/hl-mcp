# te_draw_line
#### Syntax
```
stock te_draw_line(startpos[3], endpos[3], life = 10, r = 0, g = 0, b = 255, receiver = 0, bool:reliable = true)
```

#### Usage
startpos | ```Starting position of the line```
---|---
endpos | ```Ending position of the line```
life | ```Line life```
r | ```Red color amount (0 - 255)```
g | ```Green color amount (0 - 255)```
b | ```Blue color amount (0 - 255)```
receiver | ```Client index that will be able to see the line or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Draws a simple line.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=6m32s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.