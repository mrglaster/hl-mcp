# client_cmdStart
#### Syntax
```
forward client_cmdStart(id);
```

#### Usage
id | ```Client index```
---|---
#### Description
```
Called for CmdStart() on a client.
```

#### Note
```
Use [get|set]_usercmd() to read and modify information in the usercmd
struct.
```

#### Return
```
PLUGIN_CONTINUE to ignore, PLUGIN_HANDLED or higher to block
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

