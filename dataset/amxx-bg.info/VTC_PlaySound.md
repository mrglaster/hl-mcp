# VTC_PlaySound
#### Syntax
```
native VTC_PlaySound(const receiver, const soundFilePath[]);
```

#### Usage
receiver | ```Receiver index```
---|---
soundFilePath | ```The path to the sound file```
#### Description
```
Play the audio file via the voice stream.
```

#### Note
```
Usage example:
VTC_PlaySound(id, "sound/ambience/Opera.wav");
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_vtc.inc. To use this code you should include reapi_vtc.inc as ```#include <reapi_vtc>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires VTC for correct work