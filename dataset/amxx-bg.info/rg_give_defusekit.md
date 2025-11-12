# rg_give_defusekit
#### Syntax
```
native rg_give_defusekit(const index, const bool:bDefusekit = true, const Float:color[] = {0.0, 160.0, 0.0}, const icon[] = "defuser", const bool:bFlash = false);
```

#### Usage
index | ```Client index```
---|---
defusekit | ```If nonzero the client will have a defusekit, otherwise it will be removed```
color | ```Color RGB```
icon | ```HUD sprite to use as an icon```
flash | ```If nonzero the icon will flash red```
#### Description
```
Sets the client's defusekit status and allows to set a custom HUD icon and color.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.