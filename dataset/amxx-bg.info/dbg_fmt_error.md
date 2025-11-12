# dbg_fmt_error
#### Syntax
```
native dbg_fmt_error(buffer[], maxLength);
```

#### Usage
buffer | ```Buffer to copy error message to```
---|---
maxLength | ```Maximum buffer size```
#### Description
```
Retrieves the formatted error string from a trace.
```

#### Note
```
The string format is generally: "Run time error <errno>: <description>"
```

#### Return
```
1 on success, 0 if no trace data is available
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

