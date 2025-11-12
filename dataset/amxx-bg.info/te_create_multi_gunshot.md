# te_create_multi_gunshot
#### Syntax
```
stock te_create_multi_gunshot(position[3], direction[3], decal = 105, count = 1, noise_x = 0, noise_y = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Gunshot position```
---|---
direction | ```Gunshot direction```
decal | ```Bullethole decal texture index (0 - 255)```
count | ```Number of bulletholes to generate (0 - 255)```
noise_x | ```X noise multiplied by 100```
noise_y | ```Y noise multiplied by 100```
receiver | ```Client index that will be able to see the Gunshot or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Much more compact shotgun shot stock.
```

#### Note
```
This stock is used to make a client approximate a 'spray' of gunfire.
Any weapon that fires more than one bullet per frame and fires in a bit
of a spread is a good candidate for MULTIGUNSHOT use. (shotguns)
```

#### Note
```
This effect makes the client do traces for each bullet, these client
traces ignore entities that have studio models. Traces are 4096 long.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=11m27s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.