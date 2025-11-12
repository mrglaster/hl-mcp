# set_usercmd
#### Syntax
```
native set_usercmd(type, any:...);
```

#### Usage
type | ```Entry to write to```
---|---
... | ```Depending on the entry type a different additional parameter should be provided:    int      - Second parameter should be an integer variable    float    - Second parameter should be a float variable    vector   - Second parameter should be a Float:array[3]```
#### Description
```
Sets a value in a usercmd struct.
```

#### Note
```
This native can only be used inside the client_cmdStart() forward.
```

#### Note
```
For a list of valid usercmd entries see the usercmd_* constants in
engine_const.inc
```

#### Note
```
Changes will be immediately reflected in get_usercmd() for all plugins.
```

#### Return
```
This function has no return value.
```


This code is a part of engine.inc. To use this code you should include engine.inc as ```#include <engine>```


  
  

