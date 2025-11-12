# rg_send_audio
#### Syntax
```
native rg_send_audio(const index, const sample[], const pitch = PITCH_NORM);
```

#### Usage
index | ```Receiver index or use 0 for everyone```
---|---
sample | ```Sound file to play```
pitch | ```Sound pitch```
#### Description
```
Sends the SendAudio message - plays the specified audio.
```

#### Return
```
This function has no return value.
```


This code is a part of reapi_gamedll.inc. To use this code you should include reapi_gamedll.inc as ```#include <reapi_gamedll>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it. The include requires ReGameDLL for correct work.