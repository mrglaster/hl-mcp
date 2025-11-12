# abort
#### Syntax
```
native abort(error, const fmt[] = "", any:...);
```

#### Usage
error | ```Error code```
---|---
fmt | ```Formatting rules```
... | ```Variable list of formatting parameters```
#### Description
```
Aborts execution of the current callback by throwing an error.
```

#### Note
```
Warning: This function should not be used inside error filters, module
filters (native filters are safe if trap equals 1) or the
plugin_natives() forward.
```

#### Note
```
The message will automatically be tagged with the plugin's name and the
log will include a timestamp with the message.
```

#### Note
```
For a list of possible error codes, see AMX_* constants in amxconst.inc
```

#### Return
```
This function has no return value.
```

#### Error
```
The function is guaranteed to throw an error, using the
specified custom log message.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

