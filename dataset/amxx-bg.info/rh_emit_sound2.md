# rh_emit_sound2
#### Syntax
```
native bool:rh_emit_sound2(const entity, const recipient, const channel, const sample[], Float:vol = VOL_NORM, Float:attn = ATTN_NORM, const flags = 0, const pitch = PITCH_NORM, emitFlags = 0, const Float:origin[3] = {0.0,0.0,0.0});
```

#### Usage
entity | ```Entity index or use 0 to emit from worldspawn at the specified position```
---|---
recipient | ```Recipient index or use 0 to make all clients hear it```
channel | ```Channel to emit from```
sample | ```Sound file to emit```
vol | ```Volume in percents```
attn | ```Sound attenuation```
flags | ```Emit flags```
pitch | ```Sound pitch```
emitFlags | ```Additional Emit2 flags, look at the defines like SND_EMIT2_*```
origin | ```Specify origin and only on "param" entity worldspawn that is 0```
#### Description
```
Emits a sound from an entity from the engine.
```

#### Return
```
true if the emission was successfull, false otherwise
```


This code is a part of reapi_engine.inc . To use this code you should include reapi_engine.inc as ```#include <reapi_engine>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.