# okapi_add_hook
#### Syntax
```
native okapi_hook:okapi_add_hook(okapi_func:func, const callback[], post = 0);
```

#### Usage
func | ```Handler to the function returned by an attach function```
---|---
callback | ```Nname of the public function in the code that will be```
#### Description
```
Adds a hook to a previously attached function.
```

#### Return
```
Handler to the hook
```

#### Error
```
Inexistant callback
```


This code is a part of okapi.inc. To use this code you should include okapi.inc as ```#include <okapi>```


  
  

Warning! This is an external include! It does not come bundled with AMX Mod X "out of the box" and requires additional installation. Use it only if you are absolutely certain that you need it.