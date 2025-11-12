# shake_user_screen
#### Syntax
```
stock shake_user_screen(id, Float:amplitude = 3.0, Float:duration = 3.0, Float:frequency = 1.0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
amplitude | ```Shake amplitude (0 - 16)```
duration | ```Shake duration (in seconds) (0 - 16)```
frequency | ```Delay between each shake (0 - 16)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Shakes the client's screen.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.