# read_logargv
#### Syntax
```
native read_logargv(id, output[], len);
```

#### Usage
id | ```Argument index, starting from 0```
---|---
output | ```Buffer to copy log argument to```
len | ```Maximum buffer size```
#### Description
```
Retrieves argument of log message.
```

#### Note
```
Should only be used inside of the plugin_log() forward.
```

#### Return
```
Number of cells written to buffer
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

