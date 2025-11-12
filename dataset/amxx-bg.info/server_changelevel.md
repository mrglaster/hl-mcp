# server_changelevel
#### Syntax
```
forward server_changelevel(map[]);
```

#### Usage
map | ```Map that the mod tries to change to```
---|---
#### Description
```
Called when the mod tries to change the map.
```

#### Note
```
This is *only* called if the mod itself handles the map change. The
server command "changelevel", which is used by many plugins, will not
trigger this forward. Unfortunately, this means that in practice this
forward can be unreliable and will not be called in many situations.
```

#### Note
```
AMXX 1.8.3 has added the engine_changelevel() function, which will utilize
the correct engine function to change the map, and therefore trigger
this forward.
```

#### Return
```
PLUGIN_CONTINUE to let the mod change the map
PLUGIN_HANDLED or higher to prevent the map change
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

