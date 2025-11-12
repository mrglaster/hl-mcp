# cs_play_reload_sound
#### Syntax
```
stock cs_play_reload_sound(id, bool:shotgun = false, volume = 100, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
shotgun | ```If set to true, it will play "weapons/generic_shot_reload.wav", otherwise it will play "weapons/generic_reload.wav".```
volume | ```Volume amount (0 - 255)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Plays a generic reload sound.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.