# register_think
#### Syntax
```
native register_think(const Classname[], const function[]);
```

#### Usage
Classname | ```Entity classname to hook```
---|---
function | ```Name of callback function```
#### Description
```
Registers a function to be called on entity think on all entities of a
specified class.
```

#### Note
```
The function will be called in the following manner:

public think_handler(entity)

  entity    - Index of entity thinking
```

#### Note
```
The callback should return PLUGIN_CONTINUE to ignore the think,
PLUGIN_HANDLED or higher to block it.
```

#### Note
```
When returning PLUGIN_HANDLED from the callback, Engine will still fire
other think functions like the pfn_think() forward before actually
blocking the think. To immediately block return PLUGIN_HANDLED_MAIN
instead.
```

#### Return
```
Think forward id
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

