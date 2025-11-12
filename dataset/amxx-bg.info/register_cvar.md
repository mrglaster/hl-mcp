# register_cvar
#### Syntax
```
native register_cvar(const name[], const string[], flags = FCVAR_NONE, Float:fvalue = 0.0);
```

#### Usage
name | ```Cvar name```
---|---
string | ```Default cvar value```
flags | ```Optional bitsum of flags specifying cvar behavior```
fvalue | ```Unused```
#### Description
```
Registers a new cvar for the engine.
```

#### Note
```
Deprecated. Consider to use create_cvar for more options.
```

#### Note
```
For a list of possible cvar flags see FCVAR_* constants in cvars.inc
```

#### Note
```
If an already existing cvar is registered it will not be duplicated.
The default value is only set when the cvar is registered for the very
first time since the server was started.
```

#### Note
```
The returned cvar pointer should be used with the get_pcvar_* and
set_pcvar_* set of functions.
```

#### Return
```
Unique cvar pointer
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

