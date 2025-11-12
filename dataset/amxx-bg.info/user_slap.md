# user_slap
#### Syntax
```
native user_slap(index, power, rnddir = 1);
```

#### Usage
index | ```Client index```
---|---
power | ```Power of the slap```
rnddir | ```If set to zero the player will be slapped along it's aim vector, otherwise the direction will be randomized```
#### Description
```
Slaps the client with specified power. Killing the client if applicable.
```

#### Note
```
This removes "power" amount of health from the client, performing
a kill if they have no health left after the slap.
```

#### Note
```
The function will apply a velocity to the client that is independent
of the slap power. The slap direction can be influenced by the third
parameter.
```

#### Return
```
1 if user is alive and slap succeeded, 0 otherwise
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

