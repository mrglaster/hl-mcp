# dbg_trace_begin
#### Syntax
```
native dbg_trace_begin();
```

#### Description
```
Returns a trace handle for the item at the top of the traced call stack.
```

#### Note
```
Intended for use inside an error handler set with set_error_filter()
```

#### Return
```
Trace handle, 0 if no debugging information is available
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

