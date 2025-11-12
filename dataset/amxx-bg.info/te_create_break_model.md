# te_create_break_model
#### Syntax
```
stock te_create_break_model(position[3], modelid, size[3] = {50, 50, 50}, velocity[3] = {0, 0, 0}, random = 0, count = 1, life = 10, flags = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the model```
---|---
size | ```Size of the model```
velocity | ```Model velocity```
modelid | ```Model index```
random | ```Random velocity (0 - 255)```
count | ```Number of model pieces to generate (0 - 255)```
life | ```The length of time the model shall remain (0 - 255)```
flags | ```Break model flags:   BreakModel_TypeMask   BreakModel_Glass   BreakModel_Metal   BreakModel_Flesh   BreakModel_Wood   BreakModel_Smoke   BreakModel_Trans   BreakModel_Concrete   BreakModel_2```
receiver | ```Client index that will be able to see the model or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a model or sprite entity that slowly disappears until it's gone.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.