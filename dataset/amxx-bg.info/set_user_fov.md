# set_user_fov
#### Syntax
```
stock set_user_fov(id, fov = 0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
fov | ```Field of view degrees (0 - 255)```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Changes the client's field of view (FOV).
```

#### Note
```
Setting the "fov" argument below 45 will also draw a sniper scope.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.