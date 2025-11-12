# enable_cvar_hook
#### Syntax
```
native enable_cvar_hook(cvarhook:handle);
```

#### Usage
handle | ```Forward to enable```
---|---
#### Description
```
Enables a cvar hook, restoring it to being called.
```

#### Note
```
Use the handle returned by hook_cvar_change as the parameter here.
```

#### Error
```
If an invalid hook handle is provided, an error will be
thrown.
```


This code is a part of cvars.inc. To use this code you should include cvars.inc as ```#include <cvars>```


  
  

