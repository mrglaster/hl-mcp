# set_view
#### Syntax
```
native set_view(iIndex, ViewType);
```

#### Usage
iIndex | ```Client index```
---|---
ViewType | ```View mode```
#### Description
```
Sets the engine module view mode on a client.
```

#### Note
```
For a list of valid view modes see the CAMERA_* constants in
engine_const.inc
```

#### Note
```
The engine module uses a custom entity to achieve the camera effects
and requires "models/rpgrocket.mdl" to be precached by the plugin.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

