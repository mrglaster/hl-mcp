# dbg_trace_info
#### Syntax
```
native dbg_trace_info(trace, &line, function[], maxLength1, file[], maxLength2);
```

#### Usage
trace | ```Trace handle```
---|---
line | ```Variable to set line at which plugin failed to```
function | ```Buffer to copy function to```
maxLength1 | ```Maximum function buffer size```
file | ```Buffer to copy filename to```
maxLength2 | ```Maximum filename buffer size```
#### Description
```
Retrieves the call stack info for a trace.
```

#### Return
```
1 on success, 0 if no trace data is available
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

