# precache_sound
#### Syntax
```
native precache_sound(const name[]);
```

#### Usage
name | ```Path to the sound file```
---|---
#### Description
```
Precaches a sound file.
```

#### Note
```
Can only be used inside of the plugin_precache() forward.
```

#### Note
```
The filepath is always relative to the "sound" folder, and the file has
to be a wav file. Precaching a file with this will add it to the engine
sound table, making it available for usage in emit_sound() for example.
```

#### Note
```
Precaching other filetypes (such as mp3 music), optionally in different
locations, has to be done with precache_generic()
```

#### Return
```
Unique cache id of the sound
```

#### Error
```
If called outside of the plugin_precache() forward, an error is
thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

