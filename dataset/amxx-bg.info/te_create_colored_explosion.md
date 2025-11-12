# te_create_colored_explosion
#### Syntax
```
stock te_create_colored_explosion(position[3], startcolor = 0, numcolors = 255, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Position of the explosion```
---|---
startcolor | ```Starting color (0 - 255)```
numcolors | ```Number of colors (1 - 255)```
receiver | ```Client index that will be able to see the explosion or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a Quake colormapped (base palette) particle explosion with sound.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=2m19s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.