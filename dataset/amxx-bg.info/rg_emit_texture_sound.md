# rg_emit_texture_sound
#### Syntax
```
native rg_emit_texture_sound(const ptr, Float:vecSrc[3], Float:vecEnd[3], Bullet:iBulletType);
```

#### Usage
ptr | ```Traceresult pointer, use Fakemeta's create_tr2 to instantiate one```
---|---
vecSrc | ```Start position```
vecEnd | ```End position, must match ptr's vecEndPos member```
iBulletType | ```Bullet type, see BULLET_* constants in cssdk_const.inc```
#### Description
```
Emits a sound based on a traceresult simulating a bullet hit (metal, wood, concrete, etc.).
```

#### Note
```
Used mostly on trace attacks (bullets, knife).
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.