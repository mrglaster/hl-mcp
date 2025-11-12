# pause
#### Syntax
```
native pause(const flag[], const param1[] = "", const param2[] = "");
```

#### Usage
flag | ```Pause flags   "a" - pause plugin   "c" - search for other plugins using param1   "d" - stop plugin, making it unavailable to unpause```
---|---
param1 | ```Plugin filename```
param2 | ```Unused and ignored```
#### Description
```
Pauses a plugin so it will not be executed until it is unpaused.
```

#### Note
```
This used to be able to pause specific functions, but this functionality
(along with the flags "b" and "e") has been deprecated.
```

#### Note
```
If used without flag "c" this will pause the calling plugin.
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


  
  

