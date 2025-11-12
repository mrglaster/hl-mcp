# hook_cvar_change
#### Syntax
```
native cvarhook:hook_cvar_change(pcvar, const callback[]);
```

#### Usage
pcvar | ```Pointer to cvar```
---|---
callback | ```Name of callback function```
#### Description
```
Creates a hook for when a cvar's value is changed.
```

#### Note
```
Changing the cvar value from within this forward can lead to infinite
recursion and should be avoided.
```

#### Note
```
The callback will be called in the following manner:

public cvar_change_callback(pcvar, const old_value[], const new_value[])

  pcvar         - Pointer to cvar that was changed
  old_value     - Buffer containing the previous value of the cvar
  new_value     - Buffer containing the new value of the cvar

The return value is ignored
```

#### Return
```
Callback handle that can be used with
[disable|enable]_cvar_hook
```

#### Error
```
If an invalid cvar pointer or callback function is provided,
an error will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

