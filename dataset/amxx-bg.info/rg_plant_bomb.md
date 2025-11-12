# rg_plant_bomb
#### Syntax
```
native rg_plant_bomb(const index, Float:vecOrigin[3], Float:vecAngles[3] = {0.0,0.0,0.0});
```

#### Usage
index | ```Owner index or 0 for worldspawn.```
---|---
origin | ```The origin of the bomb where it will be planted.```
angles | ```The angles of the planted bomb.```
#### Description
```
Plant a bomb.
```

#### Return
```
Index of bomb entity or AMX_NULLENT (-1) otherwise
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.