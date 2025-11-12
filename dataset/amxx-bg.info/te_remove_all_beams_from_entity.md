# te_remove_all_beams_from_entity
#### Syntax
```
stock te_remove_all_beams_from_entity(entity, receiver = 0, bool:reliable = true)
```

#### Usage
entity | ```Entity id to remove attached beams from```
---|---
receiver | ```Client index that will be able to see the changes or 0 for all clients```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Removes all beams attached to an entity.
```

#### Note
```
Video preview of this and all other te_ stocks can be found here:
https://youtu.be/szW-bSMPuyQ?t=7m7s
```

#### Return
```
0 if "receiver" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.