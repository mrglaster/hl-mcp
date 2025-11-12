# cs_set_user_defuse
#### Syntax
```
native cs_set_user_defuse(index, defusekit = 1, r = 0, g = 160, b = 0, icon[] = "defuser", flash = 0);
```

#### Usage
index | ```Client index```
---|---
defusekit | ```If nonzero the client will have a defusekit, otherwise it will be removed```
r | ```Red component of icon color```
g | ```Green component of icon color```
b | ```Blue component of icon color```
icon | ```HUD sprite to use as icon```
flash | ```If nonzero the icon will flash red```
#### Description
```
Sets the client's defusekit status and allows to set a custom HUD icon and
color.
```

#### Return
```
This function has no return value.
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error
will be thrown.
```


This code is a part of cstrike.inc. To use this code you should include cstrike.inc as ```#include <cstrike>```


  
  

Warning: This include is compatible only with Counter-Strike 1.6 and will not function with other mods (e.g., Valve, Day of Defeat, etc.).