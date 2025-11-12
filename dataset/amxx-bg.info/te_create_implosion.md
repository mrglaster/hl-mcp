# te_create_implosion
#### Syntax
```
stock te_create_implosion(position[3], radius = 64, count = 10, life = 3, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the implosion effect```
---|---
radius | ```Implosion radius```
count | ```Number of tracers to generate```
life | ```The length of time the effect shall remain```
receiver | ```Client index that will be able to see the effect or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates tracers moving towards a point.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=2m44s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.