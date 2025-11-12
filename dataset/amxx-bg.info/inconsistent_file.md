# inconsistent_file
#### Syntax
```
forward inconsistent_file(id, const filename[], reason[64]);
```

#### Usage
id | ```Client index```
---|---
filename | ```Detected file```
reason | ```Buffer storing the disconnect reason (can be overwritten)```
#### Description
```
Called when an inconsistent file is encountered by the engine.
```

#### Return
```
PLUGIN_CONTINUE to let the engine kick the client
PLUGIN_HANDLED to block the inconsistency kick
```


This code is a part of amxmodx.inc . To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

