# client_impulse
#### Syntax
```
forward client_impulse(id, impulse);
```

#### Usage
id | ```Client index```
---|---
impulse | ```Impulse triggered by client```
PLUGIN_CONTINUE | ```to ignore, PLUGIN_HANDLED or higher to                  nullify impulse (CmdStart() is not blocked)```
#### Description
```
Called when a client triggers an impulse.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

