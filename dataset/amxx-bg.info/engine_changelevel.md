# engine_changelevel
#### Syntax
```
native engine_changelevel(const map[]);
```

#### Usage
map | ```Map name to change to```
---|---
#### Description
```
Changes the map.
```

#### Note
```
This calls the pfnChangelLevel engine function.
```

#### Note
```
This has the same behavior as using the "changelevel" server command,
but will also trigger the server_changelevel() forward in AMXX
plugins. It will also notify any Metamod plugins that are hooking
the pfnChangeLevel function.
```

#### Return
```
This function has no return value.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

