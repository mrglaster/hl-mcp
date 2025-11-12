# set_speak
#### Syntax
```
native set_speak(iIndex, iSpeakFlags);
```

#### Usage
iIndex | ```Client index```
---|---
iSpeakFlags | ```New flags to set```
#### Description
```
Sets the engine module speak flags on a client.
```

#### Note
```
For a list of available flags see the SPEAK_* constants in
engine_const.inc
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


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

