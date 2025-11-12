# unpause
#### Syntax
```
native unpause(const flag[], const param1[] = "", const param2[] = "");
```

#### Usage
flag | ```Pause flags   "a" - pause plugin   "c" - search for other plugins using param1```
---|---
param1 | ```Plugin filename```
param2 | ```Unused and ignored```
#### Description
```
Unpauses a plugin so it will resume execution if it was previously paused.
```

#### Note
```
This used to be able to unpause specific functions, but this
functionality (along with the flags "b" and "e") has been deprecated.
```

#### Note
```
Without specifying flag "c" this function will do nothing, as a plugin
is incapable of unpausing itself. This is a relict of the deprecated
functionality.
```

#### Return
```
1 on success, 0 otherwise
```

#### Error
```
If it is attempted to use the deprecated functionality,
an error is thrown.
```


This code is a part of amxmodx.inc. To use this code you should include amxmodx.inc as ```#include <amxmodx>```


  
  

