# emit_sound
#### Syntax
```
native emit_sound(index, channel, const sample[], Float:vol, Float:att, flags, pitch);
```

#### Usage
index | ```Entity index, use 0 to emit from all clients```
---|---
channel | ```Channel to emit from```
sample | ```Sound file to emit```
vol | ```Volume in percent```
att | ```Sound attenuation```
flags | ```Emit flags```
pitch | ```Sound pitch```
#### Description
```
Emits a sound from an entity from the engine.
```

#### Note
```
The sample must be precached using precache_sound() so it is available
in the engine's sound table.
```

#### Note
```
For a list of available channels, see CHAN_* constants in amxconst.inc,
sounds emitted from the same channel will override each other.
```

#### Note
```
There are helpful reference constants in amxconst.inc for sound volume
(VOL_*), attenuation (ATTN_*), flags (SND_*), and pitch (PITCH_*).
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

