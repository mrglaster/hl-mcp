# te_create_projectile
#### Syntax
```
stock te_create_projectile(position[3], velocity[3], model, life = 10, owner = 0, receiver = 0, bool:reliable = true)
```

#### Usage
position | ```Projectile position```
---|---
velocity | ```Projectile velocity```
model | ```Model index that will be used for the projectile```
life | ```The length of time the projectile shall remain (0 - 255)```
owner | ```The projectile won't collide with the owner, if set to 0, the projectile will hit any client```
receiver | ```Client index that will be able to see the projectile or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates a nail-like projectile.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=10m12s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.