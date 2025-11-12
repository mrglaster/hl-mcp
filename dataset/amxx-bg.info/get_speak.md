# get_speak
#### Syntax
```
native get_speak(iIndex);
```

#### Usage
iIndex | ```Client index```
---|---
#### Description
```
Returns the engine module speak flags currently set on a client.
```

#### Note
```
For a list of available flags see the SPEAK_* constants in
engine_const.inc
```

#### Return
```
Client speak flags
```

#### Error
```
If the client index is not within the range of 1 to
MaxClients, or the client is not connected, an error will be
thrown.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

