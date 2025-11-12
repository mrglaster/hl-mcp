# create_cvar
#### Syntax
```
native create_cvar(const name[], const string[], flags = FCVAR_NONE, const description[] = "", bool:has_min = false, Float:min_val = 0.0, bool:has_max = false, Float:max_val = 0.0);
```

#### Usage
name | ```Cvar name```
---|---
string | ```Default cvar value```
flags | ```Optional bitsum of flags specifying cvar behavior```
description | ```Optional description of the cvar```
has_min | ```Optional boolean that specifies if the cvar has a minimum value```
min_val | ```Minimum floating point value```
has_max | ```Optional boolean that specifies if the cvar has a maximum value```
max_val | ```Maximum floating point value```
#### Description
```
Creates a new cvar for the engine.
```

#### Note
```
This has the same effect as register_cvar() but provides more options.
```

#### Note
```
For a list of possible cvar flags see FCVAR_* constants above.
```

#### Note
```
If an already existing cvar is registered it will not be duplicated.
The default value is only set when the cvar is registered for the very
first time since the server was started. Cvar bounds are overwritten
by the create_cvar() call just as if they were re-set using
set_pcvar_bounds().
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

#### Error
```
If invalid bounds are provided (min_val > max_val or
vice versa), an error will be thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

