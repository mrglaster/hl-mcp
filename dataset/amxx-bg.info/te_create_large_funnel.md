# te_create_large_funnel
#### Syntax
```
stock te_create_large_funnel(position[3], sprite, flag = LF_FLOAT_DOWN, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Effect position```
---|---
sprite | ```Sprite index to use```
flag | ```List of valid flags:   LF_FLOAT_DOWN           - float downwards and end in the point set in the "position" argument   LF_FLOAT_UP             - start from the point set in the "position" argument and float upwards```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a large group of sprites or models accompanied by green dots
that float up or down until they reach the point set in the "position" argument.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=7m10s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.