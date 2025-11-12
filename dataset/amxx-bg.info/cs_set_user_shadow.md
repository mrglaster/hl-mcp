# cs_set_user_shadow
#### Syntax
```
stock cs_set_user_shadow(id, shadowid = 0, bool:reliable = true)
```

#### Usage
id | ```Client index or 0 for all clients```
---|---
shadowid | ```Sprite index or 0 to disable the shadow```
reliable | ```If true, the message will be sent via the reliable channel, otherwise it will use the unreliable one```
#### Description
```
Creates/Hides the shadow beneath players.
```

#### Note
```
This stock can't be used to set shadow to a specific player. It can
only set the shadow that a specific player sees for all other players.
```

#### Return
```
0 if "id" is non-zero and the client isn't connected,
1 otherwise
```


This code is a part of msgstocks.inc. To use this code you should include msgstocks.inc as ```#include <msgstocks>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.