# read_logdata
#### Syntax
```
native read_logdata(output[], len);
```

#### Usage
output | ```Buffer to copy log message to```
---|---
len | ```Maximum buffer size```
#### Description
```
Retrieves current log message.
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


  
  

