# pfn_touch
#### Syntax
```
forward pfn_touch(ptr, ptd);
```

#### Usage
ptr | ```Index of entity being touched```
---|---
ptd | ```Index of entity touching```
#### Description
```
Called when two entities touch.
```

#### Return
```
PLUGIN_CONTINUE to ignore, PLUGIN_HANDLED or higher to block
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

